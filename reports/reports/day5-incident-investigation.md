Day 5: Azure Security Incident Investigation

Executive Summary

This project demonstrates a simulated investigation of suspicious administrative activity in a Microsoft Azure environment. The exercise uses synthetic Azure Activity Log-style events to practise event correlation, KQL investigation, timeline reconstruction, impact assessment, and incident response planning.

The scenario contains role assignment changes, an NSG security rule modification, a failed virtual machine deletion followed by a successful deletion, a subsequent role assignment removal, and additional configuration activity.

The event sequence warrants investigation because it combines identity, network, and resource-management changes. However, the evidence is synthetic and does not prove unauthorised access or account compromise. No live Azure incident was investigated, and no production resources were modified.

1. Scope and Methodology

The investigation used a fictional dataset created for portfolio training. Events were reviewed chronologically and grouped into identity, network, and resource-management activities.

KQL examples were prepared for use with Azure Activity Log data ingested into the Azure Monitor Logs "AzureActivity" table. The queries have not been executed against a live workspace and must be validated against the actual schema and status values before operational use.

2. Key Observations

Identity activity

Two successful role assignment creation events occurred at 08:00 and 08:04 UTC. A subsequent role assignment removal occurred at 08:22 UTC.

These changes could indicate legitimate administrative work or an attempt to change access during an incident. The specific role definitions and target identities are not included in the synthetic dataset, so the privilege level and effective access cannot be confirmed.

Network activity

An NSG security rule modification occurred at 08:10 UTC. The dataset does not contain the before-and-after rule configuration, source ranges, destination ports, or access direction.

The potential impact on network exposure is therefore undetermined. A real investigation would compare the rule configuration before and after the change and assess whether it introduced unintended access.

Resource deletion

A virtual machine deletion attempt failed at 08:14 UTC and a subsequent attempt succeeded at 08:18 UTC.

This sequence establishes the simulated ordering of the events. It does not establish why the first attempt failed, whether data was lost, or whether the deletion was authorised. Recovery options and related disk, backup, and activity records would need to be reviewed.

Additional activity

A service account role assignment attempt failed at 08:30 UTC. A storage account configuration update occurred at 08:35 UTC.

The available data is insufficient to link these events to the earlier actions or establish a common cause. The accounts, source addresses, and correlation identifiers should be examined alongside independent identity and operational evidence.

3. Incident Timeline

All times are UTC on 14 October 2026.

Time| Event| Assessment
08:00| Role assignment created| Review target identity and role
08:04| Second role assignment created| Determine whether the change was authorised
08:10| NSG security rule modified| Establish whether exposure increased
08:14| VM deletion attempt failed| Determine the failure reason
08:18| VM deletion succeeded| Assess workload and recovery impact
08:22| Role assignment removed| Determine which access was removed
08:30| Service account role assignment failed| Review identity and authorisation context
08:35| Storage configuration updated| Compare configuration with the approved baseline

4. Severity and Confidence

Provisional severity: High investigation priority, pending validation.

The combination of identity changes, network configuration changes, and a successful resource deletion could have significant consequences if unauthorised. However, the scenario does not establish actual compromise, data exposure, business impact, or malicious intent.

Confidence: High that the listed events exist within the synthetic dataset; low regarding attribution, intent, and actual impact.

This is a triage assessment for a fictional exercise, not a formal severity classification of a real incident.

5. Recommended Investigation Steps

1. Validate the caller identities and correlate their activity with Entra ID sign-in logs.
2. Retrieve the role definitions and target principals associated with each role assignment change.
3. Compare the NSG rule before and after the modification, including source, destination, protocol, port, and priority.
4. Determine whether the virtual machine deletion was approved and assess backup, disk, and recovery implications.
5. Investigate the failed service account operation and storage account change independently before linking them to the same incident.
6. Preserve relevant logs and timestamps, document evidence provenance, and maintain an investigation record.
7. If a real unauthorised change is confirmed, follow the organisation's incident response process, contain the affected identity or resource where appropriate, and coordinate recovery with the system owner.

6. Detection Engineering

The accompanying "detections/day5_incident_investigation.kql" file provides query examples for administrative activity, role assignment changes, NSG rule changes, failed operations, and resource deletion.

These queries are starting points, not production-ready detections. They require schema validation, testing against representative logs, tuning to reduce false positives, and integration with the organisation's monitoring and alerting processes.

7. Limitations

- All events are synthetic.
- No live Azure Activity Log or Entra ID data was queried.
- No KQL query execution or alert generation was demonstrated.
- Role definitions and NSG before-and-after configurations are not provided.
- Attribution, compromise, data exposure, and business impact remain unconfirmed.
- The scenario does not prove that the separate activities share a common cause.

8. Skills Demonstrated

- Azure administrative audit-log analysis
- KQL query design
- Identity and access change investigation
- Network security configuration review
- Incident timeline reconstruction
- Evidence-based severity assessment
- Incident response recommendations
- Technical reporting and documentation

Conclusion

This lab demonstrates a structured approach to investigating potentially suspicious Azure administrative activity. The main lesson is to correlate identity, network, and resource events while distinguishing observed evidence from assumptions.

A credible security investigation does not treat every unusual event as proof of compromise. It establishes what the evidence shows, identifies what remains unknown, and defines the next steps needed to validate the hypothesis.

Disclaimer: This is a synthetic learning exercise, not a real incident investigation, penetration test, or production security assessment.