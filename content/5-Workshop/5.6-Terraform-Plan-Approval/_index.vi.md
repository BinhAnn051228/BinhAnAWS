---
title: "Lập kế hoạch hạ tầng và phê duyệt"
date: 2026-08-25
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# 5.6. Lập kế hoạch hạ tầng và phê duyệt

Chương này hướng dẫn cấu hình dự án AWS CodeBuild cho giai đoạn **Terraform Plan**, lưu trữ tệp kế hoạch thay đổi hạ tầng dưới dạng Artifact và thiết lập cổng phê duyệt thủ công (**Manual Approval**) giúp kiểm soát chặt chẽ các tác động hạ tầng trước khi triển khai thực tế.

---

### Cấu hình CodeBuild Terraform Plan và Runtime Variables

Giai đoạn `TerraformPlan` sử dụng CodeBuild project chuyên biệt với vai trò `TerraformPlanRole`. Dự án nhận tệp buildspec `cicd/buildspec-plan.yml` và được cung cấp các biến môi trường runtime từ tầng platform:

```bash
# Kiểm tra các runtime variables được truyền vào CodeBuild Plan
echo "TF_STATE_BUCKET   : ${TF_STATE_BUCKET}"
echo "WORKLOAD_ROLE_ARN : ${WORKLOAD_ROLE_ARN}"
echo "WORKLOAD_DIR      : ${WORKLOAD_DIR}"
```

### Thực thi Terraform Init và Sinh kế hoạch triển khai

1. **Khởi tạo Terraform Backend**:
   CodeBuild cấu hình backend từ xa trỏ tới S3 bucket đã được khởi tạo trong tầng bootstrap:
   ```bash
   terraform -chdir="${WORKLOAD_DIR}" init      -backend-config="bucket=${TF_STATE_BUCKET}"      -backend-config="key=workload/terraform.tfstate"      -backend-config="region=${AWS_REGION}"
   ```

2. **Sinh kế hoạch thay đổi (Plan Output)**:
   Lệnh `terraform plan` tạo ra bản nhị phân `tfplan` và xuất bản báo cáo dạng văn bản `plan.txt` để người phê duyệt dễ dàng đọc hiểu:
   ```bash
   terraform -chdir="${WORKLOAD_DIR}" plan -out=tfplan -input=false
   terraform -chdir="${WORKLOAD_DIR}" show -no-color tfplan > plan.txt
   ```

### Đóng gói Artifact và Thiết lập cổng Manual Approval

- **Lưu trữ Artifact**: Tệp nhị phân `tfplan`, bản mô tả `plan.txt` và tệp khóa `.terraform.lock.hcl` được đóng gói thành artifact `PlanOutput` và lưu trữ an toàn trong S3 Pipeline Artifact Store.
- **Manual Approval Stage**: Pipeline tạm dừng sau khi hoàn thành bước Plan. Người có thẩm quyền (Reviewer) xem xét nội dung tệp `plan.txt`, kiểm tra danh sách tài nguyên sẽ được thêm mới, chỉnh sửa hoặc xóa bỏ.
- **Quyết định phê duyệt**:
  - Chọn **Approve**: Cho phép pipeline chuyển tiếp sang giai đoạn `TerraformApply`.
  - Chọn **Reject**: Hủy bỏ đợt triển khai, bảo vệ hệ thống khỏi những thay đổi không mong muốn.

---

![Giao diện phê duyệt thay đổi hạ tầng tại bước Manual Approval trong AWS CodePipeline](/images/5-Workshop/5.6-Terraform-Plan-Approval/manual-approval.png)

*Giao diện phê duyệt thay đổi hạ tầng tại bước Manual Approval trong AWS CodePipeline*
