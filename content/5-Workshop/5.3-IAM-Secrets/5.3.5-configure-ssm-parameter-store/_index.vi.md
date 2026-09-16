---
title: "Cấu hình AWS Systems Manager Parameter Store"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.3.5. </b> "
---

# 5.3.5. Cấu hình AWS Systems Manager Parameter Store

Platform tạo một random token và lưu tại SSM Parameter Store với type `SecureString`. Path được tạo theo mẫu `/<project>/<environment>/demo_token`.

### SSM SecureString

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

![AWS Systems Manager Parameter Store - Quản lý Secret SecureString](/images/5-Workshop/5.3-IAM-Secrets/5.3.2-ssm-parameter-store/check%20SSM.png)

*AWS Systems Manager Parameter Store - Quản lý Secret SecureString*

