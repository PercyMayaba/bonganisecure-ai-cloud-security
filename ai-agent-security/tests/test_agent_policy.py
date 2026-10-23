
"""Security tests for the simulated multi-agent policy engine."""

import pytest

from ai_agent_security.policy_engine import authorise_action


@pytest.mark.parametrize(
    ("agent_id", "action"),
    [
        ("AGENT-RESEARCH-001", "read_risk_documents"),
        ("AGENT-RESEARCH-001", "read_shared_documents"),
        ("AGENT-RISK-002", "analyse_approved_context"),
        ("AGENT-REPORT-003", "create_report_draft"),
    ],
)
def test_permitted_actions_are_allowed(agent_id, action):
    decision = authorise_action(agent_id, action)

    assert decision.allowed is True


@pytest.mark.parametrize(
    ("agent_id", "action"),
    [
        ("AGENT-RESEARCH-001", "delete_resources"),
        ("AGENT-RESEARCH-001", "modify_role_assignments"),
        ("AGENT-RISK-002", "read_risk_documents"),
        ("AGENT-RISK-002", "approve_own_actions"),
        ("AGENT-REPORT-003", "send_external_messages"),
        ("AGENT-REPORT-003", "modify_permissions"),
    ],
)
def test_unpermitted_actions_are_denied(agent_id, action):
    decision = authorise_action(agent_id, action)

    assert decision.allowed is False


def test_unknown_agent_is_denied():
    decision = authorise_action(
        "AGENT-UNKNOWN-999",
        "read_shared_documents",
    )

    assert decision.allowed is False
    assert "Unknown agent" in decision.reason


@pytest.mark.parametrize(
    ("agent_id", "action"),
    [
        ("", "read_shared_documents"),
        ("AGENT-RESEARCH-001", ""),
    ],
)
def test_empty_values_are_denied(agent_id, action):
    decision = authorise_action(agent_id, action)

    assert decision.allowed is False


def test_non_string_values_are_denied():
    decision = authorise_action(None, "read_shared_documents")

    assert decision.allowed is False
