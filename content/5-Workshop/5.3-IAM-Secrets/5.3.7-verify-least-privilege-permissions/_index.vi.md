---
title: "Kiểm tra nguyên tắc Least Privilege"
date: 2026-08-25
weight: 7
chapter: false
pre: " <b> 5.3.7. </b> "
---

# 5.3.7. Kiểm tra nguyên tắc Least Privilege

Least Privilege được thể hiện qua việc tách 4 CI/CD service role theo trách nhiệm và một EC2 workload role riêng. ScanBuildRole không có quyền deploy; TerraformPlanRole chủ yếu đọc; TerraformDeployRole chỉ có quyền mutation cần cho Workshop; EC2DemoRole chỉ gắn `AmazonSSMManagedInstanceCore` để quản trị instance qua Session Manager.

- **CodePipelineRole**: orchestration, artifact, CodeConnections, CodeBuild, SNS.
- **ScanBuildRole**: log + read artifact + read đúng SSM parameter.
- **TerraformPlanRole**: state/artifact + EC2 Describe* + đọc đúng EC2 Instance Profile.
- **TerraformDeployRole**: state/artifact + EC2/VPC mutation + PassRole EC2DemoRole + detailed monitoring.

### Xác minh EC2 IAM Role/Instance Profile

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
> Nếu vừa sửa `platform/iam.tf` hoặc `iam-policy/`, cần `terraform plan/apply` lại layer platform để policy thật trên AWS được cập nhật trước khi chạy pipeline.

