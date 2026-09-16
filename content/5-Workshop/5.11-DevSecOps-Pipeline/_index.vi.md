---
title: "Hoàn thiện AWS DevSecOps Pipeline"
date: 2026-08-25
weight: 11
chapter: false
pre: " <b> 5.11. </b> "
---

# 5.11. Hoàn thiện AWS DevSecOps Pipeline

Chương này tổng hợp toàn bộ 7 giai đoạn của chuỗi cung ứng **AWS CodePipeline** thành một quy trình tự động hóa khép kín và hướng dẫn các quy tắc vận hành commit hàng ngày.

---

### Tổng quan luồng thực thi 7 giai đoạn trong Pipeline

Mỗi khi có commit mới được đẩy lên nhánh `main` trên GitHub, chuỗi CodePipeline tự động kích hoạt và thực thi tuần tự qua 7 giai đoạn:

```text
Source ──> ValidateTest ──> SecurityScan ──> TerraformPlan ──> ManualApproval ──> TerraformApply ──> PostDeployVerification
```

1. **Source Stage**: Lắng nghe sự kiện từ GitHub thông qua AWS CodeConnections, trích xuất mã nguồn mới nhất và đóng gói thành artifact `SourceOutput`.
2. **Validate & Test Stage**: Thực thi dự án CodeBuild với `RUN_MODE=validate` để kiểm tra định dạng Terraform (`fmt`, `validate`), kiểm tra biên dịch Python và chạy kiểm thử đơn vị (`pytest`).
3. **Security Scan Stage (Security Gate)**: Chạy đồng thời 4 scanner an ninh: Gitleaks (Secret), Bandit (SAST), Trivy (SCA/CVE) và Checkov (IaC). Nếu phát hiện lỗi hoặc vi phạm chính sách bảo mật, pipeline dừng ngay lập tức.
4. **Terraform Plan Stage**: Thực thi `terraform plan` cho workload, sinh tệp nhị phân `tfplan` và bản tóm tắt `plan.txt`, lưu trữ thành artifact `PlanOutput`.
5. **Manual Approval Stage**: Dừng pipeline và gửi email cảnh báo cho reviewer. Quản trị viên kiểm tra bản kế hoạch hạ tầng trước khi chọn **Approve** hoặc **Reject**.
6. **Terraform Apply Stage**: Sử dụng đúng tệp kế hoạch nhị phân đã duyệt để thực hiện `terraform apply`, đảm bảo tính toàn vẹn tuyệt đối cho hạ tầng.
7. **Post-Deploy Verification Stage**: Chạy smoke test tự động kiểm tra trạng thái máy chủ EC2 và xác thực endpoint `/health` phản hồi mã HTTP 200 OK.

---

### Quy tắc vận hành và Quy trình commit hằng ngày

Pipeline được tạo cố định một lần ở tầng nền tảng (Platform Layer). Mọi thay đổi đối với ứng dụng hoặc cấu hình workload được thực hiện thông qua quy trình Git tiêu chuẩn:

```bash
cd ~/fcaj-aws-devsecops
git add -A
git status
git commit -m "feat: update application or workload"
git push origin main
```

> [!IMPORTANT]
> - Không cần chạy lại `terraform apply` cho tầng platform khi chỉ thay đổi mã nguồn trong `app/` hoặc `workload/`.
> - Tránh đẩy nhiều commit liên tiếp trong lúc execution trước đang ở giai đoạn `TerraformApply` để tránh lỗi xung đột khóa trạng thái (state lock).
> - Nếu xảy ra lỗi trước giai đoạn `TerraformApply`, pipeline sẽ dừng an toàn và toàn bộ hạ tầng đang hoạt động được bảo toàn nguyên vẹn.
