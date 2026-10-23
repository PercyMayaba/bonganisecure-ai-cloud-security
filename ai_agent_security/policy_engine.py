
"""Simulation-only policy enforcement for AI agents."""

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
    "AGENT-REPORT-003
