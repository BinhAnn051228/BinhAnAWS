---
title: "Create ScanBuildRole"
date: 2026-08-25
weight: 2
chapter: false
pre: " <b> 5.3.2. </b> "
---

# 5.3.2. Create ScanBuildRole

Role for CodeBuild validate/security tasks. Policy permits only writing CloudWatch logs, reading pipeline artifacts, and reading the single designated demo SSM parameter.

```hcl
resource "aws_iam_role" "scan_build" {
  name               = "${local.name}-ScanBuildRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```

---

![AWS IAM Console - ScanBuildRole configuration and restricted read policy](/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.2-scan-build-role.png)

*AWS IAM Console - ScanBuildRole configuration and restricted read policy*

