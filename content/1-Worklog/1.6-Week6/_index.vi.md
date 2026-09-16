---
title: "Worklog Tuần 6"
date: 2026-09-07
weight: 6
chapter: false
pre: " <b> 1.6. </b> "
---

### Mục tiêu tuần 6:
* Xây dựng chuỗi CI/CD tự động với AWS CodePipeline và AWS CodeBuild.
* Tích hợp bộ công cụ kiểm tra bảo mật tự động Shift-Left (Gitleaks, Bandit, Trivy, Checkov).
* Thiết lập cơ chế kiểm soát chất lượng an ninh (Security Quality Gate) tự động chặn pipeline khi có rủi ro cao.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tạo các IAM Service Roles (CodePipelineRole, ScanBuildRole, TerraformPlanRole, TerraformDeployRole).<br>- Áp dụng nghiêm ngặt nguyên tắc quyền hạn tối thiểu (Least Privilege).<br>- Lưu các thông tin nhạy cảm vào AWS SSM Parameter Store với SecureString. | 07/09/2026 | 07/09/2026 | Dự án thực tập |
| 3 | - Cấu hình AWS CodeConnections liên kết GitHub repository với AWS CodePipeline.<br>- Thiết lập webhook tự động kích hoạt pipeline mỗi khi có commit mới được đẩy lên Git. | 08/09/2026 | 08/09/2026 | Dự án thực tập |
| 4 | - Xây dựng dự án AWS CodeBuild và viết file kịch bản cấu hình `buildspec.yml`.<br>- Tích hợp công cụ Gitleaks quét lộ lọt API keys, mật khẩu và secrets trong lịch sử commit. | 09/09/2026 | 09/09/2026 | Dự án thực tập |
| 5 | - Tích hợp Bandit thực hiện Static Application Security Testing (SAST) cho mã nguồn ứng dụng.<br>- Tích hợp Trivy quét lỗ hổng các thư viện phụ thuộc và kiểm tra file hệ thống. | 10/09/2026 | 10/09/2026 | Dự án thực tập |
| 6 | - Tích hợp Checkov quét tuân thủ tiêu chuẩn CIS Benchmark cho mã nguồn Terraform IaC.<br>- Cấu hình chính sách tự động Fail pipeline khi phát hiện lỗ hổng nghiêm trọng (High/Critical). | 11/09/2026 | 11/09/2026 | Dự án thực tập |

### Kết quả đạt được tuần 6:
* Hoàn thành thiết lập phân quyền IAM chặt chẽ cho toàn bộ chuỗi CI/CD.
* Kết nối thông suốt giữa GitHub và AWS CodePipeline thông qua AWS CodeConnections (v2).
* Nhúng thành công 4 công cụ bảo mật chuyên dụng (Gitleaks, Bandit, Trivy, Checkov) vào môi trường container AWS CodeBuild.
* Thiết lập thành công cổng bảo mật tự động (Security Quality Gate) ngăn chặn các rủi ro an ninh trước khi tài nguyên đám mây được khởi tạo.
