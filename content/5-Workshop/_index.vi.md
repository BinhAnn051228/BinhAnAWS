---
title: "Workshop"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5. </b> "
---

# FCAJ AWS DevSecOps Workshop

### Tổng quan Workshop

Mục tiêu của Workshop là thiết kế và triển khai một **chuỗi cung ứng phần mềm và hạ tầng an toàn (DevSecOps CI/CD Pipeline)** hoàn chỉnh trên nền tảng điện toán đám mây **Amazon Web Services (AWS)**. Toàn bộ quy trình từ kiểm thử chất lượng, kiểm tra bảo mật Shift-Left (SAST, SCA, Secret Scanning, IaC Scanning), sinh kế hoạch thay đổi (Terraform Plan), cổng phê duyệt thủ công (Manual Approval), triển khai hạ tầng đích (Terraform Apply) và kiểm thử sau triển khai (Post-Deploy Smoke Test) đều được tự động hóa và kiểm soát chặt chẽ.

Hệ thống tuân thủ nguyên tắc thiết kế **Managed-First** (tận dụng tối đa dịch vụ AWS Managed như CodePipeline, CodeBuild, S3, SSM Parameter Store, EventBridge, CloudWatch, SNS) kết hợp các công cụ mã nguồn mở đầu ngành (**Gitleaks, Bandit, Trivy, Checkov**) để tối ưu chi phí và nâng cao hiệu quả bảo mật.

---

### Nội dung

1. [Môi trường & kiến trúc triển khai](5.1-prepare-environment/)
2. [Khởi tạo Terraform Backend & quản lý State](5.2-terraform-backend-state/)
3. [Cấu hình IAM & quản lý Secrets](5.3-iam-secrets/)
4. [Kết nối GitHub với AWS CodePipeline](5.4-github-codepipeline/)
5. [Xây dựng Validate, Test & Shift-Left Security](5.5-validate-security-gates/)
6. [Lập kế hoạch hạ tầng và phê duyệt](5.6-terraform-plan-approval/)
7. [Triển khai hạ tầng tự động](5.7-terraform-apply/)
8. [Môi trường triển khai mục tiêu](5.8-target-environment/)
9. [Kiểm thử và xác thực sau triển khai](5.9-post-deploy-verification/)
10. [Giám sát, nhật ký và cảnh báo](5.10-logging-monitoring-notification/)
11. [Hoàn thiện AWS DevSecOps Pipeline](5.11-devsecops-pipeline/)
12. [Kịch bản kiểm thử bảo mật DevSecOps](5.12-devsecops-scenarios/)
13. [Đánh giá kết quả và dọn dẹp tài nguyên](5.13-results-cleanup/)

---

*Vui lòng chọn từng mục ở menu bên trái hoặc danh sách phía trên để xem hướng dẫn chi tiết kèm mã nguồn và lệnh thực thi.*
