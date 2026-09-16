---
title: "Tạo ScanBuildRole"
date: 2026-08-25
weight: 2
chapter: false
pre: " <b> 5.3.2. </b> "
---

# 5.3.2. Tạo ScanBuildRole

Role cho CodeBuild validate/security. Policy chỉ cho phép ghi CloudWatch Logs, đọc pipeline artifact và đọc đúng SSM parameter demo.

```hcl
resource "aws_iam_role" "scan_build" {
  name               = "${local.name}-ScanBuildRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```

---

![AWS IAM Console - Cấu hình ScanBuildRole và policy quyền đọc hạn chế](/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.2-scan-build-role.png)

*AWS IAM Console - Cấu hình ScanBuildRole và policy quyền đọc hạn chế*

