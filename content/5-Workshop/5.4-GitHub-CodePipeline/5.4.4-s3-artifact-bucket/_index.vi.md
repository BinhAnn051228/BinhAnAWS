---
title: "Tạo Amazon S3 Pipeline Artifact Bucket"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.4.4. </b> "
---

# 5.4.4. Tạo Amazon S3 Pipeline Artifact Bucket

Artifact bucket được tạo ngay trong bootstrap, tách biệt với Terraform State. Bucket bật Versioning, SSE-S3, Block Public Access, BucketOwnerEnforced và lifecycle xóa artifact cũ sau 30 ngày; noncurrent version hết hạn sau 7 ngày.

### Khai báo Lifecycle Configuration

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

![Khai báo tài nguyên S3 Artifact Bucket trong bootstrap/main.tf](/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%201.png)

*Khai báo tài nguyên S3 Artifact Bucket trong bootstrap/main.tf*

![Khai báo output pipeline_artifact_bucket trong bootstrap/outputs.tf](/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%202.png)

*Khai báo output pipeline_artifact_bucket trong bootstrap/outputs.tf*

