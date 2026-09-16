---
title: "Cấu hình IAM & quản lý Secrets"
date: 2026-08-25
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# 5.3. Cấu hình IAM & quản lý Secrets

Chương này hướng dẫn thiết lập hệ thống IAM Role phân quyền chặt chẽ theo nguyên tắc Least Privilege và quản lý thông tin bí mật an toàn với AWS Systems Manager Parameter Store.

---

### Danh sách các bước triển khai trong mục 5.3:

- [**5.3.1. Tạo CodePipelineRole**](./5.3.1-create-codepipeline-role/): Role điều phối chuỗi cung ứng CI/CD trust codepipeline.amazonaws.com
- [**5.3.2. Tạo ScanBuildRole**](./5.3.2-create-scanbuild-role/): Role thực thi validate và security scan với quyền hạn đọc có giới hạn
- [**5.3.3. Tạo TerraformPlanRole**](./5.3.3-create-terraform-plan-role/): Role lập kế hoạch hạ tầng chỉ đọc hiện trạng EC2/VPC
- [**5.3.4. Tạo TerraformDeployRole**](./5.3.4-create-terraform-deploy-role/): Role duy nhất có quyền biến đổi hạ tầng EC2/VPC và PassRole EC2DemoRole
- [**5.3.5. Cấu hình AWS Systems Manager Parameter Store**](./5.3.5-configure-ssm-parameter-store/): Tạo token ngẫu nhiên lưu trữ an toàn dạng SecureString
- [**5.3.6. Lưu Secret bằng SecureString**](./5.3.6-securestring-secret-management/): Inject secret vào CodeBuild bằng biến PARAMETER_STORE không in ra log
- [**5.3.7. Kiểm tra nguyên tắc Least Privilege**](./5.3.7-verify-least-privilege-permissions/): Xác minh phân tách đặc quyền giữa 4 CI/CD roles và EC2 workload role

---
*Vui lòng chọn từng mục con ở menu bên trái hoặc liên kết phía trên để xem hướng dẫn chi tiết kèm mã nguồn và lệnh thực thi.*
