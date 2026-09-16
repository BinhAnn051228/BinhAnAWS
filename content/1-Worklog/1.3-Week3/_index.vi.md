---
title: "Worklog Tuần 3"
date: 2026-08-17
weight: 3
chapter: false
pre: " <b> 1.3. </b> "
---

### Mục tiêu tuần 3:
* Tìm hiểu an toàn mạng trên AWS (AWS Network Security).
* Thực hành cấu hình tường lửa Security Groups.
* Tìm hiểu danh sách kiểm soát truy cập mạng Network ACL (NACL).
* Tìm hiểu và kích hoạt nhật ký lưu lượng mạng Amazon VPC Flow Logs.
* Hiểu về hệ thống phân giải tên miền DNS và Amazon Route 53.
* Tìm hiểu và thiết lập kết nối liên kết mạng VPC Peering.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Tìm hiểu Security Groups.<br>- Nghiên cứu các luật Inbound (đến) và Outbound (đi).<br>- Tìm hiểu các giao thức mạng thông dụng (TCP, UDP, ICMP). | 17/08/2026 | 17/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Thực hành cấu hình Security Groups.<br>- Tạo mới và chỉnh sửa các luật trong Security Group.<br>- Kiểm tra thử nghiệm truy cập qua giao thức SSH và HTTP. | 18/08/2026 | 18/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Tìm hiểu Network ACL (NACL).<br>- So sánh sự khác nhau giữa NACL (stateless) và Security Groups (stateful).<br>- Cấu hình các luật Inbound và Outbound bảo vệ cấp độ Subnet. | 19/08/2026 | 19/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Tìm hiểu dịch vụ Amazon VPC Flow Logs.<br>- Kích hoạt VPC Flow Logs đẩy nhật ký mạng về CloudWatch Logs.<br>- Phân tích log lưu lượng để nhận diện gói tin ACCEPT và REJECT. | 20/08/2026 | 20/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 6 | - Tìm hiểu DNS và dịch vụ Amazon Route 53.<br>- Nghiên cứu mô hình kết nối liên mạng VPC Peering.<br>- Thiết lập kết nối Peering giữa 2 VPC và kiểm tra định tuyến. | 21/08/2026 | 21/08/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Kết quả đạt được tuần 3:
* Nắm vững kiến trúc an ninh mạng đa tầng trên AWS.
* Làm chủ Security Groups:
  * Kiểm soát luồng truy cập theo cơ chế Stateful ở tầng máy ảo.
  * Giới hạn dải địa chỉ IP và cổng dịch vụ theo nguyên tắc an toàn tối thiểu.
* Làm chủ Network ACLs (NACL):
  * Cấu hình bộ lọc Stateless kiểm soát gói tin ở cấp độ Subnet.
  * Phân biệt rõ sự khác nhau và cách phối hợp giữa SG và NACL.
* Phân tích an ninh mạng với Amazon VPC Flow Logs:
  * Theo dõi toàn diện các luồng dữ liệu truyền vào và ra khỏi giao diện mạng ENI.
  * Dễ dàng phát hiện các hành vi quét cổng hoặc truy cập trái phép.
* Hiểu rõ cơ chế định tuyến tên miền với Route 53 và kết nối liên VPC qua VPC Peering.
