---
title: "Tạo Amazon S3 Bucket lưu Terraform State"
date: 2026-08-25
weight: 1
chapter: false
pre: " <b> 5.2.1. </b> "
---

# 5.2.1. Tạo Amazon S3 Bucket lưu Terraform State

Bootstrap tạo một S3 bucket riêng cho Terraform State. Tên bucket được ghép từ project name, AWS Account ID và Region để giảm khả năng trùng tên toàn cục.

### Terraform State bucket

```hcl
resource "aws_s3_bucket" "terraform_state" {
  bucket = "${local.prefix}-tfstate"
}
```

Sau `terraform apply`, output `terraform_state_bucket` trả về tên bucket dùng cho backend của platform và workload.

### Bootstrap S3 State và Artifact bucket

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
> Luôn chạy plan/apply trong đúng thư mục `bootstrap`. File `*.tfplan` và `terraform.tfstate` local phải được `.gitignore` và không commit lên GitHub.

---

![Amazon S3 Console - Danh sách các S3 Bucket phục vụ Terraform State và Pipeline Artifacts](/images/5-Workshop/5.2-Terraform-Backend-State/5.2.1-s3-state-bucket/t%E1%BA%A1o%20bucket.png)

*Amazon S3 Console - Danh sách các S3 Bucket phục vụ Terraform State và Pipeline Artifacts*

