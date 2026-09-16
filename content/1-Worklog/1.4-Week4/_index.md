---
title: "Week 4 Worklog"
date: 2026-08-24
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Week 4 Objectives:
* Learn AWS monitoring, logging and alerting with Amazon CloudWatch (Metrics, Logs, Alarms).
* Learn governance, compliance, and auditing with AWS CloudTrail.
* Learn event-driven automation with Amazon EventBridge and notifications via Amazon SNS.
* Manage centralized configurations and encrypted secrets using AWS Systems Manager (SSM) Parameter Store.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Learn Amazon CloudWatch Metrics.<br>- Monitor EC2 performance metrics (CPU utilization, NetworkIn/Out).<br>- Create CloudWatch Alarm triggering when CPU exceeds 80%. | 24/08/2026 | 24/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 2 | - Learn Amazon CloudWatch Logs.<br>- Install and configure Unified CloudWatch Agent on EC2 instance.<br>- Stream system logs (`/var/log/messages`) into CloudWatch Log Groups. | 25/08/2026 | 25/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Learn AWS CloudTrail auditing.<br>- Create a multi-region Trail logging management events into S3.<br>- Inspect CloudTrail Event History to audit API activity and access sources. | 26/08/2026 | 26/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Learn Amazon EventBridge and Amazon Simple Notification Service (SNS).<br>- Create an SNS Topic and subscribe via email endpoint.<br>- Create EventBridge Rule capturing EC2 state changes and dispatching alerts to SNS. | 27/08/2026 | 27/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Learn AWS Systems Manager (SSM) Parameter Store.<br>- Store plaintext configuration and encrypted credentials with SecureString.<br>- Securely retrieve stored parameters from EC2 using AWS CLI and IAM Role. | 28/08/2026 | 28/08/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 4 Achievements:
* Mastered Amazon CloudWatch observability ecosystem:
  * Monitored system health with fine-grained metrics and automated threshold alarms.
  * Centralized system and web application logs into CloudWatch Log Groups.
* Acquired cloud auditability skills using AWS CloudTrail:
  * Traced user identities, API request timestamps, and source IP addresses.
* Built real-time event-driven alerting:
  * Routed operational state change events through EventBridge to SNS email subscribers.
* Managed secrets securely with SSM Parameter Store:
  * Encrypted sensitive database credentials using AWS KMS.
  * Completely separated application logic from configuration secrets.
