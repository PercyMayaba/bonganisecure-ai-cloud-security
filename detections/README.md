# BonganiSecure AI: Security Detection Lab

## Objective

This directory is intended to demonstrate foundational security monitoring and investigation skills relevant to Microsoft Azure and Microsoft Sentinel.

The goal is to develop detections, explain the security reasoning behind them, and document how an analyst would validate and investigate potential incidents.

## Current Scope

The repository includes `detections.kql` as a working area for Kusto Query Language (KQL) detection examples.

KQL is used to query supported Microsoft security and monitoring data sources. The tables and fields available depend on the connected service, data connectors, and ingestion configuration.

## Planned Detection Use Cases

1. **Suspicious authentication activity:** Investigate repeated failed sign-ins and unusual authentication patterns using the appropriate identity log tables.
2. **Privilege changes:** Review role assignment or directory audit events for unexpected permission changes.
3. **Network security changes:** Investigate changes to network security groups and inbound access rules.
4. **Security configuration changes:** Review Azure Activity Log events for relevant resource configuration changes.
5. **Investigation and triage:** Establish a timeline, identify affected resources, and document evidence and follow-up actions.

These are planned use cases. They should only be described as implemented detections after the relevant queries have been written and tested against suitable data.

## Validation Requirements

Before using a query operationally:

- Confirm that the target table exists in the connected environment.
- Validate field names against the actual table schema.
- Test the query against representative data.
- Check time ranges and timezone assumptions.
- Investigate false positives and expected administrative activity.
- Avoid collecting or publishing unnecessary personal or sensitive information.
- Document the query's purpose, expected results, limitations, and investigation steps.

## Azure Activity Log Context

The lab previously verified a successful `Microsoft.Security` resource-provider registration event in Azure Activity Log.

That event confirms provider registration. It does not establish that paid Defender for Cloud plans were enabled or that a security incident occurred.

## Current Limitations

- No live Microsoft Sentinel data source has been confirmed for this repository.
- Queries must be validated against the actual schema before operational use.
- Detection rules and alerting are not considered production-ready.
- No real customer or production security data should be committed to this repository.

## Next Steps

1. Review the current contents of `detections.kql`.
2. Add focused queries using verified table schemas.
3. Test the queries against authorised lab data.
4. Record sample results and investigation guidance without exposing sensitive information.
5. Update this README as each detection is implemented and verified.
