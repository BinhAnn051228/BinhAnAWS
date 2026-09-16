---
title: "Worklog Tuần 7"
date: 2026-09-14
weight: 7
chapter: false
pre: " <b> 1.7. </b> "
---

### Mục tiêu tuần 7:
* Tách biệt quy trình lập kế hoạch hạ tầng (Terraform Plan) và thực thi triển khai (Terraform Apply).
* Tích hợp cổng kiểm soát phê duyệt thủ công (Manual Approval Gate) kèm thông báo qua Amazon SNS.
* Thực thi triển khai hạ tầng tự động và kiểm thử tự động xác thực ứng dụng (Post-Deploy Smoke Test).

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Cấu hình CodeBuild thực thi `terraform plan` và xuất artifact file `tfplan`.<br>- Cấu hình Amazon SNS Topic gửi email thông báo kèm bản tóm tắt kế hoạch thay đổi cho quản trị viên. | 14/09/2026 | 14/09/2026 | Dự án thực tập |
| 3 | - Cấu hình hành động Manual Approval trong CodePipeline giữa giai đoạn Plan và Deploy.<br>- Kiểm thử cơ chế xét duyệt (Approve) và từ chối (Reject) của người phụ trách hệ thống. | 15/09/2026 | 15/09/2026 | Dự án thực tập |
| 4 | - Xây dựng giai đoạn Terraform Apply tự động trong CodeBuild sử dụng `TerraformDeployRole`.<br>- Thực thi triển khai chính xác từ file kế hoạch đã được phê duyệt (`terraform apply tfplan`). | 16/09/2026 | 16/09/2026 | Dự án thực tập |
| 5 | - Viết kịch bản kiểm thử tự động Post-Deploy Smoke Test kiểm tra máy chủ EC2.<br>- Xác thực mã phản hồi HTTP trả về 200 OK và kiểm tra nội dung trang chủ ứng dụng. | 17/09/2026 | 17/09/2026 | Dự án thực tập |
| 6 | - Kiểm thử chu trình triển khai tự động toàn diện từ khâu Git commit đến khi hoàn tất Smoke Test.<br>- Xác minh tính tự động, an toàn và độ ổn định của toàn bộ chuỗi triển khai. | 18/09/2026 | 18/09/2026 | Dự án thực tập |

### Kết quả đạt được tuần 7:
* Hoàn thiện cơ chế kiểm soát có con người giám sát (Human-in-the-loop) an toàn qua Manual Approval Gate.
* Tự động hóa hoàn toàn quy trình triển khai hạ tầng đám mây với quyền hạn tối thiểu (Least Privilege).
* Kịch bản Post-Deploy Smoke Test tự động kiểm tra và chứng minh tính sẵn sàng của ứng dụng web ngay sau triển khai.
* Chuỗi CI/CD vận hành trơn tru từ mã nguồn trên GitHub đến môi trường thực tế trên AWS.
