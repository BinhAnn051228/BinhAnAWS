---
title: "Week 6 Worklog"
date: 2026-09-07
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Week 6 Objectives:
* Build an automated CI/CD pipeline using AWS CodePipeline and AWS CodeBuild.
* Integrate multi-layered Shift-Left security scanners (Gitleaks, Bandit, Trivy, Checkov).
* Establish automated Security Quality Gates with fail-fast policies against critical risks.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Create IAM Service Roles (CodePipelineRole, ScanBuildRole, TerraformPlanRole, TerraformDeployRole).<br>- Enforce Least Privilege permissions across all roles.<br>- Store sensitive configuration secrets in AWS SSM Parameter Store using SecureString. | 07/09/2026 | 07/09/2026 | Internship Project |
| 2 | - Configure AWS CodeConnections to link GitHub repository with CodePipeline.<br>- Establish automated webhook triggers on code commit pushes to the `main` branch. | 08/09/2026 | 08/09/2026 | Internship Project |
| 3 | - Construct AWS CodeBuild project and author containerized execution script `buildspec.yml`.<br>- Integrate Gitleaks for automated secret and credential scanning in git history. | 09/09/2026 | 09/09/2026 | Internship Project |
| 4 | - Integrate Bandit for Static Application Security Testing (SAST) of application code.<br>- Integrate Trivy for dependency scanning and filesystem vulnerability assessment. | 10/09/2026 | 10/09/2026 | Internship Project |
| 5 | - Integrate Checkov for Terraform Infrastructure as Code (IaC) compliance scanning against CIS Benchmarks.<br>- Configure Quality Gate policies to automatically fail the build stage on High/Critical vulnerabilities. | 11/09/2026 | 11/09/2026 | Internship Project |

### Week 6 Achievements:
* Successfully engineered tightly scoped IAM service roles for every pipeline execution stage.
* Established seamless GitHub-to-AWS continuous integration via AWS CodeConnections (v2).
* Embedded 4 automated security scanners (Gitleaks, Bandit, Trivy, Checkov) into AWS CodeBuild.
* Implemented strict Security Quality Gates preventing deployment of vulnerable infrastructure code.
