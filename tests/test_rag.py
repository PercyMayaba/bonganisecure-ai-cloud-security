import pytest

from app.rag import retrieve_documents


def test_risk_user_can_access_risk_document():
    results = retrieve_documents("credit risk", {"Risk"})
    document_ids = {document["id"] for document in results}

    assert "RISK-001" in document_ids


def test_risk_user_cannot_access_finance_document():
    results = retrieve_documents("quarterly finance expenses", {"Risk"})
    document_ids = {document["id"] for document in results}

    assert "FIN-001" not in document_ids


def test_risk_user_cannot_access_security_only_document():
    results = retrieve_documents("security incident procedure", {"Risk"})
    document_ids = {document["id"] for document in results}

    assert "SEC-001" not in document_ids


def test_shared_document_is_available_to_risk_group():
    results = retrieve_documents("least privilege", {"Risk"})
    document_ids = {document["id"] for document in results}

    assert "SHARED-001" in document_ids


def test_empty_query_is_rejected():
    with pytest.raises(ValueError):
        retrieve_documents("   ", {"Risk"})


def test_groups_must_be_a_set():
    with pytest.raises(TypeError):
        retrieve_documents("credit risk", ["Risk"])


def test_zero_result_limit_is_rejected():
    with pytest.raises(ValueError):
        retrieve_documents("credit risk", {"Risk"}, limit=0)
