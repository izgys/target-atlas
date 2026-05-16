import httpx
import time
from pydantic import BaseModel


EUTILS_BASE = "https://eutils.ncbi.nlm.nih.gov/entrez/eutils"


class Publication(BaseModel):
    """A recent publication mentioning this target."""
    pubmed_id: str
    title: str
    abstract: str | None = None
    year: int | None = None
    journal: str | None = None


def fetch_publications(
    gene_name: str,
    max_results: int = 20,
) -> list[Publication]:
    """
    Fetch recent publications mentioning a gene target from PubMed.

    Two-step process: ESearch returns PMIDs, ESummary fetches metadata.
    Results are sorted by date descending — most recent first.

    Args:
        gene_name: gene symbol e.g. 'EGFR'
        max_results: maximum publications to return (default 20)

    Returns:
        list of Publication objects sorted by date descending
        empty list if no results or API unavailable
    """
    pmids = _esearch(gene_name, max_results)

    if not pmids:
        return []

    # Respect NCBI rate limit — 3 requests/second without API key
    time.sleep(0.4)

    publications = _efetch(pmids)
    return publications


def _esearch(gene_name: str, max_results: int) -> list[str]:
    """
    Search PubMed for PMIDs matching a gene symbol in the title field.
    Title-only search is significantly more precise than title/abstract —
    a paper with the gene symbol in its title is almost certainly about
    that gene. Abstract-level matching produces too much off-target noise
    from papers that mention the gene in passing.
    """
    query = f'"{gene_name}"[Title] AND human[organism]'

    with httpx.Client(timeout=15.0) as client:
        response = client.get(
            f"{EUTILS_BASE}/esearch.fcgi",
            params={
                "db": "pubmed",
                "term": query,
                "retmax": max_results,
                "sort": "date",
                "retmode": "json",
            }
        )
        response.raise_for_status()
        data = response.json()

    id_list = data.get("esearchresult", {}).get("idlist", [])
    return id_list

def _efetch(pmids: list[str]) -> list[Publication]:
    """
    Fetch title, abstract, year and journal for a list of PMIDs.

    Uses ESummary endpoint which returns JSON metadata.
    Abstract text requires EFetch with XML — handled separately
    via _fetch_abstracts if pmids list is non-empty.

    Args:
        pmids: list of PubMed ID strings

    Returns:
        list of Publication objects
    """
    ids_str = ",".join(pmids)

    with httpx.Client(timeout=15.0) as client:
        response = client.get(
            f"{EUTILS_BASE}/esummary.fcgi",
            params={
                "db": "pubmed",
                "id": ids_str,
                "retmode": "json",
            }
        )
        response.raise_for_status()
        data = response.json()

    results = data.get("result", {})
    # 'uids' key contains the ordered list of PMIDs
    uids = results.get("uids", [])

    publications = []
    for uid in uids:
        entry = results.get(uid, {})
        pub = _parse_summary(uid, entry)
        if pub:
            publications.append(pub)

    # Fetch abstracts separately — ESummary doesn't include them
    time.sleep(0.4)
    _enrich_abstracts(publications)

    return publications


def _parse_summary(pmid: str, entry: dict) -> Publication | None:
    """
    Parse a single ESummary entry into a Publication object.
    """
    title = entry.get("title", "").strip()
    if not title:
        return None

    # Publication year from sortpubdate field e.g. "2024/03/15 00:00"
    sortpubdate = entry.get("sortpubdate", "")
    year = None
    if sortpubdate:
        try:
            year = int(sortpubdate.split("/")[0])
        except (ValueError, IndexError):
            pass

    journal = entry.get("source", None)

    return Publication(
        pubmed_id=pmid,
        title=title,
        year=year,
        journal=journal,
    )


def _enrich_abstracts(publications: list[Publication]) -> None:
    """
    Fetch and attach abstracts for a list of publications in place.

    Uses EFetch with rettype=abstract and retmode=xml.
    Parses AbstractText from the XML response.
    Modifies publications list in place — no return value.
    """
    if not publications:
        return

    ids_str = ",".join(p.pubmed_id for p in publications)

    with httpx.Client(timeout=20.0) as client:
        response = client.get(
            f"{EUTILS_BASE}/efetch.fcgi",
            params={
                "db": "pubmed",
                "id": ids_str,
                "rettype": "abstract",
                "retmode": "xml",
            }
        )
        response.raise_for_status()
        xml_text = response.text

    # Parse abstracts from XML using simple string extraction
    # Avoids xml library dependency for a straightforward field
    abstract_map = _parse_abstracts_from_xml(xml_text, publications)

    for pub in publications:
        pub.abstract = abstract_map.get(pub.pubmed_id)


def _parse_abstracts_from_xml(
    xml_text: str,
    publications: list[Publication]
) -> dict[str, str]:
    """
    Extract PMID → abstract text mapping from PubMed XML response.

    PubMed XML structure for each article:
    <PubmedArticle>
        <MedlineCitation>
            <PMID>12345678</PMID>
            <Article>
                <Abstract>
                    <AbstractText>Abstract content here...</AbstractText>
                </Abstract>
            </Article>
        </MedlineCitation>
    </PubmedArticle>
    """
    import xml.etree.ElementTree as ET

    abstract_map = {}

    try:
        root = ET.fromstring(xml_text)
        for article in root.findall(".//PubmedArticle"):
            # Extract PMID
            pmid_el = article.find(".//MedlineCitation/PMID")
            if pmid_el is None:
                continue
            pmid = pmid_el.text

            # Extract abstract — may have multiple AbstractText elements
            # (structured abstracts have sections like Background, Methods)
            abstract_els = article.findall(".//Abstract/AbstractText")
            if abstract_els:
                # Join sections with newline if structured abstract
                abstract = " ".join(
                    el.text for el in abstract_els if el.text
                )
                abstract_map[pmid] = abstract.strip()

    except ET.ParseError:
        # If XML parsing fails return empty map
        # Publications will have abstract=None
        pass

    return abstract_map