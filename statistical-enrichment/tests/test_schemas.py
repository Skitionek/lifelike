import pytest
from marshmallow import ValidationError

from statistical_enrichment.schemas import (
    Organism,
    OrganismField,
    GeneOrganismSchema,
    EnrichmentSchema,
)


def test_organism_str():
    org = Organism(id=9606, name="Homo sapiens")
    assert str(org) == "9606/Homo sapiens"


def test_organism_field_deserialize_valid():
    field = OrganismField()
    result = field._deserialize("9606/Homo sapiens", None, None)
    assert result.id == "9606"
    assert result.name == "Homo sapiens"


def test_organism_field_deserialize_preserves_id_as_string():
    """The organism id should be kept as the raw string value from the input."""
    field = OrganismField()
    result = field._deserialize("9606/Homo sapiens", None, None)
    # id is stored as the raw string (not cast to int at this level)
    assert result.id == "9606"


def test_gene_organism_schema_valid():
    schema = GeneOrganismSchema()
    result = schema.load({
        "geneNames": ["BRCA1", "TP53"],
        "organism": "9606/Homo sapiens",
    })
    assert result["geneNames"] == ["BRCA1", "TP53"]
    assert str(result["organism"]) == "9606/Homo sapiens"


def test_gene_organism_schema_empty_gene_list():
    schema = GeneOrganismSchema()
    result = schema.load({
        "geneNames": [],
        "organism": "9606/Homo sapiens",
    })
    assert result["geneNames"] == []


def test_enrichment_schema_valid():
    schema = EnrichmentSchema()
    result = schema.load({
        "geneNames": ["BRCA1", "TP53"],
        "organism": "9606/Homo sapiens",
        "analysis": "fisher",
    })
    assert result["analysis"] == "fisher"


def test_enrichment_schema_invalid_analysis():
    schema = EnrichmentSchema()
    with pytest.raises(ValidationError):
        schema.load({
            "geneNames": ["BRCA1", "TP53"],
            "organism": "9606/Homo sapiens",
            "analysis": "invalid_method",
        })
