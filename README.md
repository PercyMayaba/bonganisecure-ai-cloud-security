# bonganisecure-ai-cloud-security
Secure AI RAG application and cloud security engineering portfolio using Python, Microsoft Azure and GitHub Actions.

About This Portfolio

Welcome to my Azure Cloud and AI Security Engineering portfolio. This repository documents my practical learning journey in cloud security, identity and access management, network security, security monitoring, incident investigation, and AI application security.

My objective is to combine my financial services background with my knowledge of machine learning, deep learning, retrieval-augmented generation (RAG), and agentic AI to develop practical security engineering skills.

The projects in this repository focus on security fundamentals, least privilege, evidence-based investigation, secure AI application design, and clear technical documentation.

Technical Focus Areas

- Azure Identity and Access Management: Role-Based Access Control (RBAC), managed identities, role assignment review, and least privilege.
- Azure Network Security: Virtual networks, subnet segmentation, Network Security Groups, traffic filtering, and security rule prioritisation.
- Cloud Security Posture: Defender for Cloud configuration review, security recommendations, and posture assessment.
- Security Monitoring and Incident Investigation: Azure Activity Log analysis, Kusto Query Language (KQL), event correlation, incident timelines, and response recommendations.
- AI Application Security: RAG document retrieval, access-control design, input validation, and automated security testing.
- DevSecOps: GitHub Actions, Python unit testing, Bandit security scanning, and security-focused development practices.

Featured Projects

1. Azure Identity and Access Management

Focus: RBAC scope, managed identities, and least privilege.

This lab explores Azure role assignments and the security implications of subscription-level permissions. It includes the creation of a user-assigned managed identity and a Reader role assignment at resource-group scope.

Security lessons:

- Understand the relationship between roles and scope.
- Review privileged access assignments.
- Use managed identities for supported Azure workloads.
- Apply permissions at the narrowest practical scope.

2. Azure Network Security and Traffic Filtering

Focus: Virtual networks, subnets, Network Security Groups, and inbound traffic control.

This lab documents the creation of a virtual network, workload subnet, NSG, and a custom inbound SSH-deny rule.

Security lessons:

- Understand basic network segmentation.
- Apply traffic-filtering rules at the appropriate network boundary.
- Review rule priority and NSG association.
- Distinguish configuration verification from live connectivity testing.

3. Azure Security Posture Review

Focus: Defender for Cloud and cloud security configuration.

This exercise explores security posture settings, provider registration, and the distinction between available foundational capabilities and paid security plans.

The lab documentation records configuration observations and limitations without claiming that paid plans were enabled or that a live security incident was detected.

4. Azure Security Incident Investigation

Focus: Synthetic audit events, KQL, incident timelines, and response planning.

This project uses a fictional Azure Activity Log-style dataset to investigate a sequence of role assignment changes, an NSG rule modification, failed and successful virtual machine deletion attempts, and additional administrative activity.

The project includes:

- Synthetic investigation evidence.
- KQL examples for administrative changes, failed operations, and resource deletion.
- A chronological incident timeline.
- A provisional severity and confidence assessment.
- Investigation and remediation recommendations.
- Explicit limitations covering untested queries and the absence of live incident data.

The exercise demonstrates an evidence-based investigation workflow. It does not claim that a real compromise occurred or that the queries have been validated against a live Log Analytics workspace.

5. Secure AI Knowledge Assistant

Focus: RAG security, document-level access control, and automated testing.

This project explores a local Python document-retrieval implementation that filters documents according to authorised groups before returning matching content.

The repository includes synthetic documents, automated tests, and security scanning through GitHub Actions.

The current implementation is a learning prototype. Production deployment would require trusted identity integration, server-side authorisation enforcement, and an appropriately configured retrieval service such as Azure AI Search. The local prototype should not be represented as a fully deployed Microsoft Entra ID-integrated application.

Tools and Technologies

- Microsoft Azure Portal
- Azure Cloud Shell and Azure CLI
- Azure Role-Based Access Control
- Azure Virtual Networks and Network Security Groups
- Microsoft Defender for Cloud
- Kusto Query Language
- Python
- Pytest
- Bandit
- Git and GitHub
- GitHub Actions
- Retrieval-Augmented Generation concepts
- Machine learning and deep learning concepts

DevSecOps and Testing

The repository includes an automated GitHub Actions workflow that runs Python tests and a Bandit security scan.

The RAG prototype has previously passed seven automated tests, and the Bandit scan reported no findings in the scanned application code at that time.

These results apply to the tested code and scan scope. They do not constitute a comprehensive security audit or prove that the complete portfolio is production-ready.

Security Engineering Principles

My approach to these projects is guided by the following principles:

1. Least privilege and appropriate access scope.
2. Defence in depth across identity, network, and application layers.
3. Evidence-based investigation and transparent reporting.
4. Automated testing and security checks during development.
5. Protection of credentials and sensitive information.
6. Clear separation between simulated exercises, configuration checks, and live validation.
7. Cost-conscious cloud experimentation.

Professional Development

I am building practical skills toward Azure Cloud Security Engineering and AI Security Engineering roles, drawing on my financial services experience and prior learning in RAG, agentic AI, machine learning, and deep learning.

I am particularly interested in the intersection of cloud security, AI application security, identity governance, and financial services risk.

Disclaimer

This repository is a personal learning portfolio. Some exercises use synthetic data, and some configurations have been verified without a deployed workload. KQL examples are not production detections unless explicitly validated against an appropriate log source.

No project should be interpreted as a formal penetration test, independent security audit, or production deployment unless that work is explicitly documented and supported by evidence.