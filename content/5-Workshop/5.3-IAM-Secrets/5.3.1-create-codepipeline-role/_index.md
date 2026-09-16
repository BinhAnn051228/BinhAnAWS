---
title: "Create CodePipelineRole"
date: 2026-08-25
weight: 1
chapter: false
pre: " <b> 5.3.1. </b> "
---

# 5.3.1. Create CodePipelineRole

Execution role for AWS CodePipeline, trusting principal `codepipeline.amazonaws.com` and granted policies for artifact bucket operations, CodeConnections, CodeBuild start/get builds, and SNS approval notifications.

```hcl
resource "aws_iam_role" "codepipeline" {
  name               = "${local.name}-CodePipelineRole"
  assume_role_policy = data.aws_iam_policy_document.codepipeline_assume.json
}
```

---

![AWS IAM Console - CodePipelineRole configuration and trust relationships](/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.1-codepipeline-role.png)

*AWS IAM Console - CodePipelineRole configuration and trust relationships*

