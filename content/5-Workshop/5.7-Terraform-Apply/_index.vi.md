---
title: "Triển khai hạ tầng tự động"
date: 2026-08-25
weight: 7
chapter: false
pre: " <b> 5.7. </b> "
---

# 5.7. Triển khai hạ tầng tự động

Chương này hướng dẫn cấu hình dự án AWS CodeBuild cho giai đoạn **Terraform Apply**, đảm bảo việc triển khai hạ tầng được thực thi an toàn bằng vai trò đặc quyền tối thiểu (**TerraformDeployRole**) và chỉ sử dụng đúng tệp kế hoạch nhị phân đã được phê duyệt.

---

### Vai trò TerraformDeployRole và Cơ chế triển khai an toàn

Giai đoạn `TerraformApply` được cấp quyền thông qua `TerraformDeployRole`. Vai trò này chỉ cho phép tạo, sửa và quản lý các tài nguyên trong phạm vi workload (VPC, Subnet, Route Table, Internet Gateway, Security Group, EC2 instance và IAM Instance Profile liên quan).

```bash
# Cập nhật Platform khi có thay đổi trong định nghĩa IAM Role hoặc Pipeline
cd ~/fcaj-aws-devsecops/platform
terraform init
terraform plan
terraform apply -auto-approve
```

### Sử dụng tệp kế hoạch đã phê duyệt và Thực thi Apply

1. **Nhận Artifacts đầu vào**:
   CodeBuild nhận đồng thời `SourceOutput` (mã nguồn ứng dụng) và `PlanOutput` (tệp `tfplan` đã qua bước phê duyệt thủ công).
2. **Khởi tạo và thực thi chính xác binary plan**:
   Hệ thống khởi chạy `terraform apply` trực tiếp với tệp kế hoạch đã định sẵn, không cho phép sinh lại plan mới trong lúc apply:
   ```bash
   RUN_MODE=apply
   terraform -chdir="${WORKLOAD_DIR}" init      -backend-config="bucket=${TF_STATE_BUCKET}"      -backend-config="key=workload/terraform.tfstate"      -backend-config="region=${AWS_REGION}"
   terraform -chdir="${WORKLOAD_DIR}" apply -input=false -auto-approve tfplan
   ```
3. **Xuất giá trị đầu ra (Workload Outputs)**:
   Sau khi apply thành công, các thông số như `ec2_public_ip` và `app_health_url` được xuất ra để chuyển tiếp cho bước kiểm tra sau triển khai.
