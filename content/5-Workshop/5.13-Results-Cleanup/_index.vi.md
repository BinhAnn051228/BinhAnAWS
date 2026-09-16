---
title: "Đánh giá kết quả và dọn dẹp tài nguyên"
date: 2026-08-25
weight: 13
chapter: false
pre: " <b> 5.13. </b> "
---

# 5.13. Đánh giá kết quả và dọn dẹp tài nguyên

Chương này tổng kết các kết quả đạt được của dự án theo tiêu chí nghiệm thu và hướng dẫn chi tiết quy trình dọn dẹp (cleanup) toàn bộ tài nguyên đám mây AWS theo đúng thứ tự phụ thuộc nhằm tối ưu chi phí.

---

### Đánh giá nghiệm thu kết quả Workshop

Dự án hoàn thành đầy đủ các mục tiêu đề ra của Workshop AWS DevSecOps:
- **Tự động hóa toàn diện**: Chuỗi cung ứng AWS CodePipeline 7 giai đoạn hoạt động ổn định từ bước push code đến kiểm thử ứng dụng sau triển khai.
- **Bảo mật Shift-Left đa tầng**: Tích hợp đồng thời 4 scanner an ninh (Gitleaks, Bandit, Trivy, Checkov) hoạt động như các cổng chặn tự động (Security Gates).
- **Kiểm soát hạ tầng chặt chẽ**: Cơ chế sinh kế hoạch Terraform Plan và cổng phê duyệt thủ công (Manual Approval) giúp loại bỏ rủi ro sai lệch hạ tầng.
- **Khả năng quan sát đầy đủ**: Tích hợp CloudWatch Logs thu thập nhật ký tập trung, EventBridge và SNS gửi thông báo tức thời, cùng CloudTrail kiểm toán an ninh.
- **Kiểm thử tự động sau triển khai**: PostDeployVerification smoke test tự động xác thực trạng thái máy chủ và tính sẵn sàng của ứng dụng.

---

### Quy trình dọn dẹp tài nguyên theo đúng thứ tự phụ thuộc

Để tránh tình trạng lỗi phụ thuộc (dependency locking) khi xóa tài nguyên, việc hủy hạ tầng cần tuân thủ nghiêm ngặt theo 3 bước sau:

#### Bước 1: Hủy tài nguyên hạ tầng ứng dụng (Workload Layer)

Hạ tầng ứng dụng (máy chủ EC2, mạng VPC, Subnet, Route Table, Security Group) cần được xóa bỏ đầu tiên:

```bash
cd ~/fcaj-aws-devsecops/workload

# Khởi tạo backend và chạy destroy
terraform init
terraform destroy -auto-approve
```

#### Bước 2: Hủy tài nguyên nền tảng CI/CD (Platform Layer)

Sau khi workload đã được xóa hoàn toàn, tiến hành hủy chuỗi CodePipeline, các CodeBuild projects, IAM roles, EventBridge rules và SNS topic:

```bash
cd ~/fcaj-aws-devsecops/platform

# Khởi tạo và hủy tầng platform
terraform init
terraform destroy -auto-approve
```

#### Bước 3: Dọn dẹp S3 Bucket và Parameter Store (Bootstrap Layer)

Các S3 bucket chứa state và artifact có cấu hình bật versioning, do đó cần dọn sạch các đối tượng trước khi thực hiện destroy:

```bash
# Xóa sạch toàn bộ object và version trong các S3 bucket
aws s3 rm "s3://${TF_STATE_BUCKET}" --recursive
aws s3 rm "s3://${ARTIFACT_BUCKET}" --recursive

# Hủy tầng bootstrap
cd ~/fcaj-aws-devsecops/bootstrap
terraform init
terraform destroy -auto-approve
```

---

### Kiểm tra tài nguyên tồn dư và Xác nhận chi phí

Sau khi hoàn tất quá trình dọn dẹp, truy cập AWS Management Console hoặc sử dụng AWS CLI để đảm bảo không còn tài nguyên chạy ngầm phát sinh chi phí:

```bash
# Kiểm tra không còn máy chủ EC2 nào ở trạng thái running
aws ec2 describe-instances   --filters "Name=instance-state-name,Values=running"   --query "Reservations[].Instances[].InstanceId"   --output text

# Kiểm tra các S3 bucket liên quan đã bị xóa
aws s3 ls | grep fcaj || true
```

> [!TIP]
> Việc kiểm tra lại trang AWS Billing Console sau 24 giờ giúp xác nhận tài khoản không còn bất kỳ chi phí phát sinh nào sau khi kết thúc Workshop.
