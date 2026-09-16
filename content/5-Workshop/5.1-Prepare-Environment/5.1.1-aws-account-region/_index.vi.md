---
title: "Chuẩn bị AWS Account và chọn Region"
date: 2026-08-25
weight: 1
chapter: false
pre: " <b> 5.1.1. </b> "
---

# 5.1.1. Chuẩn bị AWS Account và chọn Region

Project sử dụng AWS Region mặc định `ap-southeast-1` (Singapore). Biến `aws_region` được khai báo nhất quán tại cả bootstrap, platform và workload để các tài nguyên được tạo trong cùng một Region.

- **AWS Account**: Cần có quyền tạo các tài nguyên Workshop: S3, IAM, CodeBuild, CodePipeline, CodeConnections, SSM, SNS, EventBridge, CloudTrail, Budgets, VPC và EC2.
- **AWS Console**: Trong AWS Console, chọn Region Asia Pacific (Singapore) - `ap-southeast-1` trước khi thực hiện các bước quan sát hoặc kiểm tra.
- **CloudShell / Terminal**: Khi dùng AWS CloudShell hoặc terminal, đặt `AWS_REGION` và `AWS_DEFAULT_REGION` là `ap-southeast-1` để khớp với Terraform variables.

### Lệnh kiểm tra môi trường

```bash
export AWS_REGION="ap-southeast-1"
export AWS_DEFAULT_REGION="ap-southeast-1"
aws sts get-caller-identity
```

### Xác nhận AWS Account và Region

```bash
export AWS_REGION="ap-southeast-1"
export AWS_DEFAULT_REGION="$AWS_REGION"
ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
echo "AWS Account: $ACCOUNT_ID"
echo "AWS Region : $AWS_REGION"
aws sts get-caller-identity
```

> [!NOTE]
> Kết quả phải trả đúng AWS Account đang dùng cho Workshop và Region `ap-southeast-1` trước khi tạo bất kỳ resource nào.

---

![AWS IAM Console - Cấp quyền AdministratorAccess cho tài khoản IAM](/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A2nh%20ch%E1%BB%A5p%20c%E1%BA%A5p%20quy%E1%BB%81n%20cho%20t%C3%A0i%20kho%E1%BA%A3n%20IAM.png)

*AWS IAM Console - Cấp quyền AdministratorAccess cho tài khoản IAM*

![AWS CloudShell - Cấu hình AWS_REGION=ap-southeast-1 và kiểm tra get-caller-identity](/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A3nh%20ch%E1%BB%A5p%20%C4%91%E1%BB%8Bnh%20t%C3%A0i%20kho%E1%BA%A3n%20v%C3%A0%20set%20region%20m%E1%BA%B7c%20%C4%91%E1%BB%8Bnh.png)

*AWS CloudShell - Cấu hình AWS_REGION=ap-southeast-1 và kiểm tra get-caller-identity*

