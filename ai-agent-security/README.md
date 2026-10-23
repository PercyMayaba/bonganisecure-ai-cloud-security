# BonganiSecure AI Agent Identity and Workload Security Lab

## Project Overview

This project explores the security of enterprise AI workloads and Microsoft Entra Agent ID. It focuses on agent identity, least-privilege access, responsible ownership, secure tool execution, data access boundaries, auditability, and incident response.

The scenario models a fictional financial services organisation using an AI knowledge assistant to retrieve approved risk and finance documents.

The project begins with a local security design and synthetic evidence. Live Microsoft Entra Agent ID provisioning, authentication, and Azure service integration are separate future activities and are not claimed as completed.

## Scenario

A financial services organisation introduces an AI assistant that can retrieve internal knowledge and invoke approved business tools.

The organisation needs to ensure that:

- Every agent has a clearly defined purpose and accountable owner.
- Agent permissions are limited to the resources required for its task.
- Access to financial and risk information is enforced by trusted application-side controls.
- Tool calls are explicitly authorised and validated.
- Credentials and tokens are protected.
- Agent activity can be investigated using reliable audit evidence.
- An agent can be disabled or have access revoked when a security concern is confirmed.

## Proposed Architecture

1. **AI workload:** A local prototype representing a financial services knowledge assistant.
2. **Identity control plane:** Microsoft Entra Agent ID concepts, including blueprints, agent identities, sponsorship, and permission governance.
3. **Data boundary:** Synthetic finance, risk, and security documents with group-based access rules.
4. **Tool boundary:** A simulated tool gateway that rejects unapproved actions.
5. **Monitoring:** Synthetic agent activity records and investigation queries.
6. **Response:** A documented process for reviewing permissions, preserving evidence, and disabling access when appropriate.

## Security Controls

- Least-privilege authorisation
- Unique and accountable agent identities where supported
- Trusted identity and permission validation
- Server-side document access enforcement
- Explicit allowlisting of tools and actions
- Input validation and safe error handling
- Secret and token protection
- Audit logging and event correlation
- Lifecycle reviews and access revocation
- Separation of synthetic tests from live security validation

## Planned Lab Deliverables

- AI workload threat model
- Agent identity and permissions matrix
- Synthetic agent activity dataset
- Tool access-control test cases
- KQL investigation examples where a compatible log source exists
- Incident response playbook
- Microsoft Entra Agent ID integration plan

## Current Status

This repository documents a learning project and security design. Synthetic evidence and local tests are not equivalent to live Entra Agent ID authentication or a deployed Azure AI workload.

Each implementation stage will be labelled according to whether it is designed, simulated, locally tested, or validated in a live environment.

## Reference Documentation

- Microsoft Entra Agent ID: https://learn.microsoft.com/en-us/entra/agent-id/
- Agent identity concepts: https://learn.microsoft.com/en-us/entra/agent-id/agent-identities
- Agent ID best practices: https://learn.microsoft.com/en-us/entra/agent-id/best-practices-agent-id

