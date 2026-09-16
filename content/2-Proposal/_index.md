---
title: "Proposal"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# DevSecOps Architecture Proposal on AWS
## Security-Integrated and Cost-Optimized CI/CD Pipeline

### 1. The Problem
In software development and operations, manual infrastructure deployment poses significant risks of misconfigurations and is time-consuming. More importantly, if security issues are only discovered at the end of the development lifecycle (or after deployment to Production), the cost and effort to remediate them are enormous.

Therefore, adopting **Shift-Left Security** – integrating security checks (source code scanning, dependency checking, infrastructure configuration scanning) into the earliest stages of the CI/CD pipeline is crucial. It helps detect and prevent vulnerabilities from the moment developers push code to the repository.

### 2. Architecture Design
The proposed solution builds a fully automated **DevSecOps** pipeline on AWS, leveraging Managed Services combined with open-source security tools to achieve maximum efficiency at minimal cost (taking advantage of the Free Tier).

![AWS DevSecOps Pipeline Recommended Architecture Diagram](/images/2-Proposal/architecture.png)

*AWS DevSecOps Pipeline Recommended Architecture Diagram*

#### AWS Services and Roles in the Project:
| AWS Service | Role in Project | Free Tier Optimization |
| :--- | :--- | :--- |
| **AWS CodeCommit / GitHub** | Source code storage (Application & Terraform) | Free (GitHub) or 5 active users (CodeCommit) |
| **AWS CodeBuild** | Environment for running security tests and building artifacts | 100 build minutes/month (general1.small instance) |
| **AWS CodePipeline** | Orchestrates the entire CI/CD process | 1 active pipeline free per month |
| **Amazon S3** | Stores Artifacts from CodePipeline and Terraform State | 5GB Standard Storage free |
| **System Manager (SSM)** | Stores sensitive environment variables (API Keys, DB Pass) | Standard parameters 100% free |

### 3. Implementation
The project setup follows a strict order to ensure the infrastructure is permissioned and secured from the very first steps:

1. **Initialize Storage Backend and Secrets Management**: 
   - Use S3 to manage Terraform State securely with Versioning and Encryption.
   - Manage sensitive parameters via SSM Parameter Store.
2. **Configure IAM Roles**: 
   - Apply the principle of Least Privilege for CodeBuild and CodePipeline roles.
3. **Write DevSecOps Script (`buildspec.yml`)**: Integrate security scanning tools into AWS CodeBuild:
   - **SCA (Software Composition Analysis)**: Use Trivy or Safety to scan dependencies.
   - **SAST (Static Application Security Testing)**: Use Bandit (for Python) or SonarQube to scan source code.
   - **IaC Scanning**: Use tfsec or Checkov to scan Terraform configurations for misconfigurations.
4. **Set Up AWS CodePipeline**: 
   - **Stage 1 (Source)**: Triggered by commits from Github/CodeCommit.
   - **Stage 2 (Test & Scan)**: Run security scans with CodeBuild. Halt pipeline if CRITICAL/HIGH errors occur.
   - **Stage 3 (Deploy)**: Automatically apply Terraform infrastructure via CodeBuild.

### 4. DevSecOps Demo/PoC
This is the core section to prove effectiveness. Demo scenario:
- Intentionally write vulnerable code or a Terraform config that opens port 22 to the public (0.0.0.0/0).
- Push the code to the main branch.
- CodeBuild runs the security scans, detects the vulnerability using tfsec/Checkov, and **fails with a red error (Failed)**, blocking the flawed infrastructure from being deployed to the real environment.

![AWS CodePipeline halted at SecurityScan upon detecting security violation](/images/2-Proposal/checkov-block-pipeline.png)

*AWS CodePipeline halted at SecurityScan upon detecting security violation*

![Detailed CodeBuild execution log confirming build failure and blocking deployment](/images/2-Proposal/log-checkov-block-pipeline.png)

*Detailed CodeBuild execution log confirming build failure and blocking deployment*

### 5. Conclusion & Lessons Learned
The DevSecOps solution delivers an automated, secure process with excellent cost optimization capabilities by leveraging AWS Free Tier services and open-source tools. 
In the future, the solution can easily be expanded to integrate more advanced AWS security services like **Amazon Inspector** or **AWS Security Hub** for larger enterprise environments.