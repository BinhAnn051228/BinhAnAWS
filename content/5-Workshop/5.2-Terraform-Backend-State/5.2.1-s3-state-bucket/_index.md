---
title: "Create Amazon S3 Bucket for Terraform State"
date: 2026-08-25
weight: 1
chapter: false
pre: " <b> 5.2.1. </b> "
---

# 5.2.1. Create Amazon S3 Bucket for Terraform State

Bootstrap creates a dedicated S3 bucket for Terraform State. The bucket name is constructed from project name, AWS Account ID, and Region to ensure global uniqueness: `${local.prefix}-tfstate`.

### Terraform State Bucket

```hcl
resource "aws_s3_bucket" "terraform_state" {
  bucket = "${local.prefix}-tfstate"
}
```

After `terraform apply`, the output `terraform_state_bucket` returns the bucket name used for backend configuration of platform and workload.

### Bootstrap S3 State and Artifact Buckets

```bash
cd ~/fcaj-aws-devsecops/bootstrap
cp -n terraform.tfvars.example terraform.tfvars
terraform init
terraform fmt -check
terraform validate
terraform plan -out=bootstrap.tfplan
terraform apply bootstrap.tfplan
terraform output
```

> [!IMPORTANT]
> Always execute plan/apply inside the `bootstrap` directory. Local `*.tfplan` files and `terraform.tfstate` must be `.gitignore`'d and never committed to GitHub.

---

![Amazon S3 Console - S3 Buckets created for Terraform State and Pipeline Artifacts](/images/5-Workshop/5.2-Terraform-Backend-State/5.2.1-s3-state-bucket/t%E1%BA%A1o%20bucket.png)

*Amazon S3 Console - S3 Buckets created for Terraform State and Pipeline Artifacts*

