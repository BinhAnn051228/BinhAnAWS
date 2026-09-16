---
title: "Giám sát, nhật ký và cảnh báo"
date: 2026-08-25
weight: 10
chapter: false
pre: " <b> 5.10. </b> "
---

# 5.10. Giám sát, nhật ký và cảnh báo

Chương này hướng dẫn thiết lập hệ thống quan sát toàn diện cho chuỗi DevSecOps, kết hợp giữa **Amazon CloudWatch**, **Amazon EventBridge**, **Amazon SNS**, **AWS CloudTrail** và **AWS Budgets** nhằm thu thập nhật ký thực thi, gửi thông báo tức thời và kiểm soát chi phí hoạt động.

---

### Thu thập nhật ký tập trung và Giám sát tiến độ Pipeline

- **Amazon CloudWatch Logs**: Tự động thu thập và lưu trữ toàn bộ build log chi tiết từ các dự án CodeBuild (`validate-security`, `terraform-plan`, `terraform-apply`). Quản trị viên có thể theo dõi tiến độ chi tiết của các scanner hoặc phân tích log lỗi Terraform ngay trên CloudWatch Console.
- **Theo dõi tiến độ CodePipeline**: Bảng điều khiển CodePipeline cung cấp góc nhìn trực quan theo thời gian thực về trạng thái của từng giai đoạn trong chuỗi cung ứng.

---

### Cảnh báo tự động qua Amazon EventBridge và SNS

1. **Amazon EventBridge Rule**:
   Hệ thống cấu hình rule tự động bắt các sự kiện thay đổi trạng thái của CodePipeline (đặc biệt khi pipeline chuyển sang trạng thái `FAILED` hoặc `SUCCEEDED`):
   ```json
   {
     "source": ["aws.codepipeline"],
     "detail-type": ["CodePipeline Pipeline Execution State Change"],
     "detail": {
       "pipeline": ["fcaj-devsecops-pipeline"],
       "state": ["FAILED", "SUCCEEDED"]
     }
   }
   ```

2. **Amazon SNS Topic và Email Notification**:
   EventBridge chuyển tiếp thông điệp sự kiện tới SNS Topic `fcaj-devsecops-notifications`, từ đó tự động gửi email thông báo tới danh sách email kỹ sư phụ trách:
   ```bash
   # Kiểm tra danh sách người nhận email đã được xác nhận (Confirmed)
   aws sns list-subscriptions-by-topic --topic-arn "$SNS_TOPIC_ARN"
   ```

---

### Ghi vết kiểm toán với CloudTrail và Quản trị chi phí với AWS Budgets

- **AWS CloudTrail**: Toàn bộ các API calls tác động lên tài nguyên AWS (IAM, S3, CodePipeline, EC2) đều được ghi nhận vào CloudTrail, đáp ứng yêu cầu tuân thủ an ninh và phục vụ truy vết điều tra sự cố.
- **AWS Budgets**: Khởi tạo ngân sách cảnh báo chi phí định kỳ cho môi trường Workshop, tự động kích hoạt email cảnh báo khi chi phí thực tế hoặc chi phí dự báo vượt ngưỡng quy định.
