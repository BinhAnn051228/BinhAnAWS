---
title: "Workshop"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# FCAJ AWS DevSecOps Workshop

### Workshop Overview

The objective of this Workshop is to design and implement a comprehensive, production-ready **secure software and infrastructure delivery supply chain (DevSecOps CI/CD Pipeline)** on **Amazon Web Services (AWS)**. The entire lifecycle—encompassing code linting, unit testing, Shift-Left security validation (SAST, SCA, Secret Scanning, IaC Scanning), immutable change planning (Terraform Plan), gated human review (Manual Approval), target infrastructure provisioning (Terraform Apply), and automated smoke testing (Post-Deploy Smoke Test)—is fully automated and strictly governed.

The architecture adheres to the **Managed-First** design principle (maximizing managed AWS services such as CodePipeline, CodeBuild, S3, SSM Parameter Store, EventBridge, CloudWatch, and SNS) augmented by industry-standard open-source security utilities (**Gitleaks, Bandit, Trivy, Checkov**) to achieve high security efficacy at minimal operational cost.

---

### Content

1. [Environment Preparation & Deployment Architecture](5.1-prepare-environment/)
2. [Terraform Backend Initialization & State Management](5.2-terraform-backend-state/)
3. [IAM Configuration & Secrets Management](5.3-iam-secrets/)
4. [Connect GitHub with AWS CodePipeline](5.4-github-codepipeline/)
5. [Validate, Test & Shift-Left Security](5.5-validate-security-gates/)
6. [Terraform Plan & Manual Approval](5.6-terraform-plan-approval/)
7. [Terraform Apply & AWS Infrastructure Deployment](5.7-terraform-apply/)
8. [Target AWS Environment Deployment](5.8-target-environment/)
9. [Post-Deploy Verification](5.9-post-deploy-verification/)
10. [Logging, Monitoring & Notification](5.10-logging-monitoring-notification/)
11. [Complete AWS DevSecOps Pipeline](5.11-devsecops-pipeline/)
12. [DevSecOps Demo Scenarios](5.12-devsecops-scenarios/)
13. [Workshop Evaluation & Resource Teardown](5.13-results-cleanup/)

---

*Please select each section from the left sidebar or the list above to view detailed instructions, source code, and verification commands.*
