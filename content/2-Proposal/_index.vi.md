---
title: "Bản đề xuất"
date: 2026-07-21
weight: 2
chapter: false
pre: " <b> 2. </b> "
---

# Đề xuất Kiến trúc DevSecOps trên AWS
## CI/CD Pipeline tích hợp Bảo mật và Tối ưu chi phí

### 1. Đặt vấn đề
Trong quá trình phát triển và vận hành phần mềm, việc triển khai hạ tầng thủ công tiềm ẩn nhiều rủi ro về sai sót cấu hình và tốn kém thời gian. Đặc biệt, nếu các vấn đề bảo mật chỉ được phát hiện ở giai đoạn cuối của quá trình phát triển (hoặc sau khi đã triển khai lên Production), chi phí và công sức để khắc phục sẽ rất lớn.

Do đó, việc áp dụng **Shift-Left Security** – đưa các bước kiểm tra bảo mật (quét mã nguồn, kiểm tra thư viện phụ thuộc, quét cấu hình hạ tầng) vào giai đoạn sớm nhất của quy trình CI/CD là vô cùng quan trọng. Nó giúp phát hiện và ngăn chặn lỗ hổng ngay từ khi lập trình viên đẩy code lên hệ thống.

### 2. Thiết kế Giải pháp
Giải pháp đề xuất xây dựng một quy trình **DevSecOps** tự động hoàn toàn trên AWS, sử dụng các dịch vụ Managed Services kết hợp với các công cụ bảo mật mã nguồn mở để đạt được hiệu quả tối đa với chi phí tối thiểu (tận dụng Free Tier).

![Sơ đồ kiến trúc giải pháp AWS DevSecOps Pipeline](/images/2-Proposal/architecture.png)

*Sơ đồ kiến trúc giải pháp AWS DevSecOps Pipeline*

#### Các dịch vụ AWS và vai trò trong dự án:
| Dịch vụ AWS | Vai trò trong dự án | Tối ưu Free Tier |
| :--- | :--- | :--- |
| **AWS CodeCommit / GitHub** | Lưu trữ mã nguồn (Application & Terraform) | Miễn phí (GitHub) hoặc 5 active users (CodeCommit) |
| **AWS CodeBuild** | Môi trường chạy các bài test bảo mật và build artifact | 100 phút build/tháng (loại general1.small) |
| **AWS CodePipeline** | Điều phối toàn bộ quy trình CI/CD | 1 active pipeline miễn phí mỗi tháng |
| **Amazon S3** | Lưu trữ Artifacts từ CodePipeline và Terraform State | 5GB Standard Storage miễn phí |
| **System Manager (SSM)** | Lưu trữ các biến môi trường nhạy cảm (API Keys, DB Pass) | Standard parameters miễn phí 100% |

### 3. Triển khai Thực tế
Quy trình thiết lập dự án tuân thủ thứ tự chặt chẽ để đảm bảo hạ tầng được cấp quyền và bảo mật từ những bước đầu tiên:

1. **Khởi tạo Backend lưu trữ và Quản lý Secrets**: 
   - Sử dụng S3 để quản lý Terraform State an toàn với Versioning và Encryption.
   - Quản lý các tham số nhạy cảm qua SSM Parameter Store.
2. **Cấu hình IAM Role**: 
   - Áp dụng nguyên tắc đặc quyền tối thiểu (Least Privilege) cho CodeBuild và CodePipeline.
3. **Viết kịch bản DevSecOps (`buildspec.yml`)**: Tích hợp các công cụ quét bảo mật vào AWS CodeBuild:
   - **SCA (Software Composition Analysis)**: Dùng Trivy hoặc Safety quét thư viện phụ thuộc.
   - **SAST (Static Application Security Testing)**: Dùng Bandit (nếu code Python) hoặc SonarQube quét mã nguồn.
   - **IaC Scanning**: Dùng tfsec hoặc Checkov quét cấu hình Terraform nhằm phát hiện misconfigurations.
4. **Thiết lập AWS CodePipeline**: 
   - **Stage 1 (Source)**: Bắt sự kiện commit từ Github/CodeCommit.
   - **Stage 2 (Test & Scan)**: Chạy quét bảo mật với CodeBuild. Ngừng pipeline nếu có lỗi CRITICAL/HIGH.
   - **Stage 3 (Deploy)**: Tự động apply hạ tầng Terraform qua CodeBuild.

### 4. Trình diễn DevSecOps
Kịch bản demo:
- Cố tình viết một đoạn code chứa lỗ hổng hoặc cấu hình Terraform mở port 22 ra public (0.0.0.0/0).
- Push code lên nhánh chính.
- CodeBuild chạy quét mã nguồn, phát hiện lỗ hổng bằng tfsec/Checkov và **báo lỗi đỏ (Failed)**, chặn đứng việc triển khai hạ tầng lỗi ra môi trường thực tế.

![AWS CodePipeline bị chặn tại SecurityScan khi phát hiện vi phạm](/images/2-Proposal/checkov-block-pipeline.png)

*AWS CodePipeline bị chặn tại SecurityScan khi phát hiện vi phạm*

![Nhật ký chi tiết CodeBuild ghi nhận lỗi và chặn thực thi pipeline](/images/2-Proposal/log-checkov-block-pipeline.png)

*Nhật ký chi tiết CodeBuild ghi nhận lỗi và chặn thực thi pipeline*

### 5. Kết luận & Bài học kinh nghiệm
Giải pháp DevSecOps mang lại quy trình tự động, an toàn và có khả năng tối ưu hóa chi phí cực tốt khi tận dụng được các dịch vụ Free Tier của AWS và công cụ mã nguồn mở. 
Trong tương lai, giải pháp có thể dễ dàng mở rộng để tích hợp thêm các dịch vụ bảo mật chuyên sâu của AWS như **Amazon Inspector** hay **AWS Security Hub** cho các môi trường doanh nghiệp quy mô lớn hơn.