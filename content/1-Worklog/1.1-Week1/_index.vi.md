---
title: "Worklog Tuần 1"
date: 2026-08-03
weight: 1
chapter: false
pre: " <b> 1.1. </b> "
---

### Mục tiêu tuần 1:
* Tham gia định hướng thực tập, tìm hiểu quy trình làm việc và các khái niệm cơ bản về AWS Cloud.
* Học và thực hành dịch vụ quản lý danh tính và truy cập (AWS IAM).
* Triển khai máy chủ ảo Amazon EC2 và cấu hình tường lửa Security Group.
* Thiết lập mạng ảo Amazon VPC (Public/Private Subnets, Internet Gateway, Route Tables).
* Khởi tạo lưu trữ đám mây Amazon S3 và lưu trữ trang web tĩnh.
* Cấu hình IAM Role cho EC2 và thao tác với AWS CLI.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tham gia định hướng thực tập.<br>- Tìm hiểu kiến thức cơ bản về AWS Cloud.<br>- Tạo IAM Group và IAM User.<br>- Gán chính sách AdministratorAccess và kiểm tra đăng nhập IAM User. | 03/08/2026 | 03/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Tìm hiểu dịch vụ Amazon EC2.<br>- Khởi tạo máy ảo Amazon Linux EC2 instance.<br>- Cấu hình Security Group.<br>- Kết nối tới máy chủ qua SSH.<br>- Cài đặt Apache Web Server và triển khai trang web đơn giản. | 04/08/2026 | 04/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Tìm hiểu dịch vụ Amazon VPC.<br>- Tạo một VPC mới.<br>- Tạo Public Subnet và Private Subnet.<br>- Gắn Internet Gateway vào VPC.<br>- Cấu hình bảng định tuyến Route Tables. | 05/08/2026 | 05/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Tìm hiểu dịch vụ Amazon S3.<br>- Tạo S3 Bucket.<br>- Tải lên các tệp tin của trang web.<br>- Cấu hình Bucket Policy.<br>- Bật tính năng Static Website Hosting. | 06/08/2026 | 06/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Tìm hiểu IAM Role và công cụ AWS CLI.<br>- Tạo IAM Role cho EC2 instance.<br>- Gán quyền AmazonS3ReadOnlyAccess cho Role.<br>- Kết nối EC2 qua SSH.<br>- Thực hành các câu lệnh AWS CLI tương tác với S3. | 07/08/2026 | 07/08/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 1:
* Nắm vững kiến thức cơ bản về AWS Cloud và quy trình thực tập.
* Làm chủ dịch vụ AWS IAM:
  * Tạo IAM Groups và IAM Users.
  * Phân quyền với chính sách IAM Policy.
  * Đăng nhập và xác thực an toàn bằng tài khoản IAM User.
* Triển khai thành công máy chủ Amazon EC2:
  * Cấu hình tường lửa Security Groups.
  * Kết nối quản trị từ xa qua SSH.
  * Cài đặt Apache Web Server.
  * Triển khai trang web đơn giản hoạt động ổn định.
* Làm chủ kiến trúc mạng Amazon VPC:
  * Tạo VPC riêng biệt.
  * Cấu hình phân vùng Public Subnet và Private Subnet.
  * Gắn Internet Gateway để thông mạng ra Internet.
  * Cấu hình bảng định tuyến Route Tables và gán Public IPv4.
