# Multi-Agent AI Workload Threat Model

**Status:** Design exercise; simulation only  
**Cloud deployment:** None  
**Microsoft Entra Agent ID provisioning:** Not performed

## Assets

- Synthetic finance and risk documents
- Agent identity and permission records
- Inter-agent messages and analysis results
- Report drafts
- Audit events and investigation evidence

## Trust boundaries

1. The document store is a protected data boundary.
2. The research agent can retrieve only documents permitted by the authorisation layer.
3. The risk analysis agent receives only approved research output.
4. The reporting agent produces drafts but cannot perform external actions.
5. A policy enforcement layer checks every tool request before execution.
6. Human operators retain authority over sensitive or irreversible actions.

## Threat scenarios

| Threat | Potential impact | Proposed control |
|---|---|---|
| Research agent retrieves a restricted document | Unauthorised disclosure | Server-side document-level authorisation |
| Agent impersonation or identity confusion | Actions attributed to the wrong agent | Distinct identities and trusted identity validation |
| Prompt injection in a document | Unintended tool requests | Treat retrieved content as untrusted input; enforce tool policies independently |
| Risk agent receives unauthorised context | Incorrect or sensitive analysis | Validate the context passed between agents |
| Reporting agent attempts an external action | Unapproved disclosure | Allowlisted tools and deny-by-default authorisation |
| Agent permissions become excessive | Wider potential compromise | Least privilege and periodic access reviews |
| Audit evidence is incomplete | Delayed or incorrect investigation | Record actor, action, target, result, timestamp, and correlation identifier |

## Security assumptions

The simulated identity inventory does not authenticate agents. A production implementation must derive the acting identity from a trusted authentication mechanism and must not rely on an agent-provided name or identifier.

The application must enforce permissions independently of the model's instructions. A model saying that an action is authorised is not proof of authorisation.

## Incident response

If unauthorised agent activity is confirmed in a real deployment:

1. Preserve relevant audit and application logs.
2. Identify the affected agent identity and its parent blueprint where applicable.
3. Review recent permissions, credentials, and tool activity.
4. Revoke or disable access using approved administrative procedures.
5. Assess data exposure and downstream actions.
6. Restore the intended permissions and validate controls before resuming operation.
7. Document evidence, impact, and corrective actions.

## Validation boundary

This threat model is a proposed security design. The controls have not been validated against a live Entra Agent ID environment. Subsequent simulation tests will demonstrate application-level policy decisions only.
