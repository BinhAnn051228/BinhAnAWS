---
title: "Worklog Tuần 4"
date: 2026-08-24
weight: 4
chapter: false
pre: " <b> 1.4. </b> "
---

### Mục tiêu tuần 4:
* Tìm hiểu hệ thống giám sát và cảnh báo trên AWS: Amazon CloudWatch (Metrics, Logs, Alarms).
* Tìm hiểu dịch vụ kiểm toán và ghi vết hoạt động tài khoản AWS CloudTrail.
* Tìm hiểu kiến trúc xử lý sự kiện với Amazon EventBridge và gửi thông báo qua Amazon SNS.
* Quản lý cấu hình tập trung và chuỗi bí mật với AWS Systems Manager (SSM) Parameter Store.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu Amazon CloudWatch Metrics.<br>- Giám sát các chỉ số vận hành của EC2 (CPU Utilization, NetworkIn/Out).<br>- Tạo cảnh báo CloudWatch Alarm tự động kích hoạt khi CPU vượt 80%. | 24/08/2026 | 24/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Tìm hiểu Amazon CloudWatch Logs.<br>- Cài đặt và cấu hình Unified CloudWatch Agent trên máy chủ EC2.<br>- Thu thập và đẩy các file nhật ký hệ thống (`/var/log/messages`) về CloudWatch Log Groups. | 25/08/2026 | 25/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Tìm hiểu dịch vụ kiểm toán AWS CloudTrail.<br>- Khởi tạo Trail ghi vết các sự kiện quản trị (Management Events) lưu về S3.<br>- Tra cứu lịch sử cuộc gọi API để rà soát bảo mật tài khoản. | 26/08/2026 | 26/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Tìm hiểu dịch vụ Amazon EventBridge và Amazon Simple Notification Service (SNS).<br>- Tạo SNS Topic và đăng ký nhận thông báo qua Email.<br>- Cấu hình EventBridge Rule bắt sự kiện thay đổi trạng thái máy chủ EC2 và gửi cảnh báo qua SNS. | 27/08/2026 | 27/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Tìm hiểu AWS Systems Manager (SSM) Parameter Store.<br>- Tạo và lưu trữ tham số cấu hình dạng String và mật khẩu mã hóa SecureString.<br>- Truy xuất tham số an toàn từ máy chủ EC2 thông qua AWS CLI và IAM Role. | 28/08/2026 | 28/08/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 4:
* Làm chủ hệ sinh thái giám sát AWS CloudWatch:
  * Theo dõi sát sao sức khỏe tài nguyên với Custom Metrics và Alarms.
  * Quản lý nhật ký ứng dụng tập trung tại CloudWatch Log Groups.
* Nắm vững kỹ năng kiểm toán an ninh với AWS CloudTrail:
  * Nhận biết chính xác ai đã thực hiện thao tác gì, khi nào và từ địa chỉ IP nào trên tài khoản AWS.
* Tự động hóa cảnh báo thời gian thực:
  * Xây dựng luồng thông báo tự động từ EventBridge tới Email quản trị viên qua Amazon SNS.
* Quản lý cấu hình an toàn tuyệt đối với SSM Parameter Store:
  * Mã hóa các thông tin nhạy cảm (database password, API token) bằng khóa AWS KMS.
  * Tách biệt hoàn toàn cấu hình khỏi mã nguồn ứng dụng.
