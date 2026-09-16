---
title: "Chuẩn bị môi trường & kiến trúc triển khai"
date: 2026-08-25
weight: 1
chapter: false
pre: " <b> 5.1. </b> "
---

# 5.1. Chuẩn bị môi trường & kiến trúc triển khai

Phần Workshop được tổ chức theo trình tự triển khai thực tế: chuẩn bị môi trường, bootstrap backend, tạo platform CI/CD, tích hợp security gate, triển khai workload, xác minh sau deploy, giám sát và cuối cùng chạy các kịch bản kiểm thử DevSecOps.

---

### Danh sách các bước triển khai trong mục 5.1:

- [**5.1.1. Chuẩn bị AWS Account và chọn Region**](./5.1.1-aws-account-region/): Thiết lập quyền hạn AWS và cấu hình Region mặc định ap-southeast-1
- [**5.1.2. Chuẩn bị GitHub Repository**](./5.1.2-github-repository/): Khởi tạo Git repo và đẩy toàn bộ source tree lên GitHub branch main
- [**5.1.3. Chuẩn bị Terraform và cấu trúc source code**](./5.1.3-terraform-code-structure/): Tổng quan cấu trúc project chia lớp độc lập và phiên bản công cụ
- [**5.1.4. Giới thiệu kiến trúc tổng thể Workshop**](./5.1.4-overall-architecture/): Sơ đồ kiến trúc tổng thể FCAJ AWS DevSecOps và các dịch vụ hỗ trợ
- [**5.1.5. Giới thiệu luồng DevSecOps triển khai**](./5.1.5-devsecops-workflow/): Luồng pipeline 7 giai đoạn nghiêm ngặt từ Source đến PostDeployVerification

---
*Vui lòng chọn từng mục con ở menu bên trái hoặc liên kết phía trên để xem hướng dẫn chi tiết kèm mã nguồn và lệnh thực thi.*
