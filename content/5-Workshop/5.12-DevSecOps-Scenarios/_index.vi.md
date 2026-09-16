---
title: "Kịch bản kiểm thử bảo mật DevSecOps"
date: 2026-08-25
weight: 12
chapter: false
pre: " <b> 5.12. </b> "
---

# 5.12. Kịch bản kiểm thử bảo mật DevSecOps

Chương này chứng minh hiệu quả thực tế của các cổng kiểm soát an ninh (**Security Gates**) thông qua các kịch bản kiểm thử: triển khai đường cơ sở sạch, tự động phát hiện và ngăn chặn cấu hình SSH không an toàn, rò rỉ secret, thư viện có lỗ hổng CVE và cơ chế từ chối phê duyệt hạ tầng.

---

### Kịch bản 1: Triển khai thành công trên đường cơ sở sạch (Baseline Succeeded)

- **Mục tiêu**: Xác nhận toàn bộ chuỗi CI/CD hoạt động trơn tru khi mã nguồn và hạ tầng tuân thủ đầy đủ các chuẩn an ninh.
- **Kết quả**: Tất cả 7 giai đoạn từ Source đến PostDeployVerification đều chuyển sang màu xanh (`SUCCEEDED`). Ứng dụng web được cập nhật thành công và phản hồi mã `200 OK`.

---

### Kịch bản 2: Checkov chặn cấu hình mở cổng SSH nguy hiểm

- **Tình huống**: Thêm cấu hình Security Group mở cổng SSH `22` cho toàn mạng Internet (`0.0.0.0/0`) từ tệp mẫu `demo/fixtures/public_ssh.tf.example`.
- **Thực thi**:
  ```bash
  cp demo/fixtures/public_ssh.tf.example workload/public_ssh.tf
  git add workload/public_ssh.tf && git commit -m "test: simulate public ssh vulnerability" && git push
  ```
- **Kết quả**: Checkov phát hiện vi phạm quy chuẩn an ninh `CKV_AWS_24`, trả về mã lỗi và **chặn đứng pipeline tại stage SecurityScan**. Giai đoạn Terraform Plan không được phép diễn ra.

---

### Kịch bản 3: Gitleaks chặn rò rỉ khóa bí mật (Secret Leakage)

- **Tình huống**: Thêm một đoạn mã chứa chuỗi giả lập AWS Access Key vào file `app/leak.py`.
- **Thực thi**:
  ```bash
  echo 'AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLEEXAMPLE"' > app/leak.py
  git add app/leak.py && git commit -m "test: simulate credential leak" && git push
  ```
- **Kết quả**: Gitleaks nhận diện chuỗi ký tự khớp với định dạng AWS Access Key, ẩn thông tin nhạy cảm trong log và **dừng pipeline ngay lập tức**.

---

### Kịch bản 4: Trivy chặn thư viện có lỗ hổng bảo mật nghiêm trọng

- **Tình huống**: Thêm một thư viện Python phiên bản cũ chứa lỗ hổng CVE mức `HIGH/CRITICAL` vào `app/requirements.txt`.
- **Thực thi**:
  ```bash
  cat demo/fixtures/requirements-vulnerable.txt >> app/requirements.txt
  git add app/requirements.txt && git commit -m "test: simulate vulnerable dependency" && git push
  ```
- **Kết quả**: Trivy quét cơ sở dữ liệu lỗ hổng quốc tế, phát hiện CVE nghiêm trọng và trả về mã lỗi `1`, làm thất bại stage SecurityScan.

---

### Kịch bản 5: Từ chối kế hoạch thay đổi tại Manual Approval

- **Tình huống**: Pipeline vượt qua các cổng bảo mật tự động và chuyển sang bước chờ phê duyệt. Quản trị viên kiểm tra bản kế hoạch `plan.txt`, phát hiện thay đổi hạ tầng không mong muốn.
- **Hành động**: Quản trị viên chọn **Reject** trong bảng điều khiển AWS CodePipeline kèm theo lý do từ chối.
- **Kết quả**: Pipeline dừng lại tại bước Manual Approval, giai đoạn `TerraformApply` không được kích hoạt, bảo vệ hạ tầng sản xuất khỏi các thay đổi trái phép.

---

### Đánh giá hiệu quả các cổng an ninh (Security Gates)

Thông qua các kịch bản thử nghiệm thực tế, hệ thống DevSecOps đã chứng minh khả năng phát hiện sớm và ngăn chặn tự động (Shift-Left) các rủi ro an ninh phổ biến: rò rỉ thông tin đăng nhập, lỗ hổng thư viện bên thứ ba, sai cấu hình hạ tầng đám mây và rủi ro triển khai hạ tầng không kiểm soát.
