---
title: "Worklog Tuần 2"
date: 2026-08-10
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Mục tiêu tuần 2:
* Tìm hiểu bảo mật Amazon S3 và cấu hình Bucket Policy.
* Thực hành IAM Role và sử dụng AWS CLI.
* Tìm hiểu và sử dụng EC2 User Data để tự động hóa cài đặt máy chủ.
* Tìm hiểu dịch vụ cơ sở dữ liệu quan hệ Amazon RDS MySQL.
* Kết nối máy chủ EC2 với cơ sở dữ liệu Amazon RDS.
* Triển khai ứng dụng web hoàn chỉnh kết nối cơ sở dữ liệu trên AWS.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu chính sách bảo mật Amazon S3 Policy.<br>- Tạo S3 Bucket lưu trữ.<br>- Cấu hình Bucket Policy kiểm soát quyền truy cập.<br>- Kiểm tra và thử nghiệm truy cập công khai/riêng tư. | 10/08/2026 | 10/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Tìm hiểu cơ chế xác thực với IAM Role.<br>- Gán IAM Role cho EC2 instance.<br>- Kiểm tra quyền truy cập S3 từ EC2 thông qua AWS CLI. | 11/08/2026 | 11/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Tìm hiểu tính năng EC2 User Data.<br>- Viết bootstrap script tự động hóa trong User Data.<br>- Tự động cài đặt Web Server và PHP khi khởi động máy ảo.<br>- Kiểm tra ứng dụng khởi chạy tự động không cần can thiệp thủ công. | 12/08/2026 | 12/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Tìm hiểu dịch vụ cơ sở dữ liệu quan hệ Amazon RDS MySQL.<br>- Tạo DB Subnet Group trong phân vùng Private Subnet.<br>- Khởi tạo cơ sở dữ liệu Amazon RDS MySQL.<br>- Cấu hình Security Group cho phép kết nối cổng 3306 từ EC2. | 13/08/2026 | 13/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Kết nối máy chủ EC2 tới cơ sở dữ liệu Amazon RDS.<br>- Triển khai ứng dụng web động kết nối cơ sở dữ liệu.<br>- Kiểm tra kết nối, truy vấn dữ liệu và tính bền vững của ứng dụng. | 14/08/2026 | 14/08/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 2:
* Nắm vững bảo mật Amazon S3:
  * Tạo Bucket S3 bảo mật cao.
  * Viết chính sách Bucket Policy phân quyền chi tiết.
  * Kiểm soát việc chặn truy cập công khai ngoài ý muốn.
* Làm chủ IAM Role và AWS CLI:
  * Khởi tạo và gắn IAM Role vào máy ảo EC2.
  * Loại bỏ hoàn toàn Access Key/Secret Key khỏi mã nguồn.
  * Thao tác thành thạo lệnh `aws s3 ls`, `aws s3 cp` từ máy chủ.
* Tự động hóa máy chủ với EC2 User Data:
  * Tự động cài đặt và kích hoạt dịch vụ web ngay khi máy ảo khởi chạy.
* Triển khai cơ sở dữ liệu Amazon RDS MySQL:
  * Khởi tạo cơ sở dữ liệu trong phân vùng mạng riêng biệt an toàn.
  * Cấu hình tường lửa Security Group cô lập cơ sở dữ liệu với Internet.
* Kết nối hoàn chỉnh EC2 và Amazon RDS:
  * Ứng dụng web truy xuất dữ liệu mượt mà, lưu trữ và đọc dữ liệu ổn định.
