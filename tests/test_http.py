"""
The shared HTTP layer every client builds on: retries and the eval cache.

httpx.MockTransport answers requests from a Python function, so these
tests exercise the real transport classes without any network.
"""
import httpx
import pytest

import target_atlas.utils.http as http


@pytest.fixture(autouse=True)
def no_sleep(monkeypatch):
    # Backoff is 2/4/8 s — patch it out so the suite stays fast
    monkeypatch.setattr(http.time, "sleep", lambda seconds: None)


@pytest.fixture(autouse=True)
def cache_off_after_test():
    yield
    http.disable_cache()   # enable_cache() is global state; never leak it into other tests


def scripted(*statuses):
    """MockTransport returning the given statuses in order; records call count."""
    calls = []

    def handler(request):
        calls.append(request)
        return httpx.Response(statuses[min(len(calls), len(statuses)) - 1], text="body")

    return httpx.MockTransport(handler), calls


def test_retry_recovers_from_transient_errors():
    inner, calls = scripted(503, 500, 200)
    client = httpx.Client(transport=http.RetryTransport(inner=inner))

    assert client.get("https://api.example/x").status_code == 200
    assert len(calls) == 3


def test_retry_does_not_repeat_client_errors():
    inner, calls = scripted(404)
    client = httpx.Client(transport=http.RetryTransport(inner=inner))

    assert client.get("https://api.example/x").status_code == 404
    assert len(calls) == 1          # a bad request cannot be fixed by repeating it


def test_retry_gives_up_after_the_last_attempt():
    inner, calls = scripted(503)
    client = httpx.Client(transport=http.RetryTransport(inner=inner, retries=3))

    assert client.get("https://api.example/x").status_code == 503
    assert len(calls) == 4          # 1 attempt + 3 retries


def test_cache_replays_successful_responses(tmp_path):
    inner, calls = scripted(200)
    client = httpx.Client(transport=http.CachingTransport(tmp_path, inner=inner))

    first = client.get("https://api.example/x")
    second = client.get("https://api.example/x")

    assert first.text == second.text == "body"
    assert len(calls) == 1          # second answer came from disk


@pytest.mark.parametrize("status", [500, 429])
def test_cache_never_stores_transient_failures(tmp_path, status):
    inner, calls = scripted(status)
    client = httpx.Client(transport=http.CachingTransport(tmp_path, inner=inner))

    client.get("https://api.example/x")
    client.get("https://api.example/x")

    assert len(calls) == 2          # an outage must not be frozen into later runs
    assert not any(tmp_path.rglob("*.json"))


def test_cache_key_includes_the_request_body(tmp_path):
    # RCSB search is a POST: two different queries to one URL are different answers
    inner, calls = scripted(200)
    client = httpx.Client(transport=http.CachingTransport(tmp_path, inner=inner))

    client.post("https://api.example/search", json={"q": "P00533"})
    client.post("https://api.example/search", json={"q": "Q9NZC2"})

    assert len(calls) == 2


def test_http_client_uses_the_cache_only_when_enabled(tmp_path):
    with http.http_client(timeout=1.0) as client:
        assert isinstance(client._transport, http.RetryTransport)

    http.enable_cache(tmp_path)
    with http.http_client(timeout=1.0) as client:
        assert isinstance(client._transport, http.CachingTransport)
        assert isinstance(client._transport.inner, http.RetryTransport)   # cache outside, retry inside
