import json

import pandas as pd

from statistical_enrichment.services.enrichment.enrich_methods.fisher import (
    add_q_value,
    fisher,
    fisher_p,
)


def test_fisher_p_returns_value_between_zero_and_one():
    """fisher_p should always return a probability in [0, 1]."""
    p = fisher_p(k=5, M=100, n=20, N=30)
    assert 0 <= p <= 1


def test_fisher_p_increases_with_fewer_matches():
    """
    Fewer matching drawn objects (lower k) should yield a less significant
    (higher) p-value than a perfect overlap.
    """
    p_high_overlap = fisher_p(k=5, M=100, n=5, N=5)
    p_low_overlap = fisher_p(k=0, M=100, n=5, N=5)
    assert p_high_overlap < p_low_overlap


def test_add_q_value_adds_columns():
    """add_q_value should add 'q-value' and 'rejected' columns to the DataFrame."""
    df = pd.DataFrame({"p-value": [0.01, 0.05, 0.10]})
    add_q_value(df, related_go_terms_count=10)
    assert "q-value" in df.columns
    assert "rejected" in df.columns


def test_add_q_value_correct_length():
    """add_q_value should not change the number of rows."""
    df = pd.DataFrame({"p-value": [0.01, 0.05, 0.10]})
    add_q_value(df, related_go_terms_count=10)
    assert len(df) == 3


def test_fisher_returns_json_list():
    """fisher() should return a JSON-encoded list of enrichment results."""
    go_terms = [
        {
            "goId": "GO:0006915",
            "goTerm": "apoptotic process",
            "goLabel": ["biological_process"],
            "geneNames": ["BRCA1", "TP53", "EGFR"],
        },
        {
            "goId": "GO:0007049",
            "goTerm": "cell cycle",
            "goLabel": ["biological_process"],
            "geneNames": ["CDK2", "CDK4", "CCND1"],
        },
    ]
    gene_names = ["BRCA1", "TP53"]

    result_json = fisher(gene_names, go_terms, related_go_terms_count=2)

    result = json.loads(result_json)
    assert isinstance(result, list)


def test_fisher_includes_overlapping_go_terms():
    """GO terms that overlap with the query genes should appear in results."""
    go_terms = [
        {
            "goId": "GO:0006915",
            "goTerm": "apoptotic process",
            "goLabel": ["biological_process"],
            "geneNames": ["BRCA1", "TP53", "EGFR"],
        },
        {
            "goId": "GO:0007049",
            "goTerm": "cell cycle",
            "goLabel": ["biological_process"],
            "geneNames": ["CDK2", "CDK4", "CCND1"],
        },
    ]
    gene_names = ["BRCA1", "TP53"]

    result_json = fisher(gene_names, go_terms, related_go_terms_count=2)
    result = json.loads(result_json)

    go_ids = [r["goId"] for r in result]
    assert "GO:0006915" in go_ids


def test_fisher_results_sorted_by_p_value():
    """Results should be sorted by p-value in ascending order."""
    go_terms = [
        {
            "goId": "GO:0006915",
            "goTerm": "apoptotic process",
            "goLabel": ["biological_process"],
            "geneNames": ["BRCA1", "TP53", "EGFR"],
        },
        {
            "goId": "GO:0007049",
            "goTerm": "cell cycle",
            "goLabel": ["biological_process"],
            "geneNames": ["CDK2", "CDK4", "CCND1", "BRCA1"],
        },
    ]
    gene_names = ["BRCA1", "TP53"]

    result_json = fisher(gene_names, go_terms, related_go_terms_count=2)
    result = json.loads(result_json)

    p_values = [r["p-value"] for r in result]
    assert p_values == sorted(p_values)
