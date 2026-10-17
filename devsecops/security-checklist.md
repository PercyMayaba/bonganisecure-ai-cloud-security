# BonganiSecure AI: DevSecOps Security Checklist

## Project Scope

This project demonstrates foundational cloud security, identity and access management, document-level authorisation, and automated Python security checks.

The application currently uses synthetic training documents and local Python retrieval. Azure resources are documented separately. The local prototype is not yet integrated with Microsoft Entra ID or Azure AI Search.

## Identity and Access Management

- [x] Reviewed least-privilege access concepts.
- [x] Created a user-assigned managed identity named `mi-bongani-day1`.
- [x] Assigned the Reader role at resource-group scope.
- [ ] Verify workload identity authentication in an application.
- [ ] Integrate Microsoft Entra ID authentication into the application.
- [ ] Validate real identity group membership before authorising document access.

## Network Security

- [x] Created the lab virtual network `vnet-bongani-day2`.
- [x] Created the `subnet-workload` subnet.
- [x] Created and associated the `nsg-bongani-day2` network security group.
- [x] Configured an inbound SSH deny rule at priority 200.
- [ ] Review effective network security rules and document the results.
- [ ] Add further network controls only where required by the lab design.

## Application Security

- [x] Use synthetic documents rather than real customer or confidential data.
- [x] Filter documents by authorised groups before keyword matching.
- [x] Validate empty queries, group input types, and result limits.
- [x] Add automated tests for access-control behaviour.
- [ ] Connect authorisation groups to a trusted identity provider.
- [ ] Add production-grade authentication, logging, and error handling before deployment.
- [ ] Review retrieval behaviour for data leakage and prompt-injection risks before adding an LLM.

## Secrets and Configuration

- [x] Exclude `.env` files, private keys, and local virtual environments using `.gitignore`.
- [ ] Verify that no secrets, credentials, tenant identifiers, or sensitive principal identifiers are committed.
- [ ] Use managed identity or an approved secrets manager for any future Azure integration.
- [ ] Never place credentials or access tokens in source code, logs, or screenshots.

## Automated Security Checks

- [x] Added automated tests using pytest.
- [x] Ran the current test suite successfully: 7 tests passed.
- [x] Ran Bandit against the `app` directory: no findings reported.
- [x] Added a GitHub Actions workflow for tests and Bandit.
- [ ] Confirm the workflow passes on GitHub after the code is pushed.
- [ ] Review future dependency vulnerabilities and update dependencies as needed.

## Azure Security Posture

- [x] Registered the Microsoft.Security resource provider.
- [x] Reviewed Defender for Cloud settings and available security assessments.
- [x] Kept Defender plan settings at their existing free tiers during the lab.
- [ ] Review and document outstanding security recommendations.
- [ ] Verify findings in the Azure portal before describing them as resolved.

## Evidence and Reporting

- [ ] Record dates, commands, and screenshots for significant lab results.
- [ ] Keep findings separate from planned work.
- [ ] Remove sensitive identifiers from screenshots and public reports.
- [ ] Recheck the repository before every public release.

## Status

This checklist is a working security baseline, not a certification of production readiness. Items marked incomplete require additional implementation or verification.
