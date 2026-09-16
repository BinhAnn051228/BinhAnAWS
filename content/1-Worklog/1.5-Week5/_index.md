---
title: "Week 5 Worklog"
date: 2026-08-31
weight: 5
chapter: false
pre: " <b> 1.5. </b> "
---

### Week 5 Objectives:
* Prepare for the graduation internship project: **AWS DevSecOps Pipeline**.
* Research technologies, analyze security requirements, and design the initial system architecture.
* Initialize GitHub project repository and author Terraform IaC code for Bootstrap and target environments.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Research internship project ideas and analyze DevSecOps system requirements.<br>- Evaluate security risks in cloud software supply chains and IaC deployments. | 31/08/2026 | 31/08/2026 | Internship Project |
| 2 | - Select the official internship project topic: **AWS DevSecOps Pipeline with Terraform & Shift-Left Security**.<br>- Identify technologies: AWS CodePipeline, CodeBuild, Terraform, Gitleaks, Bandit, Trivy, Checkov. | 01/09/2026 | 01/09/2026 | Internship Project |
| 3 | - Design end-to-end application and deployment architecture.<br>- Create architecture diagrams covering Bootstrap, CI/CD stages, security gates, and target environment. | 02/09/2026 | 02/09/2026 | Internship Project |
| 4 | - Set up local development environment: Terraform CLI, AWS CLI v2, Git, VS Code.<br>- Initialize GitHub project repository with modular directory organization. | 03/09/2026 | 03/09/2026 | Internship Project |
| 5 | - Author Terraform code for Bootstrap backend (S3 bucket for remote state + DynamoDB table for State Locking).<br>- Author Terraform code defining target infrastructure (VPC, Public Subnets, Security Groups, EC2 instance). | 04/09/2026 | 04/09/2026 | Internship Project |

### Week 5 Achievements:
* Researched, evaluated, and aligned with mentor on project scope.
* Completed formal project proposal and finalized architecture diagrams.
* Configured local development environment and initialized structured Git repository.
* Provisioned Bootstrap remote state backend (S3 + DynamoDB State Locking) preventing concurrency conflicts.
* Codified target infrastructure (VPC, Subnets, Security Groups, EC2) into modular Terraform manifests.
