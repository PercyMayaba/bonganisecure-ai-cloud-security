
"""Simulation-only policy enforcement for a multi-agent AI workflow."""

from dataclasses import dataclass


@dataclass(frozen=True)
class PolicyDecision:
    allowed: bool
    agent_id: str
    action: str
    reason: str


AGENT_POLICIES = {
    "AGENT-RESEARCH-001": {
        "read_risk_documents",
        "read_shared_documents",
    },
    "AGENT-RISK-002": {
        "analyse_approved_context",
    },
    "AGENT-REPORT-003": {
        "create_report_draft",
    },
}


def authorise_action(agent_id: str, action: str) -> PolicyDecision:
    """Allow only actions explicitly assigned to a known agent."""

    if not isinstance(agent_id, str) or not isinstance(action, str):
        return PolicyDecision(
            False, "UNKNOWN", "UNKNOWN",
            "Invalid identity or action format.",
        )

    if not agent_id.strip() or not action.strip():
        return PolicyDecision(
            False, agent_id or "UNKNOWN", action or "UNKNOWN",
            "Identity and action must not be empty.",
        )

    permitted_actions = AGENT_POLICIES.get(agent_id)

    if permitted_actions is None:
        return PolicyDecision(
            False, agent_id, action,
            "Unknown agent identity. Access denied by default.",
        )

    if action not in permitted_actions:
        return PolicyDecision(
            False, agent_id, action,
            "Action is not explicitly permitted for this agent.",
        )

    return PolicyDecision(
        True, agent_id, action,
        "Action is explicitly permitted by the simulation policy.",
    )

