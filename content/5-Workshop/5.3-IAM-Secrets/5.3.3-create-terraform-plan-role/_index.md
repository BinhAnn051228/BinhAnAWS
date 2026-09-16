---
title: "Create TerraformPlanRole"
date: 2026-08-25
weight: 3
chapter: false
pre: " <b> 5.3.3. </b> "
---

# 5.3.3. Create TerraformPlanRole

Role for Terraform Plan. Beyond log/artifact/state access, the role holds `ec2:Describe*` and `iam:GetInstanceProfile` to inspect live infrastructure and instance profiles during planning; it holds no permission to mutate workloads.

```hcl
resource "aws_iam_role" "terraform_plan" {
  name               = "${local.name}-TerraformPlanRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```

---

![AWS IAM Console - TerraformPlanRole read-only policy for EC2 Describe*](/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.3-terraform-plan-role.png)

*AWS IAM Console - TerraformPlanRole read-only policy for EC2 Describe**

