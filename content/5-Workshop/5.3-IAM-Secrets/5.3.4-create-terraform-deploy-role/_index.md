---
title: "Create TerraformDeployRole"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.3.4. </b> "
---

# 5.3.4. Create TerraformDeployRole

Role for Terraform Apply. Policy authorizes required EC2/VPC APIs for provisioning/teardown, `ec2:MonitorInstances`/`UnmonitorInstances` for detailed monitoring, `iam:GetInstanceProfile` and scoped `iam:PassRole` to `EC2DemoRole`, alongside necessary remote state and artifact access.

```hcl
resource "aws_iam_role" "terraform_deploy" {
  name               = "${local.name}-TerraformDeployRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```

---

![AWS IAM Console - TerraformDeployRole scoped deployment policies for EC2/VPC](/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.4-terraform-deploy-role.png)

*AWS IAM Console - TerraformDeployRole scoped deployment policies for EC2/VPC*

