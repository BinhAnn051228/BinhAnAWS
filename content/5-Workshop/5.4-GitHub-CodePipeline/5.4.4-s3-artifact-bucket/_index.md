---
title: "Create Amazon S3 Pipeline Artifact Bucket"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.4.4. </b> "
---

# 5.4.4. Create Amazon S3 Pipeline Artifact Bucket

The artifact bucket is created during bootstrap, fully decoupled from Terraform State. The bucket enforces Versioning, SSE-S3, Block Public Access, BucketOwnerEnforced, and lifecycle rules expiring old artifacts after 30 days (noncurrent versions after 7 days).

### Lifecycle Configuration

```hcl
resource "aws_s3_bucket_lifecycle_configuration" "pipeline_artifacts" {
  bucket = aws_s3_bucket.pipeline_artifacts.id
  rule {
    id     = "expire-old-pipeline-artifacts"
    status = "Enabled"
    filter {}
    expiration {
      days = 30
    }
    noncurrent_version_expiration {
      noncurrent_days = 7
    }
  }
}
```

---

![S3 Artifact Bucket resource configuration in bootstrap/main.tf](/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%201.png)

*S3 Artifact Bucket resource configuration in bootstrap/main.tf*

![Export pipeline_artifact_bucket output in bootstrap/outputs.tf](/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%202.png)

*Export pipeline_artifact_bucket output in bootstrap/outputs.tf*

