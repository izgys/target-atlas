"""
Shared HTTP client factory with an optional on-disk response cache.

Every API client builds its httpx.Client through http_client(). By default
this client only retries transient failures. When enable_cache() has been
called (the eval harness does this), requests also go through CachingTransport: each response is stored as
a JSON file keyed by method + URL + body, and replayed on later runs.

Caching at the transport layer keeps the clients unaware of it, and because
raw responses are stored, a fix to a client's parsing code applies to cached
data too.

Every client also retries transient failures (5xx, 429, timeouts) with
exponential backoff via RetryTransport, which sits underneath the cache:
cached responses return immediately, live ones get several attempts.
"""
import hashlib
import json
import time
from pathlib import Path

import httpx


_cache_dir: Path | None = None

RETRY_STATUSES = {429, 500, 502, 503, 504}


def enable_cache(cache_dir: str | Path) -> None:
    """Route all subsequent http_client() requests through the disk cache."""
    global _cache_dir
    _cache_dir = Path(cache_dir)
    _cache_dir.mkdir(parents=True, exist_ok=True)


def disable_cache() -> None:
    global _cache_dir
    _cache_dir = None


def http_client(timeout: float, **kwargs) -> httpx.Client:
    """Return an httpx.Client with retries, cached if enable_cache() is active."""
    transport: httpx.BaseTransport = RetryTransport()
    if _cache_dir is not None:
        transport = CachingTransport(_cache_dir, inner=transport)
    return httpx.Client(timeout=timeout, transport=transport, **kwargs)


class RetryTransport(httpx.BaseTransport):
    """
    httpx transport that retries transient failures with exponential backoff.

    Retries server errors, rate limits and timeouts — the failures that
    succeed on a second try (ChEMBL's intermittent 500s, NCBI's 429s).
    4xx client errors are returned immediately: retrying a bad request
    cannot fix it.
    """

    def __init__(
        self,
        inner: httpx.BaseTransport | None = None,
        retries: int = 3,
        backoff: float = 2.0,
    ):
        self.inner = inner or httpx.HTTPTransport()
        self.retries = retries
        self.backoff = backoff

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        for attempt in range(self.retries + 1):
            is_last = attempt == self.retries
            try:
                response = self.inner.handle_request(request)
            except (httpx.TimeoutException, httpx.NetworkError):
                if is_last:
                    raise
            else:
                if response.status_code not in RETRY_STATUSES or is_last:
                    return response
                response.close()

            time.sleep(self.backoff * 2 ** attempt)   # 2s, 4s, 8s

        raise RuntimeError("unreachable")


class CachingTransport(httpx.BaseTransport):
    """
    httpx transport that replays stored responses and records new ones.

    Only successful and 'not found' answers are stored (status < 500,
    except 429). Server errors and rate limits are transient — caching
    them would freeze an outage into every later run.
    """

    def __init__(self, cache_dir: Path, inner: httpx.BaseTransport | None = None):
        self.cache_dir = cache_dir
        self.inner = inner or httpx.HTTPTransport()

    def handle_request(self, request: httpx.Request) -> httpx.Response:
        path = self._cache_path(request)

        if path.exists():
            cached = json.loads(path.read_text(encoding="utf-8"))
            return httpx.Response(
                status_code=cached["status_code"],
                headers={"content-type": cached["content_type"]},
                content=cached["content"].encode("utf-8"),
                request=request,
            )

        response = self.inner.handle_request(request)
        response.read()   # decodes gzip etc., so the stored body is plain text

        if response.status_code < 500 and response.status_code != 429:
            path.parent.mkdir(parents=True, exist_ok=True)
            path.write_text(
                json.dumps({
                    "method": request.method,
                    "url": str(request.url),
                    "status_code": response.status_code,
                    "content_type": response.headers.get("content-type", ""),
                    "content": response.content.decode("utf-8", errors="replace"),
                }),
                encoding="utf-8",
            )

        return response

    def _cache_path(self, request: httpx.Request) -> Path:
        # Body matters for POST queries (RCSB search sends JSON)
        key = hashlib.sha256(
            request.method.encode()
            + str(request.url).encode()
            + request.content
        ).hexdigest()
        return self.cache_dir / request.url.host / f"{key}.json"
