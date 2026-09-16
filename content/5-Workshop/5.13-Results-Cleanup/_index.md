---
title: "Workshop Acceptance & Resource Cleanup"
date: 2026-08-25
weight: 13
chapter: false
pre: " <b> 5.13. </b> "
---

# 5.13. Workshop Acceptance & Resource Cleanup

This chapter summarizes the project deliverables against workshop acceptance criteria and provides a step-by-step teardown procedure to destroy all AWS resources in correct dependency order.

---

### Workshop Acceptance Evaluation

The project fulfills all architectural and security objectives defined for the AWS DevSecOps Workshop:
- **Full Automation**: Automated 7-stage continuous delivery pipeline orchestrated by AWS CodePipeline from Git push to post-deploy testing.
- **Multi-Layer Shift-Left Security**: Concurrent execution of Gitleaks, Bandit, Trivy, and Checkov acting as blocking security gates.
- **Governance & Change Control**: Deterministic Terraform Plan artifacts coupled with Manual Approval gates before apply execution.
- **Full-Stack Observability**: Centralized CloudWatch logging, EventBridge state tracking, SNS email alerts, and CloudTrail audit logging.
- **Automated Verification**: PostDeployVerification smoke testing ensuring host and HTTP application health before completion.

---

### Resource Cleanup in Dependency Order

To prevent dependency lockouts during teardown, infrastructure destruction must strictly follow this 3-step sequence:

#### Step 1: Destroy Workload Infrastructure Layer

Workload resources (EC2 instances, VPCs, Subnets, Route Tables, and Security Groups) must be destroyed first:

```bash
cd ~/fcaj-aws-devsecops/workload

# Initialize and destroy workload
terraform init
terraform destroy -auto-approve
```

#### Step 2: Destroy CI/CD Platform Layer

Once the workload layer is completely destroyed, teardown CodePipeline, CodeBuild projects, IAM roles, EventBridge rules, and SNS topics:

```bash
cd ~/fcaj-aws-devsecops/platform

# Initialize and destroy platform
terraform init
terraform destroy -auto-approve
```

#### Step 3: Purge S3 Buckets & Destroy Bootstrap Layer

S3 buckets storing state and build artifacts enforce object versioning. Purge all bucket contents before executing destroy:

```bash
# Empty state and artifact buckets
aws s3 rm "s3://${TF_STATE_BUCKET}" --recursive
aws s3 rm "s3://${ARTIFACT_BUCKET}" --recursive

# Destroy bootstrap resources
cd ~/fcaj-aws-devsecops/bootstrap
terraform init
terraform destroy -auto-approve
```

---

### Verifying Residual Resources & Billing Confirmation

Verify that no unmanaged or orphaned resources remain running in the AWS account:

```bash
# Confirm zero running EC2 instances
aws ec2 describe-instances   --filters "Name=instance-state-name,Values=running"   --query "Reservations[].Instances[].InstanceId"   --output text

# Confirm workshop S3 buckets are removed
aws s3 ls | grep fcaj || true
```

> [!TIP]
> Reviewing the AWS Billing & Cost Management console 24 hours after teardown confirms zero residual charges.
