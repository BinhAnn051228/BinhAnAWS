---
title: "Verify Terraform State"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.2.5. </b> "
---

# 5.2.5. Verify Terraform State

After init and apply, verify state using Terraform CLI and the S3 Console. Workload and platform must maintain separated state keys within the shared state bucket.

### Verify State and Lockfile

```bash
terraform -chdir=platform state list
aws s3 ls "s3://${TF_STATE_BUCKET}/platform/"
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/"

# Inspect lock files if conflicting executions are suspected
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/" | grep tflock || true
```

> [!NOTE]
> If TerraformPlan reports `Error acquiring the state lock` while a TerraformApply execution is active, wait for Apply to complete, then retry. Never remove a `.tflock` file while Terraform or CodeBuild is actively manipulating state.

