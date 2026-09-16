---
title: "Week 7 Worklog"
date: 2026-09-14
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Week 7 Objectives:
* Decouple the infrastructure planning stage (Terraform Plan) from execution (Terraform Apply).
* Integrate a Manual Approval Gate with real-time email notification via Amazon SNS.
* Execute automated deployment using Least Privilege IAM roles and conduct automated Post-Deploy Smoke Tests.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Configure CodeBuild stage to execute `terraform plan` and output artifact `tfplan`.<br>- Configure Amazon SNS topic to dispatch email alerts with approval details to administrators. | 14/09/2026 | 14/09/2026 | Internship Project |
| 2 | - Configure Manual Approval action in CodePipeline between Plan and Deploy stages.<br>- Test administrator review, approval, and rejection mechanisms. | 15/09/2026 | 15/09/2026 | Internship Project |
| 3 | - Construct Terraform Apply build project with restricted TerraformDeployRole (Least Privilege).<br>- Enforce automated execution of `terraform apply tfplan` upon manual sign-off. | 16/09/2026 | 16/09/2026 | Internship Project |
| 4 | - Develop automated Post-Deploy Smoke Test script to validate EC2 Web Endpoint.<br>- Verify HTTP response status code returns 200 OK and validate content delivery. | 17/09/2026 | 17/09/2026 | Internship Project |
| 5 | - Execute end-to-end pipeline run from source commit to completed smoke test verification.<br>- Validate continuous, auditable, zero-touch deployment workflow across all stages. | 18/09/2026 | 18/09/2026 | Internship Project |

### Week 7 Achievements:
* Perfected secure human-in-the-loop governance: Infrastructure changes require explicit engineer approval.
* Achieved zero-touch, auditable infrastructure deployment powered by least-privilege service roles.
* Automated smoke tests instantly verify application health upon successful pipeline execution.
* Seamless continuous delivery cycle operational from GitHub repository to live AWS cloud environment.
