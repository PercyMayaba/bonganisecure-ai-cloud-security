
"""Security tests for simulated multi-agent message validation."""

import pytest

from ai_agent_security.message_validation import validate_agent_message


@pytest.fixture
def valid_message():
    return {
        "message_id": "MSG-001",
        "sender_agent_id": "AGENT-RESEARCH-001",
        "recipient_agent_id": "AGENT-RISK-002",
        "action": "analyse_approved_context",
        "payload": {"context": "Synthetic risk summary"},
    }


def test_valid_message_structure_is_accepted(valid_message):
    result = validate_agent_message(valid_message)

    assert result.valid is True


def test_unknown_sender_is_rejected(valid_message):
    valid_message["sender_agent_id"] = "AGENT-UNKNOWN-999"

    result = validate_agent_message(valid_message)

    assert result.valid is False
    assert "Unknown sender" in result.reason


def test_unknown_recipient_is_rejected(valid_message):
    valid_message["recipient_agent_id"] = "AGENT-UNKNOWN-999"

    result = validate_agent_message(valid_message)

    assert result.valid is False
    assert "Unknown recipient" in result.reason


def test_missing_required_field_is_rejected(valid_message):
    del valid_message["action"]

    result = validate_agent_message(valid_message)

    assert result.valid is False
    assert "Missing required fields" in result.reason


def test_empty_sender_id_is_rejected(valid_message):
    valid_message["sender_agent_id"] = " "

    result = validate_agent_message(valid_message)

    assert result.valid is False


def test_non_dictionary_message_is_rejected():
    result = validate_agent_message("not a message")

    assert result.valid is False


def test_non_dictionary_payload_is_rejected(valid_message):
    valid_message["payload"] = "unstructured payload"

    result = validate_agent_message(valid_message)

    assert result.valid is False
    assert "Payload must be a dictionary" in result.reason


def test_claimed_identity_is_not_treated_as_authenticated(valid_message):
    result = validate_agent_message(valid_message)

    assert result.valid is True
    assert "not authenticated" in result.reason
