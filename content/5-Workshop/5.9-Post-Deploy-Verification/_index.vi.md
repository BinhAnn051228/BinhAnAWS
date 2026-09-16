---
title: "Kiểm thử và xác thực sau triển khai"
date: 2026-08-25
weight: 9
chapter: false
pre: " <b> 5.9. </b> "
---

# 5.9. Kiểm thử và xác thực sau triển khai

Chương này hướng dẫn cấu hình giai đoạn kiểm thử tự động **PostDeployVerification (Smoke Test)** sau khi hoàn tất `TerraformApply`, giúp đảm bảo máy chủ EC2 đã khởi động xong và ứng dụng phản hồi chính xác trước khi kết thúc pipeline.

---

### Cơ chế kiểm thử tự động Smoke Test

Giai đoạn Smoke Test được thực thi bởi AWS CodeBuild sử dụng file cấu hình `cicd/buildspec-apply.yml` với chế độ `RUN_MODE=smoke`:

1. **Lấy địa chỉ máy chủ**: Lấy địa chỉ IP công khai hoặc Public DNS của EC2 từ Terraform output của workload.
2. **Kiểm tra trạng thái máy chủ EC2**: Xác nhận máy chủ đang ở trạng thái `running` và vượt qua các bài kiểm tra hệ thống (`system status checks`).
3. **Kiểm tra HTTP Health Endpoint**: Thực hiện gửi HTTP request liên tục (kèm cơ chế retry tự động trong 2-3 phút) tới đường dẫn `/health` để chờ máy chủ hoàn tất chạy script bootstrap.
4. **Xác thực mã phản hồi HTTP 200 OK**: Pipeline chỉ được coi là thành công (`SUCCEEDED`) khi nhận được phản hồi HTTP 200 kèm nội dung JSON hợp lệ.

---

### Xử lý sự cố khi Smoke Test thất bại

Trong trường hợp Smoke Test không nhận được mã phản hồi 200 trong thời gian chờ (timeout), giai đoạn này sẽ dừng lại ở trạng thái `FAILED`. Để điều tra nguyên nhân mà không cần mở cổng SSH, quản trị viên sử dụng AWS Systems Manager Session Manager để kết nối an toàn vào máy chủ:

```bash
# Lấy Instance ID của EC2 demo đang chạy
INSTANCE_ID=$(aws ec2 describe-instances   --filters "Name=tag:Name,Values=*fcaj*" "Name=instance-state-name,Values=running"   --query "Reservations[].Instances[].InstanceId"   --output text)

# Kết nối trực tiếp vào máy chủ thông qua SSM
aws ssm start-session --target "$INSTANCE_ID"

# Khi vào trong terminal của máy chủ EC2, kiểm tra nhật ký:
sudo systemctl status demo-app
cat /var/log/user-data.log
sudo journalctl -u demo-app -n 50 --no-pager
```

> [!NOTE]
> Khi Smoke Test thất bại, hạ tầng AWS đã được tạo nhưng dịch vụ ứng dụng có thể gặp lỗi cú pháp Python hoặc thiếu thư viện. Việc kiểm tra `user-data.log` giúp nhanh chóng cô lập nguyên nhân và sửa đổi mã nguồn.
