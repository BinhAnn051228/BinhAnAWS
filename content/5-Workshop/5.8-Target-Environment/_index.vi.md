---
title: "Môi trường triển khai mục tiêu"
date: 2026-08-25
weight: 8
chapter: false
pre: " <b> 5.8. </b> "
---

# 5.8. Môi trường triển khai mục tiêu

Chương này trình bày chi tiết kiến trúc hạ tầng Workload được quản lý tự động bằng Terraform, bao gồm mạng **Amazon VPC**, nhóm bảo mật (**Security Group**), máy chủ **Amazon EC2** và quy trình bootstrap ứng dụng web demo.

---

### Kiến trúc mạng và Kiểm soát truy cập hạ tầng

- **Mạng Amazon VPC và Phân vùng Subnet**: Khởi tạo VPC độc lập với dải địa chỉ riêng biệt, gắn kết Internet Gateway và cấu hình Route Table liên kết Public Subnet để định tuyến lưu lượng mạng ra ngoài Internet.
- **Security Group kiểm soát luồng dữ liệu**: Thiết lập Security Group cho Web Server, chỉ cho phép lưu lượng HTTP (port 80) từ bên ngoài phục vụ kiểm thử và truy cập ứng dụng. Cổng SSH (port 22) được đóng hoàn toàn để tuân thủ quy chuẩn an ninh. Default Security Group bị vô hiệu hóa toàn bộ inbound/outbound rules.

---

### Khởi tạo máy chủ EC2 và Tự động triển khai ứng dụng Web

1. **Cấu hình máy chủ Amazon EC2**:
   Máy chủ sử dụng hệ điều hành Amazon Linux 2023, loại instance `t3.micro` và được gắn IAM Instance Profile để cho phép quản trị an toàn thông qua AWS Systems Manager (SSM) Session Manager thay vì SSH.

2. **Quy trình Bootstrap tự động (`user_data.sh.tftpl`)**:
   Khi máy chủ được tạo, script user data tự động cài đặt runtime Python 3.11, tải mã nguồn Flask app, cài đặt thư viện phụ thuộc và đăng ký dịch vụ `systemd` tự khởi chạy:

```bash
#!/bin/bash
set -euo pipefail

# Cập nhật gói phần mềm và cài đặt Python
dnf update -y
dnf install -y python3.11 python3.11-pip git

# Tạo người dùng và thư mục ứng dụng
useradd -m -s /bin/bash appuser || true
mkdir -p /opt/app && chown appuser:appuser /opt/app

# Cài đặt mã nguồn và thư viện
cat <<'EOF' > /opt/app/app.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "FCAJ AWS DevSecOps Workshop - Demo Application Running"

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "demo-web-app"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
EOF

# Cấu hình systemd service tự khởi động cùng hệ thống
cat <<'EOF' > /etc/systemd/system/demo-app.service
[Unit]
Description=FCAJ Demo Web Application
After=network.target

[Service]
User=root
WorkingDirectory=/opt/app
ExecStart=/usr/bin/python3.11 /opt/app/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now demo-app
```

---

### Kiểm tra kết nối và Truy cập ứng dụng

Sau khi hạ tầng được triển khai hoàn tất, kiểm tra khả năng truy cập ứng dụng thông qua địa chỉ IP công khai hoặc DNS của EC2:

```bash
# Lấy Public IP từ output của workload
EC2_IP=$(terraform -chdir=workload output -raw ec2_public_ip)
echo "Kiểm tra truy cập EC2 Web Server tại: http://${EC2_IP}/"

# Gửi HTTP request kiểm tra
curl -I "http://${EC2_IP}/"
curl -s "http://${EC2_IP}/health"
```

> [!TIP]
> Ứng dụng trả về mã trạng thái HTTP `200 OK` tại endpoint `/health`, xác nhận máy chủ EC2 và dịch vụ web Flask đã hoạt động ổn định và sẵn sàng phục vụ lưu lượng.
