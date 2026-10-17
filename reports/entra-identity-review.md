# Microsoft Entra Identity Review

## Project

BonganiSecure AI Cloud Security Portfolio

## Purpose

This report documents the identity and access management controls reviewed during the Azure security lab. It distinguishes verified lab configuration from work that remains outstanding.

## 1. Managed Identity

**Resource:** `mi-bongani-day1`

A user-assigned managed identity was created as part of the Day 1 Azure security exercise.

The identity provides a foundation for exploring passwordless authentication between Azure workloads and supported Azure services. Managed identities can reduce the need to store application credentials in source code or configuration files.

**Verified lab result:** The managed identity was created, and the Reader role was assigned at resource-group scope.

**Remaining work:** Application authentication using this identity has not yet been verified. The identity should not be described as integrated with the Python application until that integration is implemented and tested.

## 2. Role-Based Access Control

The Reader role was assigned at resource-group scope for the lab identity.

Reader is a read-only Azure resource management role. It does not, by itself, grant access to every data plane or application resource.

The principle of least privilege requires reviewing the permissions needed for each workload and avoiding broader access than necessary.

**Remaining work:**
- Verify the current role assignment in Azure.
- Confirm that the assigned scope matches the intended workload.
- Review whether the identity requires any additional permissions for a future implementation.
- Avoid granting additional roles without a documented requirement.

## 3. Secure AI Document Access

The local Python prototype uses synthetic documents with an `allowed_groups` attribute. Its retrieval function filters documents against a supplied set of trusted groups before matching keywords.

This is a local authorisation demonstration only. The group set is supplied by the caller and is not yet obtained from Microsoft Entra ID.

**Security limitation:** In a deployed application, the server must validate the user's identity and derive authorised group membership from a trusted source. It must never trust arbitrary group names supplied by a client.

## 4. Findings and Next Steps

| Area | Current status |
|---|---|
| User-assigned managed identity created | Verified in the lab |
| Reader role at resource-group scope | Previously verified in the lab |
| Python document retrieval prototype | Implemented locally |
| Automated authorisation tests | Seven tests passed locally |
| Entra ID authentication in Python app | Not implemented |
| Live Entra group membership validation | Not implemented |
| Azure AI Search integration | Not implemented |

## 5. Conclusion

The lab establishes a foundation for demonstrating least privilege, managed identities, and document-level authorisation concepts.

It is not yet a production Entra-integrated RAG solution. The next phase is to implement and test trusted authentication and group-based authorisation, then document the results using reproducible evidence.

No customer data or production credentials should be used in this portfolio.
