---
title: "Week 8 Worklog"
date: 2026-09-15
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Week 8 Objectives:
* Establish real-time monitoring and alerting via CloudWatch, EventBridge, and SNS.
* Conduct comprehensive validation across 6 realistic DevSecOps test scenarios.
* Perform cloud resource teardown, cost audits, and final internship report sign-off.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Configure Amazon EventBridge rules to capture CodePipeline status changes (FAILED / SUCCEEDED).<br>- Configure SNS target to send immediate failure alert emails to engineers. | 21/09/2026 | 21/09/2026 | Internship Project |
| 2 | - Configure CloudWatch Alarms for EC2 workload monitoring and audit API actions via CloudTrail.<br>- Set up AWS Budgets cost alerts ensuring zero unexpected billing. | 22/09/2026 | 22/09/2026 | Internship Project |
| 3 | - Execute first 3 DevSecOps scenarios:<br>&emsp;+ Scenario 1: Golden Path deployment success.<br>&emsp;+ Scenario 2: Commit secret detection and pipeline abort via Gitleaks.<br>&emsp;+ Scenario 3: Python SAST security flaw detection and abort via Bandit.<br>- Capture console screenshots and detailed build logs. | 23/09/2026 | 23/09/2026 | Internship Project |
| 4 | - Execute remaining 3 DevSecOps scenarios:<br>&emsp;+ Scenario 4: Checkov open SSH (0.0.0.0/0:22) security group rule interception.<br>&emsp;+ Scenario 5: Manual Approval rejection workflow validation.<br>&emsp;+ Scenario 6: Post-deploy smoke test health verification.<br>- Compile security scan reports and evaluate overall DevSecOps maturity metrics. | 24/09/2026 | 24/09/2026 | Internship Project |
| 5 | - Teardown 100% of provisioned cloud infrastructure using `terraform destroy`.<br>- Audit AWS Cost Explorer ensuring $0 unplanned charges.<br>- Finalize graduation internship documentation, presentation slides, and complete defense with mentor. | 25/09/2026 | 27/09/2026 | Internship Report |

### Week 8 Achievements:
* Completed automated alert ecosystem ensuring engineers are immediately notified of deployment failures.
* Validated robustness of the DevSecOps Pipeline through 6 real-world incident simulations.
* Safely torn down 100% of test resources, ensuring zero unintended cloud expenditure.
* Successfully concluded the 8-week internship program with comprehensive technical documentation and a portfolio website.
