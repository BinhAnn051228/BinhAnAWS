---
title: "Xây dựng Validate, Test & Shift-Left Security"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# 5.5. Xây dựng Validate, Test & Shift-Left Security

Chương này hướng dẫn xây dựng các tầng phòng thủ Shift-Left Security tự động với AWS CodeBuild: kiểm tra định dạng cú pháp (linting), kiểm thử đơn vị (unit testing) và tích hợp đồng thời 4 scanner bảo mật gồm **Gitleaks** (Secret), **Bandit** (SAST), **Trivy** (SCA/CVE) và **Checkov** (IaC).

---

### Cấu hình dự án AWS CodeBuild Validate & Test

Dự án CodeBuild `validate-security` được khởi tạo dựa trên image chuẩn `standard:7.0`, kích thước tính toán `BUILD_GENERAL1_SMALL`, nhận mã nguồn từ CodePipeline và gắn vai trò `ScanBuildRole`. Để tối ưu hóa tài nguyên và chi phí, cùng một dự án CodeBuild được tái sử dụng cho cả hai giai đoạn kiểm thử chất lượng và quét an ninh thông qua biến môi trường `RUN_MODE`.

---

![AWS CodeBuild Console - Danh sách các CodeBuild Projects phục vụ Validate và Security Gates](/images/5-Workshop/5.5-Validate-Security-Gates/image.png)

*AWS CodeBuild Console - Danh sách các CodeBuild Projects phục vụ Validate và Security Gates*

---

### Kiểm tra định dạng HCL và tính hợp lệ của Terraform

Ở chế độ `RUN_MODE=validate`, hệ thống tiến hành xác thực cú pháp và logic cơ bản trước khi chạy các công cụ quét chuyên sâu:

```bash
RUN_MODE=validate
terraform fmt -check -recursive bootstrap platform workload
terraform -chdir="${WORKLOAD_DIR}" init -backend=false -input=false
terraform -chdir="${WORKLOAD_DIR}" validate
python -m compileall -q app
pytest -q app/tests
```

Giai đoạn `ValidateTest` yêu cầu toàn bộ các bước kiểm tra định dạng Terraform, biên dịch mã nguồn Python và unit test bằng Pytest phải hoàn thành không có lỗi trước khi được phép tiến vào cổng an ninh.

#### Chạy ValidateTest trước khi push mã nguồn

```bash
cd ~/fcaj-aws-devsecops
terraform fmt -check -recursive bootstrap platform workload
terraform -chdir=workload init -backend=false -input=false
terraform -chdir=workload validate
python3 -m compileall -q app
python3 -m pip install --user -r app/requirements.txt pytest
python3 -m pytest -q app/tests
```

> [!NOTE]
> Nếu Pytest báo lỗi không tìm thấy `test_client`, đảm bảo file kiểm thử `app/tests/test_app.py` import đúng instance Flask thông qua câu lệnh: `from app.app import app`.

---

### Tích hợp 4 lớp bảo mật Shift-Left Security

Khi chuyển sang chế độ `RUN_MODE=security`, CodeBuild tuần tự thực thi 4 công cụ kiểm tra độc lập:

1. **Quét phát hiện lộ lọt bí mật với Gitleaks**:
   Gitleaks quét toàn bộ thư mục mã nguồn theo cấu hình `.gitleaks.toml` để phát hiện các API key, mật khẩu hoặc AWS credentials bị vô tình đưa vào commit:
   ```bash
   gitleaks dir . --config .gitleaks.toml --redact --no-banner
   ```
   Kết quả quét được tự động ẩn bớt (redact) để tránh hiển thị thông tin nhạy cảm trong build log.

2. **Phân tích tĩnh mã nguồn ứng dụng với Bandit (SAST)**:
   Bandit quét mã nguồn Python trong thư mục `app`, tập trung kiểm tra các lỗ hổng tiềm ẩn có mức độ nghiêm trọng và độ tin cậy cao:
   ```bash
   bandit -r app -lll -iii
   ```

3. **Quét lỗ hổng thư viện phụ thuộc với Trivy (SCA / CVE)**:
   Trivy kiểm tra danh mục thư viện trong `app/requirements.txt` đối chiếu với cơ sở dữ liệu CVE quốc tế, tự động kích hoạt mã lỗi nếu phát hiện lỗ hổng mức `HIGH` hoặc `CRITICAL`:
   ```bash
   trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
   ```

4. **Quét an toàn hạ tầng mã hóa với Checkov (IaC Scan)**:
   Checkov phân tích các tệp Terraform trong thư mục `workload` nhằm phát hiện sai lệch cấu hình an toàn trên AWS:
   ```bash
   checkov -d "${WORKLOAD_DIR}" --framework terraform --compact
   ```
   Các ngoại lệ thử nghiệm đã được document trực tiếp trong mã nguồn cho VPC Flow Logs (`CKV2_AWS_11`), Public Subnet (`CKV_AWS_130`), HTTP port 80 (`CKV_AWS_260`) và Public IP (`CKV_AWS_88`).

#### Lệnh kiểm tra thủ công toàn bộ lớp an ninh

```bash
cd ~/fcaj-aws-devsecops
gitleaks dir . --config .gitleaks.toml --redact --no-banner
bandit -r app -lll -iii
trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
checkov -d workload --framework terraform --compact
```

---

### Thiết lập cơ chế chặn Security Gate tự động

Cổng kiểm soát an ninh (Security Gate) được thiết lập chặt chẽ trong chuỗi cung ứng: giai đoạn `SecurityScan` bắt buộc phải trả về trạng thái thành công thì giai đoạn `TerraformPlan` mới được kích hoạt. Tệp buildspec kích hoạt tùy chọn `set -euo pipefail`, đảm bảo nếu bất kỳ scanner nào phát hiện lỗi (exit code khác 0), toàn bộ pipeline sẽ bị chặn đứng ngay lập tức để bảo vệ hạ tầng.
