---
title: "Configure Versioning, Encryption, and Block Public Access"
date: 2026-08-25
weight: 2
chapter: false
pre: " <b> 5.2.2. </b> "
---

# 5.2.2. Configure Versioning, Encryption, and Block Public Access

The state bucket enforces Versioning, SSE-S3 (AES256), Block Public Access, and BucketOwnerEnforced. These controls provide version history, encryption at rest, and complete isolation from public exposure.

### Security Controls Applied to Terraform State Bucket

```hcl
resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_ownership_controls" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}
```

---

![Amazon S3 Console - Bucket Versioning Enabled protecting Terraform State](/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/bucket%20verioning%20enable.png)

*Amazon S3 Console - Bucket Versioning Enabled protecting Terraform State*

![Amazon S3 Console - Server-side Default Encryption SSE-S3](/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/default%20encrytion%20.png)

*Amazon S3 Console - Server-side Default Encryption SSE-S3*

![Amazon S3 Console - Block All Public Access preventing unauthorized exposure](/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/permissions%20block%20all%20publicj%20access%20on.png)

*Amazon S3 Console - Block All Public Access preventing unauthorized exposure*

