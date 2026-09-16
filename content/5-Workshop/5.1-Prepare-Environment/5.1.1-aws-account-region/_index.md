---
title: "Prepare AWS Account and Select Region"
date: 2026-08-25
weight: 1
chapter: false
pre: " <b> 5.1.1. </b> "
---

# 5.1.1. Prepare AWS Account and Select Region

The project defaults to the AWS Region `ap-southeast-1` (Singapore). The `aws_region` variable is consistently declared across bootstrap, platform, and workload modules to ensure all resources reside in the same Region.

- **Account Permissions**: The AWS account must have permissions to provision Workshop resources: S3, IAM, CodeBuild, CodePipeline, CodeConnections, SSM, SNS, EventBridge, CloudTrail, Budgets, VPC, and EC2.
- **AWS Console**: Always select Asia Pacific (Singapore) - `ap-southeast-1` before performing visual inspections or verifications.
- **Terminal / CloudShell**: When using AWS CloudShell or local CLI, set `AWS_REGION` and `AWS_DEFAULT_REGION` to `ap-southeast-1` to match Terraform configurations.

### Environment Verification Command

```bash
export AWS_REGION="ap-southeast-1"
export AWS_DEFAULT_REGION="ap-southeast-1"
aws sts get-caller-identity
```

### Confirm AWS Account and Region

```bash
export AWS_REGION="ap-southeast-1"
export AWS_DEFAULT_REGION="$AWS_REGION"
ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
echo "AWS Account: $ACCOUNT_ID"
echo "AWS Region : $AWS_REGION"
aws sts get-caller-identity
```

> [!NOTE]
> The command must return the intended AWS Account ID and Region `ap-southeast-1` prior to provisioning any infrastructure resources.

---

![AWS IAM Console - Grant AdministratorAccess permissions to IAM user](/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A2nh%20ch%E1%BB%A5p%20c%E1%BA%A5p%20quy%E1%BB%81n%20cho%20t%C3%A0i%20kho%E1%BA%A3n%20IAM.png)

*AWS IAM Console - Grant AdministratorAccess permissions to IAM user*

![AWS CloudShell - Set AWS_REGION=ap-southeast-1 and verify get-caller-identity](/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A3nh%20ch%E1%BB%A5p%20%C4%91%E1%BB%8Bnh%20t%C3%A0i%20kho%E1%BA%A3n%20v%C3%A0%20set%20region%20m%E1%BA%B7c%20%C4%91%E1%BB%8Bnh.png)

*AWS CloudShell - Set AWS_REGION=ap-southeast-1 and verify get-caller-identity*

