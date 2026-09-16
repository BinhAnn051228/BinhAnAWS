---
title: "Tạo CodePipelineRole"
date: 2026-08-25
weight: 1
chapter: false
pre: " <b> 5.3.1. </b> "
---

# 5.3.1. Tạo CodePipelineRole

Role cho AWS CodePipeline, trust principal `codepipeline.amazonaws.com` và được gắn policy thao tác artifact bucket, CodeConnections, CodeBuild và SNS approval notification.

```hcl
resource "aws_iam_role" "codepipeline" {
  name               = "${local.name}-CodePipelineRole"
  assume_role_policy = data.aws_iam_policy_document.codepipeline_assume.json
}
```

---

![AWS IAM Console - Cấu hình CodePipelineRole và trust relationship](/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.1-codepipeline-role.png)

*AWS IAM Console - Cấu hình CodePipelineRole và trust relationship*

