---
title: "Verify Principle of Least Privilege"
date: 2026-08-25
weight: 7
chapter: false
pre: " <b> 5.3.7. </b> "
---

# 5.3.7. Verify Principle of Least Privilege

Least Privilege is demonstrated through strict separation across 4 CI/CD service roles and 1 EC2 workload role. ScanBuildRole cannot deploy; TerraformPlanRole is primarily read-only; TerraformDeployRole only holds mutation permissions required for the workshop; EC2DemoRole only attaches `AmazonSSMManagedInstanceCore` for administration via Session Manager.

- **CodePipelineRole**: orchestration, artifacts, CodeConnections, CodeBuild, SNS.
- **ScanBuildRole**: logs + read artifacts + read designated SSM parameter.
- **TerraformPlanRole**: state/artifacts + EC2 Describe* + inspect EC2 Instance Profile.
- **TerraformDeployRole**: state/artifacts + EC2/VPC mutation + PassRole EC2DemoRole + detailed monitoring.

### Verify EC2 IAM Role / Instance Profile

```bash
aws iam get-role \
  --role-name fcaj-devsecops-dev-EC2DemoRole \
  --query 'Role.Arn' --output text

aws iam get-instance-profile \
  --instance-profile-name fcaj-devsecops-dev-EC2DemoProfile \
  --query 'InstanceProfile.{Name:InstanceProfileName,Arn:Arn}' \
  --output table
```

> [!NOTE]
> If modifications are made to `platform/iam.tf` or `iam-policy/`, re-run `terraform plan/apply` on the platform layer so AWS IAM policies are updated before the pipeline executes.

