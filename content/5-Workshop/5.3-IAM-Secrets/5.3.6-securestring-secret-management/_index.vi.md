---
title: "Lưu Secret bằng SecureString"
date: 2026-08-25
weight: 6
chapter: false
pre: " <b> 5.3.6. </b> "
---

# 5.3.6. Lưu Secret bằng SecureString

CodeBuild inject parameter vào biến `DEMO_TOKEN` bằng environment variable type `PARAMETER_STORE`. Build chỉ xác minh biến tồn tại và cố ý không in giá trị ra log:

```hcl
environment_variable {
  name  = "DEMO_TOKEN"
  value = aws_ssm_parameter.demo_token.name
  type  = "PARAMETER_STORE"
}
```

### buildspec snippet

```bash
test -n "${DEMO_TOKEN:-}" || { echo "SecureString injection failed"; exit 1; }
echo "SSM SecureString was injected successfully; value intentionally not printed."
```

