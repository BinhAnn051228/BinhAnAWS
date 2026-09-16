---
title: "Tạo TerraformPlanRole"
date: 2026-08-25
weight: 3
chapter: false
pre: " <b> 5.3.3. </b> "
---

# 5.3.3. Tạo TerraformPlanRole

Role cho Terraform Plan. Ngoài log/artifact/state, role có `ec2:Describe*` và `iam:GetInstanceProfile` để đọc hiện trạng hạ tầng/instance profile khi lập plan; role này không có quyền mutate workload.

```hcl
resource "aws_iam_role" "terraform_plan" {
  name               = "${local.name}-TerraformPlanRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```

---

![AWS IAM Console - Cấu hình TerraformPlanRole quyền đọc chỉ hạn chế EC2 Describe*](/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.3-terraform-plan-role.png)

*AWS IAM Console - Cấu hình TerraformPlanRole quyền đọc chỉ hạn chế EC2 Describe**

