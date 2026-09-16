---
title: "Chuẩn bị Terraform và cấu trúc source code"
date: 2026-08-25
weight: 3
chapter: false
pre: " <b> 5.1.3. </b> "
---

# 5.1.3. Chuẩn bị Terraform và cấu trúc source code

Repository được chia thành các lớp độc lập để phân tách bootstrap, platform CI/CD và workload. Terraform CLI mặc định trong CodeBuild là `1.16.2`; Gitleaks `8.30.1` và Trivy `0.74.0` được cấu hình qua biến platform.

### Cấu trúc project

```text
fcaj-aws-devsecops/
├── app/              # Demo Flask app + unit tests
├── bootstrap/        # S3 Terraform State và S3 Pipeline Artifact
├── platform/         # IAM, CodeBuild, CodeConnections, CodePipeline, SNS, EventBridge, CloudTrail, Budget, SSM
├── workload/         # VPC, Public Subnet, Internet Gateway, Route Table, Security Group và EC2 demo
├── cicd/             # 3 buildspec cho validate/security, plan, apply/smoke
├── iam-policy/       # IAM policy JSON templates cho từng vai trò
├── demo/             # Fixture và script kích hoạt các tình huống lỗi có chủ đích
├── docs/             # Tài liệu kiến trúc và sơ đồ hệ thống
├── scripts/          # Shell script hỗ trợ init và cấu hình
├── .gitleaks.toml    # Cấu hình rule quét secret
├── Makefile          # Command tiện ích chạy local test/security
└── README.md         # Hướng dẫn chi tiết dự án
```

- `bootstrap/`: Tạo S3 Terraform State và S3 Pipeline Artifact.
- `platform/`: Tạo IAM, CodeBuild, CodeConnections, CodePipeline, SNS, EventBridge, CloudTrail, Budget và SSM Parameter Store.
- `workload/`: Tạo VPC, Public Subnet, Internet Gateway, Route Table, Security Group và EC2 demo.
- `cicd/`: 3 buildspec cho validate/security, plan, apply/smoke.
- `demo/`: Fixture và script kích hoạt các tình huống lỗi có chủ đích.

### Cài/kiểm tra Terraform trên CloudShell mới

```bash
cd ~
TF_VERSION="1.16.2"
curl -fsSLo /tmp/terraform.zip   "https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip"
unzip -o /tmp/terraform.zip -d "$HOME/bin"
export PATH="$HOME/bin:$PATH"
terraform version
```

> [!TIP]
> CloudShell có thể bị reset. Nếu tạo lại môi trường, chỉ cần clone repo và cài lại Terraform; tài nguyên AWS/state trong S3 không mất theo CloudShell.

