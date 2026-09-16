---
title: "Configure AWS Systems Manager Parameter Store"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.3.5. </b> "
---

# 5.3.5. Configure AWS Systems Manager Parameter Store

The platform generates a random token stored in SSM Parameter Store as type `SecureString`. The path follows the pattern `/<project>/<environment>/demo_token`.

### SSM SecureString Declaration

```hcl
resource "aws_ssm_parameter" "demo_token" {
  name        = local.demo_token_path
  description = "Demo SecureString consumed by CodeBuild without printing the value."
  type        = "SecureString"
  value       = random_password.demo_token.result
  overwrite   = true
}
```

---

![AWS Systems Manager Parameter Store - SecureString Secret Management](/images/5-Workshop/5.3-IAM-Secrets/5.3.2-ssm-parameter-store/check%20SSM.png)

*AWS Systems Manager Parameter Store - SecureString Secret Management*

