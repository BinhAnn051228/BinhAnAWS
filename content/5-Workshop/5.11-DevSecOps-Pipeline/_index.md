---
title: "Complete AWS DevSecOps Pipeline"
date: 2026-08-25
weight: 11
chapter: false
pre: " <b> 5.11. </b> "
---

# 5.11. Complete AWS DevSecOps Pipeline

This chapter synthesizes the complete 7-stage **AWS CodePipeline** continuous delivery workflow into a cohesive operational overview alongside daily developer commit practices.

---

### 7-Stage Pipeline Execution Workflow

Every commit pushed to the `main` branch on GitHub automatically triggers the 7 sequential delivery stages:

```text
Source ──> ValidateTest ──> SecurityScan ──> TerraformPlan ──> ManualApproval ──> TerraformApply ──> PostDeployVerification
```

1. **Source Stage**: Captures repository pushes via AWS CodeConnections, packaging source code into the `SourceOutput` artifact.
2. **Validate & Test Stage**: Runs CodeBuild under `RUN_MODE=validate` to verify Terraform syntax formatting, test Python compilation, and execute Pytest suites.
3. **Security Scan Stage (Security Gate)**: Concurrently runs Gitleaks (Secrets), Bandit (SAST), Trivy (SCA/CVE), and Checkov (IaC). Scanner violations halt execution immediately.
4. **Terraform Plan Stage**: Generates the workload `tfplan` binary and summary `plan.txt`, packaged as the `PlanOutput` artifact.
5. **Manual Approval Stage**: Pauses execution and dispatches SNS review alerts. Administrators inspect planned changes before choosing **Approve** or **Reject**.
6. **Terraform Apply Stage**: Consumes the approved plan binary to execute `terraform apply`, ensuring predictable and tamper-free infrastructure provisioning.
7. **Post-Deploy Verification Stage**: Runs automated smoke tests validating EC2 host availability and verifying HTTP 200 status on the `/health` endpoint.

---

### Daily Developer Commit Workflow

The pipeline is provisioned once in the platform layer. Routine application or workload changes follow standard Git workflows:

```bash
cd ~/fcaj-aws-devsecops
git add -A
git status
git commit -m "feat: update application or workload"
git push origin main
```

> [!IMPORTANT]
> - There is no need to re-apply the platform layer for routine changes inside `app/` or `workload/`.
> - Avoid rapid consecutive pushes while an active execution is in `TerraformApply` to prevent state lock contention.
> - If an error occurs prior to `TerraformApply`, the pipeline fails safely and live infrastructure remains untouched.
