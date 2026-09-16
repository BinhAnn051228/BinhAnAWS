---
title: "Worklog Tuần 8"
date: 2026-09-15
weight: 8
chapter: false
pre: " <b> 1.8. </b> "
---

### Mục tiêu tuần 8:
* Thiết lập hệ thống giám sát và cảnh báo thời gian thực với CloudWatch, EventBridge và SNS.
* Thực hiện kiểm thử toàn diện 6 kịch bản an ninh DevSecOps thực tế.
* Thực hiện dọn dẹp tài nguyên đám mây, kiểm soát chi phí và nghiệm thu báo cáo tổng kết thực tập.

### Các công việc cần triển khai trong tuần này:
| Thứ | Công việc | Ngày bắt đầu | Ngày hoàn thành | Nguồn tài liệu |
| --- | --- | --- | --- | --- |
| 2 | - Cấu hình luật Amazon EventBridge bắt sự kiện trạng thái CodePipeline (FAILED / SUCCEEDED).<br>- Cấu hình target Amazon SNS gửi thông báo tức thời qua email cho đội ngũ kỹ sư khi pipeline gặp sự cố. | 21/09/2026 | 21/09/2026 | Dự án thực tập |
| 3 | - Cấu hình CloudWatch Alarms giám sát máy chủ EC2 và kiểm toán API qua CloudTrail.<br>- Thiết lập ngưỡng kiểm soát chi phí AWS Budgets đảm bảo chi phí phát sinh duy trì ở mức 0 USD. | 22/09/2026 | 22/09/2026 | Dự án thực tập |
| 4 | - Thực hiện thử nghiệm 3 kịch bản DevSecOps đầu tiên:<br>&emsp;+ Kịch bản 1: Luồng thành công chuẩn (Golden Path).<br>&emsp;+ Kịch bản 2: Chặn commit chứa thông tin bí mật với Gitleaks.<br>&emsp;+ Kịch bản 3: Chặn mã nguồn có lỗ hổng bảo mật với Bandit SAST.<br>- Thu thập log chi tiết và chụp ảnh bằng chứng bảo mật. | 23/09/2026 | 23/09/2026 | Dự án thực tập |
| 5 | - Thực hiện thử nghiệm 3 kịch bản DevSecOps tiếp theo:<br>&emsp;+ Kịch bản 4: Chặn cấu hình mở cổng 22 ra Internet (0.0.0.0/0) với Checkov.<br>&emsp;+ Kịch bản 5: Từ chối phê duyệt thủ công tại cổng Manual Approval.<br>&emsp;+ Kịch bản 6: Kiểm thử xác nhận sức khỏe dịch vụ sau khi deploy.<br>- Tổng hợp báo cáo đánh giá an ninh và đo lường các chỉ số hiệu quả. | 24/09/2026 | 24/09/2026 | Dự án thực tập |
| 6 | - Dọn dẹp toàn bộ tài nguyên đám mây đã khởi tạo bằng lệnh `terraform destroy`.<br>- Kiểm tra đối soát bảng kê chi phí AWS Cost Explorer đảm bảo không phát sinh chi phí ngoài ý muốn.<br>- Hoàn thiện hồ sơ báo cáo thực tập, slide thuyết trình và nghiệm thu kết quả với người hướng dẫn. | 25/09/2026 | 27/09/2026 | Báo cáo thực tập |

### Kết quả đạt được tuần 8:
* Hoàn thiện hệ sinh thái cảnh báo tự động, bảo đảm đội ngũ kỹ thuật luôn nắm bắt kịp thời trạng thái triển khai.
* Chứng minh hiệu quả vượt trội của chuỗi DevSecOps Pipeline qua 6 kịch bản kiểm thử giả lập sự cố an ninh thực tế.
* Dọn dẹp 100% tài nguyên thực hành an toàn, kiểm soát chi phí phát sinh ở mức tối ưu.
* Hoàn thành xuất sắc chương trình thực tập 8 tuần với tài liệu báo cáo kỹ thuật và trang web dự án hoàn chỉnh.
