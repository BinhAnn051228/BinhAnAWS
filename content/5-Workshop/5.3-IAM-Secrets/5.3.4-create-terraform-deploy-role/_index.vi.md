---
title: "Tạo TerraformDeployRole"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.3.4. </b> "
---

# 5.3.4. Tạo TerraformDeployRole

Role cho Terraform Apply. Policy cho phép các API EC2/VPC cần thiết để tạo/xóa tài nguyên Workshop, `ec2:MonitorInstances`/`UnmonitorInstances` cho detailed monitoring, `iam:GetInstanceProfile` và `iam:PassRole` được scope tới `EC2DemoRole`, cùng quyền state/artifact cần thiết.

```hcl
resource "aws_iam_role" "terraform_deploy" {
  name               = "${local.name}-TerraformDeployRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```

---

![AWS IAM Console - Cấu hình TerraformDeployRole giới hạn quyền deploy EC2/VPC](/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.4-terraform-deploy-role.png)

*AWS IAM Console - Cấu hình TerraformDeployRole giới hạn quyền deploy EC2/VPC*

