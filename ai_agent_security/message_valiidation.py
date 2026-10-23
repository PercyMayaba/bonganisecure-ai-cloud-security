
"""Validate message structure in a simulated multi-agent workflow.

This validates message fields and claimed agent IDs only.
It does not authenticate identities or verify trusted tokens.
"""

from dataclasses import dataclass


KNOWN_AGENTS = {
    "AGENT-RESEARCH-001",
    "AGENT-RISK-002",
    "AGENT-REPORT-003",
}

REQUIRED_FIELDS = {
    "message_id",
    "sender_agent_id",
    "recipient_agent_id",
    "action",
    "payload",
}


@dataclass(frozen=True)
class MessageValidation:
    valid: bool
    reason: str


def validate_agent_message(message: object) -> MessageValidation:
    """Reject malformed messages and unknown agent identifiers."""

    if not isinstance(message, dict):
        return MessageValidation(
            False, "Message must be a dictionary."
        )

    missing_fields = REQUIRED_FIELDS - message.keys()
    if missing_fields:
        return MessageValidation(
            False,
            f"Missing required fields: {', '.join(sorted(missing_fields))}.",
        )

    for field in (
        "message_id",
        "sender_agent_id",
        "recipient_agent_id",
        "action",
    ):
        value = message[field]
        if not isinstance(value, str) or not value.strip():
            return MessageValidation(
                False,
                f"Field '{field}' must be a non-empty string.",
            )

    if message["sender_agent_id"] not in KNOWN_AGENTS:
        return MessageValidation(
            False, "Unknown sender agent. Message rejected."
        )

    if message["recipient_agent_id"] not in KNOWN_AGENTS:
        return MessageValidation(
            False, "Unknown recipient agent. Message rejected."
        )

    if not isinstance(message["payload"], dict):
        return MessageValidation(
            False, "Payload must be a dictionary."
        )

    return MessageValidation(
        True,
        "Message structure is valid; sender identity is not authenticated.",
    )
