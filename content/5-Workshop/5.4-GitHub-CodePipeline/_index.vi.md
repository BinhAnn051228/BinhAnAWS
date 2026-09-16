---
title: "Kết nối GitHub với AWS CodePipeline"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.4. </b> "
---

# 5.4. Kết nối GitHub với AWS CodePipeline

Chương này hướng dẫn tích hợp AWS CodeConnections với GitHub repository, cấu hình S3 Artifact Store và xây dựng chuỗi cung ứng AWS CodePipeline 7 giai đoạn tự động.

---

### Danh sách các bước triển khai trong mục 5.4:

- [**5.4.1. Chuẩn bị Repository và Branch**](./5.4.1-prepare-repo-branch/): Cấu hình biến GitHub owner, repo và branch main cho pipeline
- [**5.4.2. Tạo AWS CodeConnections**](./5.4.2-create-codeconnections/): Khởi tạo resource aws_codeconnections_connection ở trạng thái PENDING
- [**5.4.3. Kết nối GitHub Repository**](./5.4.3-connect-github-repo/): Thao tác trên AWS Console xác thực GitHub App chuyển sang AVAILABLE
- [**5.4.4. Tạo Amazon S3 Pipeline Artifact Bucket**](./5.4.4-s3-artifact-bucket/): Tạo bucket lưu trữ artifact trung gian với lifecycle 30 ngày
- [**5.4.5. Khởi tạo AWS CodePipeline**](./5.4.5-create-codepipeline/): Định nghĩa pipeline V1 chế độ SUPERSEDED liên kết toàn diện 7 stage
- [**5.4.6. Kiểm tra Source Trigger**](./5.4.6-verify-source-trigger/): Commit push mã nguồn và xác minh CodePipeline tự động kích hoạt

---
*Vui lòng chọn từng mục con ở menu bên trái hoặc liên kết phía trên để xem hướng dẫn chi tiết kèm mã nguồn và lệnh thực thi.*
