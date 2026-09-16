---
title: "Secure Secrets Management via SecureString"
date: 2026-08-25
weight: 6
chapter: false
pre: " <b> 5.3.6. </b> "
---

# 5.3.6. Secure Secrets Management via SecureString

CodeBuild injects the secret into variable `DEMO_TOKEN` via environment variable type `PARAMETER_STORE`. The build script validates token presence without printing the value:

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

