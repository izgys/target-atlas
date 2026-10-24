"""Builders for eval-result dicts shared by the repeat and tracking tests."""


def score(value):
    return {"score": value}


def levels(druggability="high", structural="high", chemical="high", literature="high"):
    return {
        "druggability_score": druggability,
        "structural_confidence": structural,
        "chemical_confidence": chemical,
        "literature_confidence": literature,
    }


def result(query, identity=1.0, recall=0.5, citation=1.0, gap=1.0, verdict=None):
    return {
        "query": query,
        "identity": score(identity),
        "fact_recall": {"score": recall, "categories": {
            c: {"found": 1, "expected": 2} for c in ("pdb_ids", "approved_drugs", "pmids")
        }},
        "citation": score(citation),
        "gap_honesty": score(gap),
        "levels": verdict or levels(),
    }


def make_pass(repeat, results):
    import statistics

    metrics = ["identity", "fact_recall", "citation", "gap_honesty"]
    aggregate = {}
    for m in metrics:
        values = [r[m]["score"] for r in results if m in r and r[m]["score"] is not None]
        aggregate[m] = statistics.mean(values) if values else None
    return {"repeat": repeat, "targets": results, "aggregate": aggregate}
