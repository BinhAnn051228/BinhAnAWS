import os
from pathlib import Path

BASE_DIR = Path(r"c:\Users\ASUS\Desktop\Năm cuối\Prj thực tập\BinhAnAWS")
CONTENT_DIR = BASE_DIR / "content" / "5-Workshop"

def write_page(folder_name, weight, num, title_vi, title_en, body_vi, body_en):
    target_dir = CONTENT_DIR / folder_name
    os.makedirs(target_dir, exist_ok=True)
    
    # Clean any leftover subdirectories if present
    for item in target_dir.iterdir():
        if item.is_dir():
            import shutil
            shutil.rmtree(item)

    vi_path = target_dir / "_index.vi.md"
    en_path = target_dir / "_index.md"

    vi_content = f"""---
title: "{title_vi}"
date: 2026-08-25
weight: {weight}
chapter: false
pre: " <b> {num}. </b> "
---

# {num}. {title_vi}

{body_vi.strip()}
"""

    en_content = f"""---
title: "{title_en}"
date: 2026-08-25
weight: {weight}
chapter: false
pre: " <b> {num}. </b> "
---

# {num}. {title_en}

{body_en.strip()}
"""

    vi_path.write_text(vi_content, encoding="utf-8")
    en_path.write_text(en_content, encoding="utf-8")
    print(f"Generated unified chapter {num}: {folder_name}")

def generate_all():
    # 5.5
    write_page(
        "5.5-Validate-Security-Gates", 5, "5.5",
        "Xây dựng Validate, Test & Shift-Left Security",
        "Build Validate, Test & Shift-Left Security",
        """Chương này hướng dẫn xây dựng các tầng phòng thủ Shift-Left Security tự động với AWS CodeBuild: kiểm tra định dạng cú pháp (linting), kiểm thử đơn vị (unit testing) và tích hợp đồng thời 4 scanner bảo mật gồm **Gitleaks** (Secret), **Bandit** (SAST), **Trivy** (SCA/CVE) và **Checkov** (IaC).

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
""",
        """This chapter guides you through establishing automated Shift-Left security guardrails using AWS CodeBuild: code formatting and linting, unit testing, and integrating 4 specialized security scanners: **Gitleaks** (Secret Detection), **Bandit** (SAST), **Trivy** (SCA/CVE), and **Checkov** (IaC).

---

### AWS CodeBuild Validate & Test Project Configuration

The `validate-security` CodeBuild project runs on the standard `standard:7.0` container image with compute size `BUILD_GENERAL1_SMALL`, consumes artifacts from CodePipeline, and assumes the `ScanBuildRole`. To optimize resource efficiency and cost, the same CodeBuild project is dynamically driven by the `RUN_MODE` environment variable across both validation and security scanning phases.

---

![AWS CodeBuild Console - CodeBuild Projects list supporting Validate and Security Gates](/images/5-Workshop/5.5-Validate-Security-Gates/image.png)

*AWS CodeBuild Console - CodeBuild Projects list supporting Validate and Security Gates*

---

### Terraform Format & Syntax Validation

Under `RUN_MODE=validate`, the pipeline validates formatting, syntax integrity, and baseline application logic:

```bash
RUN_MODE=validate
terraform fmt -check -recursive bootstrap platform workload
terraform -chdir="${WORKLOAD_DIR}" init -backend=false -input=false
terraform -chdir="${WORKLOAD_DIR}" validate
python -m compileall -q app
pytest -q app/tests
```

The `ValidateTest` stage requires all Terraform formatting, Python compilation, and Pytest test suites to succeed without error before advancing to security scans.

#### Run ValidateTest Locally Before Push

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
> If Pytest reports that `test_client` cannot be found, ensure `app/tests/test_app.py` correctly imports the Flask instance: `from app.app import app`.

---

### Multi-Layer Shift-Left Security Scanners

Under `RUN_MODE=security`, CodeBuild sequentially runs four independent verification scanners:

1. **Secret Scanning with Gitleaks**:
   Gitleaks inspects the repository directory against `.gitleaks.toml` rules to catch exposed secrets, tokens, or AWS credentials:
   ```bash
   gitleaks dir . --config .gitleaks.toml --redact --no-banner
   ```

2. **Static Application Security Testing with Bandit (SAST)**:
   Bandit analyzes application Python source code in the `app/` directory, focusing strictly on high-severity and high-confidence vulnerabilities:
   ```bash
   bandit -r app -lll -iii
   ```

3. **Dependency CVE Scanning with Trivy (SCA)**:
   Trivy matches dependencies in `app/requirements.txt` against global vulnerability feeds and fails the build upon finding `HIGH` or `CRITICAL` severity CVEs:
   ```bash
   trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
   ```

4. **Infrastructure as Code Scanning with Checkov**:
   Checkov analyzes workload Terraform templates to detect security misconfigurations:
   ```bash
   checkov -d "${WORKLOAD_DIR}" --framework terraform --compact
   ```
   Documented baseline exceptions are recognized for VPC Flow Logs (`CKV2_AWS_11`), Public Subnets (`CKV_AWS_130`), HTTP port 80 (`CKV_AWS_260`), and Public IPs (`CKV_AWS_88`).

#### Run Security Scans Manually

```bash
cd ~/fcaj-aws-devsecops
gitleaks dir . --config .gitleaks.toml --redact --no-banner
bandit -r app -lll -iii
trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
checkov -d workload --framework terraform --compact
```

---

### Automated Security Gate Enforcement

Security Gates are strictly enforced in the delivery pipeline: `SecurityScan` must complete with zero exit codes before `TerraformPlan` is allowed to execute. Buildspecs enforce `set -euo pipefail`, ensuring that any scanner detecting a violation halts the delivery pipeline immediately.
"""
    )

    # 5.6
    write_page(
        "5.6-Terraform-Plan-Approval", 6, "5.6",
        "Lập kế hoạch hạ tầng và phê duyệt",
        "Infrastructure Planning & Manual Approval",
        """Chương này hướng dẫn cấu hình dự án AWS CodeBuild cho giai đoạn **Terraform Plan**, lưu trữ tệp kế hoạch thay đổi hạ tầng dưới dạng Artifact và thiết lập cổng phê duyệt thủ công (**Manual Approval**) giúp kiểm soát chặt chẽ các tác động hạ tầng trước khi triển khai thực tế.

---

### Cấu hình CodeBuild Terraform Plan và Runtime Variables

Giai đoạn `TerraformPlan` sử dụng CodeBuild project chuyên biệt với vai trò `TerraformPlanRole`. Dự án nhận tệp buildspec `cicd/buildspec-plan.yml` và được cung cấp các biến môi trường runtime từ tầng platform:

```bash
# Kiểm tra các runtime variables được truyền vào CodeBuild Plan
echo "TF_STATE_BUCKET   : ${TF_STATE_BUCKET}"
echo "WORKLOAD_ROLE_ARN : ${WORKLOAD_ROLE_ARN}"
echo "WORKLOAD_DIR      : ${WORKLOAD_DIR}"
```

### Thực thi Terraform Init và Sinh kế hoạch triển khai

1. **Khởi tạo Terraform Backend**:
   CodeBuild cấu hình backend từ xa trỏ tới S3 bucket đã được khởi tạo trong tầng bootstrap:
   ```bash
   terraform -chdir="${WORKLOAD_DIR}" init \
     -backend-config="bucket=${TF_STATE_BUCKET}" \
     -backend-config="key=workload/terraform.tfstate" \
     -backend-config="region=${AWS_REGION}"
   ```

2. **Sinh kế hoạch thay đổi (Plan Output)**:
   Lệnh `terraform plan` tạo ra bản nhị phân `tfplan` và xuất bản báo cáo dạng văn bản `plan.txt` để người phê duyệt dễ dàng đọc hiểu:
   ```bash
   terraform -chdir="${WORKLOAD_DIR}" plan -out=tfplan -input=false
   terraform -chdir="${WORKLOAD_DIR}" show -no-color tfplan > plan.txt
   ```

### Đóng gói Artifact và Thiết lập cổng Manual Approval

- **Lưu trữ Artifact**: Tệp nhị phân `tfplan`, bản mô tả `plan.txt` và tệp khóa `.terraform.lock.hcl` được đóng gói thành artifact `PlanOutput` và lưu trữ an toàn trong S3 Pipeline Artifact Store.
- **Manual Approval Stage**: Pipeline tạm dừng sau khi hoàn thành bước Plan. Người có thẩm quyền (Reviewer) xem xét nội dung tệp `plan.txt`, kiểm tra danh sách tài nguyên sẽ được thêm mới, chỉnh sửa hoặc xóa bỏ.
- **Quyết định phê duyệt**:
  - Chọn **Approve**: Cho phép pipeline chuyển tiếp sang giai đoạn `TerraformApply`.
  - Chọn **Reject**: Hủy bỏ đợt triển khai, bảo vệ hệ thống khỏi những thay đổi không mong muốn.

---

![Giao diện phê duyệt thay đổi hạ tầng tại bước Manual Approval trong AWS CodePipeline](/images/5-Workshop/5.6-Terraform-Plan-Approval/manual-approval.png)

*Giao diện phê duyệt thay đổi hạ tầng tại bước Manual Approval trong AWS CodePipeline*
""",
        """This chapter covers configuring the AWS CodeBuild project for **Terraform Plan**, persisting plan artifacts, and setting up a **Manual Approval** gate to govern infrastructure modifications before production changes take effect.

---

### CodeBuild Terraform Plan & Runtime Variables

The `TerraformPlan` stage operates inside a dedicated CodeBuild project running under `TerraformPlanRole`. The build consumes `cicd/buildspec-plan.yml` and receives runtime parameters managed by the platform layer:

```bash
# Inspect runtime parameters supplied to CodeBuild Plan
echo "TF_STATE_BUCKET   : ${TF_STATE_BUCKET}"
echo "WORKLOAD_ROLE_ARN : ${WORKLOAD_ROLE_ARN}"
echo "WORKLOAD_DIR      : ${WORKLOAD_DIR}"
```

### Executing Terraform Init & Generating Plan Artifacts

1. **Initializing the Remote Backend**:
   CodeBuild initializes the remote S3 state backend created during the bootstrap phase:
   ```bash
   terraform -chdir="${WORKLOAD_DIR}" init \
     -backend-config="bucket=${TF_STATE_BUCKET}" \
     -backend-config="key=workload/terraform.tfstate" \
     -backend-config="region=${AWS_REGION}"
   ```

2. **Generating the Execution Plan**:
   `terraform plan` outputs a deterministic binary `tfplan` and generates a human-readable text summary `plan.txt`:
   ```bash
   terraform -chdir="${WORKLOAD_DIR}" plan -out=tfplan -input=false
   terraform -chdir="${WORKLOAD_DIR}" show -no-color tfplan > plan.txt
   ```

### Packaging Artifacts & Enforcing Manual Approval

- **Artifact Preservation**: The binary `tfplan`, summary `plan.txt`, and `.terraform.lock.hcl` are packaged into the `PlanOutput` artifact and stored in S3.
- **Manual Approval Gate**: The pipeline halts upon plan completion. Reviewers inspect `plan.txt` directly to review planned additions, modifications, or destructions.
- **Review Decision**:
  - Selecting **Approve** authorizes the pipeline to proceed to `TerraformApply`.
  - Selecting **Reject** terminates the execution, protecting live infrastructure from unintended alterations.

---

![Infrastructure review and approval dialog at Manual Approval stage in AWS CodePipeline](/images/5-Workshop/5.6-Terraform-Plan-Approval/manual-approval.png)

*Infrastructure review and approval dialog at Manual Approval stage in AWS CodePipeline*
"""
    )

    # 5.7
    write_page(
        "5.7-Terraform-Apply", 7, "5.7",
        "Triển khai hạ tầng tự động",
        "Automated Infrastructure Deployment",
        """Chương này hướng dẫn cấu hình dự án AWS CodeBuild cho giai đoạn **Terraform Apply**, đảm bảo việc triển khai hạ tầng được thực thi an toàn bằng vai trò đặc quyền tối thiểu (**TerraformDeployRole**) và chỉ sử dụng đúng tệp kế hoạch nhị phân đã được phê duyệt.

---

### Vai trò TerraformDeployRole và Cơ chế triển khai an toàn

Giai đoạn `TerraformApply` được cấp quyền thông qua `TerraformDeployRole`. Vai trò này chỉ cho phép tạo, sửa và quản lý các tài nguyên trong phạm vi workload (VPC, Subnet, Route Table, Internet Gateway, Security Group, EC2 instance và IAM Instance Profile liên quan).

```bash
# Cập nhật Platform khi có thay đổi trong định nghĩa IAM Role hoặc Pipeline
cd ~/fcaj-aws-devsecops/platform
terraform init
terraform plan
terraform apply -auto-approve
```

### Sử dụng tệp kế hoạch đã phê duyệt và Thực thi Apply

1. **Nhận Artifacts đầu vào**:
   CodeBuild nhận đồng thời `SourceOutput` (mã nguồn ứng dụng) và `PlanOutput` (tệp `tfplan` đã qua bước phê duyệt thủ công).
2. **Khởi tạo và thực thi chính xác binary plan**:
   Hệ thống khởi chạy `terraform apply` trực tiếp với tệp kế hoạch đã định sẵn, không cho phép sinh lại plan mới trong lúc apply:
   ```bash
   RUN_MODE=apply
   terraform -chdir="${WORKLOAD_DIR}" init \
     -backend-config="bucket=${TF_STATE_BUCKET}" \
     -backend-config="key=workload/terraform.tfstate" \
     -backend-config="region=${AWS_REGION}"
   terraform -chdir="${WORKLOAD_DIR}" apply -input=false -auto-approve tfplan
   ```
3. **Xuất giá trị đầu ra (Workload Outputs)**:
   Sau khi apply thành công, các thông số như `ec2_public_ip` và `app_health_url` được xuất ra để chuyển tiếp cho bước kiểm tra sau triển khai.
""",
        """This chapter covers configuring the AWS CodeBuild project for **Terraform Apply**, executing infrastructure changes securely under the least-privilege `TerraformDeployRole` strictly consuming the pre-approved plan binary.

---

### TerraformDeployRole & Secure Deployment Model

The `TerraformApply` stage assumes `TerraformDeployRole`. Permissions are constrained strictly to workload-scoped resources (VPCs, Subnets, Route Tables, Internet Gateways, Security Groups, EC2 instances, and IAM Instance Profiles).

```bash
# Update platform layer when modifying IAM roles or pipeline definitions
cd ~/fcaj-aws-devsecops/platform
terraform init
terraform plan
terraform apply -auto-approve
```

### Consuming Approved Plans & Executing Apply

1. **Input Artifact Assembly**:
   CodeBuild receives `SourceOutput` alongside the approved `PlanOutput`.
2. **Deterministic Plan Application**:
   Terraform executes directly against the approved binary plan without regenerating plans at apply time:
   ```bash
   RUN_MODE=apply
   terraform -chdir="${WORKLOAD_DIR}" init \
     -backend-config="bucket=${TF_STATE_BUCKET}" \
     -backend-config="key=workload/terraform.tfstate" \
     -backend-config="region=${AWS_REGION}"
   terraform -chdir="${WORKLOAD_DIR}" apply -input=false -auto-approve tfplan
   ```
3. **Emitting Workload Outputs**:
   Upon apply completion, output values such as `ec2_public_ip` and `app_health_url` are emitted for subsequent verification.
"""
    )

    # 5.8
    write_page(
        "5.8-Target-Environment", 8, "5.8",
        "Môi trường triển khai mục tiêu",
        "Target Workload Environment",
        """Chương này trình bày chi tiết kiến trúc hạ tầng Workload được quản lý tự động bằng Terraform, bao gồm mạng **Amazon VPC**, nhóm bảo mật (**Security Group**), máy chủ **Amazon EC2** và quy trình bootstrap ứng dụng web demo.

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
""",
        """This chapter details the workload target infrastructure managed automatically by Terraform, encompassing **Amazon VPC**, **Security Groups**, **Amazon EC2**, and automated application bootstrapping.

---

### Workload Network Architecture & Access Controls

- **Amazon VPC & Subnets**: Provisions a dedicated VPC with isolated address space, an Internet Gateway, and a Route Table associated with the public subnet for routing internet traffic.
- **Security Group Ingress Controls**: Configures web server security groups permitting HTTP (port 80) traffic for accessibility and testing. Ingress port 22 (SSH) remains fully closed to eliminate brute-force attack vectors. Default security groups are stripped of all rules.

---

### EC2 Provisioning & Automated Application Bootstrap

1. **Amazon EC2 Instance Configuration**:
   Instances run Amazon Linux 2023 (`t3.micro`) equipped with an IAM Instance Profile granting secure management via AWS Systems Manager (SSM) Session Manager without exposed management ports.

2. **Automated User Data Bootstrapping (`user_data.sh.tftpl`)**:
   During instance launch, the user data script installs Python 3.11, configures the Flask web application, installs requirements, and registers a persistent `systemd` service:

```bash
#!/bin/bash
set -euo pipefail

# Update packages and install Python
dnf update -y
dnf install -y python3.11 python3.11-pip git

# Create dedicated application user
useradd -m -s /bin/bash appuser || true
mkdir -p /opt/app && chown appuser:appuser /opt/app

# Deploy application code
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

# Register systemd unit
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

### Verifying Network Connectivity & Application Access

Verify public connectivity and endpoint health using the emitted workload outputs:

```bash
# Extract Public IP from workload output
EC2_IP=$(terraform -chdir=workload output -raw ec2_public_ip)
echo "Accessing EC2 Web Server at: http://${EC2_IP}/"

# Query HTTP health endpoint
curl -I "http://${EC2_IP}/"
curl -s "http://${EC2_IP}/health"
```

> [!TIP]
> A successful `200 OK` response from the `/health` route validates that both the infrastructure network layer and the demo application service are operating correctly.
"""
    )

    # 5.9
    write_page(
        "5.9-Post-Deploy-Verification", 9, "5.9",
        "Kiểm thử và xác thực sau triển khai",
        "Post-Deploy Verification & Smoke Testing",
        """Chương này hướng dẫn cấu hình giai đoạn kiểm thử tự động **PostDeployVerification (Smoke Test)** sau khi hoàn tất `TerraformApply`, giúp đảm bảo máy chủ EC2 đã khởi động xong và ứng dụng phản hồi chính xác trước khi kết thúc pipeline.

---

### Cơ chế kiểm thử tự động (Automated Smoke Test)

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
INSTANCE_ID=$(aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=*fcaj*" "Name=instance-state-name,Values=running" \
  --query "Reservations[].Instances[].InstanceId" \
  --output text)

# Kết nối trực tiếp vào máy chủ thông qua SSM
aws ssm start-session --target "$INSTANCE_ID"

# Khi vào trong terminal của máy chủ EC2, kiểm tra nhật ký:
sudo systemctl status demo-app
cat /var/log/user-data.log
sudo journalctl -u demo-app -n 50 --no-pager
```

> [!NOTE]
> Khi Smoke Test thất bại, hạ tầng AWS đã được tạo nhưng dịch vụ ứng dụng có thể gặp lỗi cú pháp Python hoặc thiếu thư viện. Việc kiểm tra `user-data.log` giúp nhanh chóng cô lập nguyên nhân và sửa đổi mã nguồn.
""",
        """This chapter covers configuring the automated **PostDeployVerification (Smoke Test)** stage following `TerraformApply`, ensuring the EC2 host and demo web application are fully operational before finalizing the pipeline.

---

### Automated Smoke Testing Architecture

Smoke testing is performed by AWS CodeBuild driven by `cicd/buildspec-apply.yml` under `RUN_MODE=smoke`:

1. **Extracting Host Identifiers**: Retrieves the workload Public IP or Public DNS from Terraform state outputs.
2. **Instance State Verification**: Confirms the EC2 instance is in `running` state and passing standard system health checks.
3. **HTTP Endpoint Polling**: Executes automated curl loops against `/health` with retries to account for application bootstrapping duration.
4. **Validating HTTP 200 OK**: The delivery pipeline concludes with `SUCCEEDED` only upon receiving a verified HTTP 200 response with valid JSON payload.

---

### Troubleshooting Smoke Test Failures

If the smoke test times out without receiving HTTP 200, CodePipeline marks the stage as `FAILED`. Administrators can securely troubleshoot the instance via AWS Systems Manager Session Manager without opening SSH ports:

```bash
# Retrieve Instance ID of the running demo EC2
INSTANCE_ID=$(aws ec2 describe-instances \
  --filters "Name=tag:Name,Values=*fcaj*" "Name=instance-state-name,Values=running" \
  --query "Reservations[].Instances[].InstanceId" \
  --output text)

# Start secure terminal session via SSM
aws ssm start-session --target "$INSTANCE_ID"

# Inspect application status and bootstrap logs:
sudo systemctl status demo-app
cat /var/log/user-data.log
sudo journalctl -u demo-app -n 50 --no-pager
```

> [!NOTE]
> Smoke test failures indicate that while infrastructure provisioning succeeded, the application process encountered an initialization error. Checking `user-data.log` accelerates root-cause isolation.
"""
    )

    # 5.10
    write_page(
        "5.10-Logging-Monitoring-Notification", 10, "5.10",
        "Giám sát, nhật ký và cảnh báo",
        "Logging, Monitoring & Notifications",
        """Chương này hướng dẫn thiết lập hệ thống quan sát toàn diện cho chuỗi DevSecOps, kết hợp giữa **Amazon CloudWatch**, **Amazon EventBridge**, **Amazon SNS**, **AWS CloudTrail** và **AWS Budgets** nhằm thu thập nhật ký thực thi, gửi thông báo tức thời và kiểm soát chi phí hoạt động.

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
""",
        """This chapter covers establishing full-stack observability for the DevSecOps pipeline, integrating **Amazon CloudWatch**, **Amazon EventBridge**, **Amazon SNS**, **AWS CloudTrail**, and **AWS Budgets** for centralized logging, event notifications, and cost governance.

---

### Centralized Logging & Pipeline Progress Monitoring

- **Amazon CloudWatch Logs**: Automatically collects and persists build output logs across all CodeBuild projects (`validate-security`, `terraform-plan`, `terraform-apply`), providing transparent trace logs for scanner violations and Terraform errors.
- **CodePipeline Visual Tracking**: The CodePipeline dashboard delivers real-time visibility across all 7 delivery stages.

---

### Event-Driven Notifications via EventBridge & SNS

1. **Amazon EventBridge Rule**:
   Listens for state change events emitted by CodePipeline (specifically capturing `FAILED` and `SUCCEEDED` triggers):
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

2. **Amazon SNS Topic & Email Alerts**:
   EventBridge routes events to the `fcaj-devsecops-notifications` SNS topic, which fans out email alerts to designated engineering contacts:
   ```bash
   # Verify confirmed subscriptions on the SNS topic
   aws sns list-subscriptions-by-topic --topic-arn "$SNS_TOPIC_ARN"
   ```

---

### Audit Logging via CloudTrail & Cost Governance via AWS Budgets

- **AWS CloudTrail**: Logs all API activity touching AWS resources (IAM, S3, CodePipeline, EC2) for compliance reporting and incident forensics.
- **AWS Budgets**: Enforces cost governance by alerting team leads when actual or forecasted monthly expenditures exceed target thresholds.
"""
    )

    # 5.11
    write_page(
        "5.11-DevSecOps-Pipeline", 11, "5.11",
        "Hoàn thiện AWS DevSecOps Pipeline",
        "Complete AWS DevSecOps Pipeline",
        """Chương này tổng hợp toàn bộ 7 giai đoạn của chuỗi cung ứng **AWS CodePipeline** thành một quy trình tự động hóa khép kín và hướng dẫn các quy tắc vận hành commit hàng ngày.

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
""",
        """This chapter synthesizes the complete 7-stage **AWS CodePipeline** continuous delivery workflow into a cohesive operational overview alongside daily developer commit practices.

---

### 7-Stage Pipeline Execution Workflow

Every commit pushed to the `main` branch on GitHub automatically triggers the 7 sequential delivery stages:

```text
Source ──> ValidateTest ──> SecurityScan ──> TerraformPlan ──> ManualApproval ──> TerraformApply ──> PostDeployVerification
```

1. **Source Stage**: Captures repository pushes via AWS CodeConnections, packaging source code into the `SourceOutput` artifact.
2. **Validate & Test Stage**: Runs CodeBuild under `RUN_MODE=validate` to verify Terraform syntax formatting, test Python compilation, and execute Pytest suites.
3. **Security Scan Stage (Security Gate)**: Concurrently runs Gitleaks (Secrets), Bandit (SAST), Trivy (SCA/CVE), and Checkov (IaC). Scanner violations halt execution immediately.
4. **Terraform Plan Stage**: Generates the workload `tfplan` binary and summary `plan.txt`, packaged as the `PlanOutput` artifact.
5. **Manual Approval Stage**: Pauses execution and dispatches SNS review alerts. Administrators inspect planned changes before choosing **Approve** or **Reject**.
6. **Terraform Apply Stage**: Consumes the approved plan binary to execute `terraform apply`, ensuring predictable and tamper-free infrastructure provisioning.
7. **Post-Deploy Verification Stage**: Runs automated smoke tests validating EC2 host availability and verifying HTTP 200 status on the `/health` endpoint.

---

### Daily Developer Commit Workflow

The pipeline is provisioned once in the platform layer. Routine application or workload changes follow standard Git workflows:

```bash
cd ~/fcaj-aws-devsecops
git add -A
git status
git commit -m "feat: update application or workload"
git push origin main
```

> [!IMPORTANT]
> - There is no need to re-apply the platform layer for routine changes inside `app/` or `workload/`.
> - Avoid rapid consecutive pushes while an active execution is in `TerraformApply` to prevent state lock contention.
> - If an error occurs prior to `TerraformApply`, the pipeline fails safely and live infrastructure remains untouched.
"""
    )

    # 5.12
    write_page(
        "5.12-DevSecOps-Scenarios", 12, "5.12",
        "Kịch bản kiểm thử bảo mật DevSecOps",
        "DevSecOps Demonstration Scenarios",
        """Chương này chứng minh hiệu quả thực tế của các cổng kiểm soát an ninh (**Security Gates**) thông qua các kịch bản kiểm thử: triển khai đường cơ sở sạch, tự động phát hiện và ngăn chặn cấu hình SSH không an toàn, rò rỉ secret, thư viện có lỗ hổng CVE và cơ chế từ chối phê duyệt hạ tầng.

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
""",
        """This chapter demonstrates the real-world efficacy of **Security Gates** across five practical scenarios: clean baseline deployment, automated blocking of open SSH ingress, credential leakage detection, vulnerable dependency discovery, and manual approval rejection.

---

### Scenario 1: Clean Baseline Deployment (Success)

- **Objective**: Validate the end-to-end pipeline operates reliably when code and infrastructure definitions adhere to security best practices.
- **Result**: All 7 stages from Source to PostDeployVerification transition to `SUCCEEDED` (green). The demo web app is deployed and returns HTTP `200 OK`.

---

### Scenario 2: Checkov Blocks Dangerous Open SSH Ingress

- **Simulation**: Introducing a security group rule opening port `22` (SSH) to `0.0.0.0/0` from `demo/fixtures/public_ssh.tf.example`.
- **Execution**:
  ```bash
  cp demo/fixtures/public_ssh.tf.example workload/public_ssh.tf
  git add workload/public_ssh.tf && git commit -m "test: simulate public ssh vulnerability" && git push
  ```
- **Result**: Checkov identifies violation `CKV_AWS_24`, exits with a failure code, and **halts the pipeline at SecurityScan**, preventing Terraform Plan from running.

---

### Scenario 3: Gitleaks Blocks Leaked Secrets & Credentials

- **Simulation**: Adding code containing a simulated AWS Access Key into `app/leak.py`.
- **Execution**:
  ```bash
  echo 'AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLEEXAMPLE"' > app/leak.py
  git add app/leak.py && git commit -m "test: simulate credential leak" && git push
  ```
- **Result**: Gitleaks matches the AWS credential pattern, redacts output in build logs, and **fails the build immediately**.

---

### Scenario 4: Trivy Blocks Vulnerable Third-Party Dependencies

- **Simulation**: Adding an outdated dependency containing `HIGH/CRITICAL` CVEs into `app/requirements.txt`.
- **Execution**:
  ```bash
  cat demo/fixtures/requirements-vulnerable.txt >> app/requirements.txt
  git add app/requirements.txt && git commit -m "test: simulate vulnerable dependency" && git push
  ```
- **Result**: Trivy identifies qualifying CVEs and exits with code `1`, halting execution before deployment.

---

### Scenario 5: Rejecting Infrastructure Changes at Manual Approval

- **Simulation**: The pipeline completes scanning and enters approval. The reviewer inspects `plan.txt` and discovers unauthorized changes.
- **Action**: The reviewer clicks **Reject** in the AWS CodePipeline console providing rationale.
- **Result**: Execution terminates; `TerraformApply` is never invoked, protecting live environments from unapproved drift.

---

### Summary of Security Gate Efficacy

Through real-world test scenarios, the DevSecOps delivery pipeline proves its ability to identify and block common industry vulnerabilities early in the software lifecycle (Shift-Left): leaked secrets, vulnerable dependencies, and infrastructure misconfigurations.
"""
    )

    # 5.13
    write_page(
        "5.13-Results-Cleanup", 13, "5.13",
        "Đánh giá kết quả và dọn dẹp tài nguyên",
        "Workshop Acceptance & Resource Cleanup",
        """Chương này tổng kết các kết quả đạt được của dự án theo tiêu chí nghiệm thu và hướng dẫn chi tiết quy trình dọn dẹp (cleanup) toàn bộ tài nguyên đám mây AWS theo đúng thứ tự phụ thuộc nhằm tối ưu chi phí.

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
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query "Reservations[].Instances[].InstanceId" \
  --output text

# Kiểm tra các S3 bucket liên quan đã bị xóa
aws s3 ls | grep fcaj || true
```

> [!TIP]
> Việc kiểm tra lại trang AWS Billing Console sau 24 giờ giúp xác nhận tài khoản không còn bất kỳ chi phí phát sinh nào sau khi kết thúc Workshop.
""",
        """This chapter summarizes the project deliverables against workshop acceptance criteria and provides a step-by-step teardown procedure to destroy all AWS resources in correct dependency order.

---

### Workshop Acceptance Evaluation

The project fulfills all architectural and security objectives defined for the AWS DevSecOps Workshop:
- **Full Automation**: Automated 7-stage continuous delivery pipeline orchestrated by AWS CodePipeline from Git push to post-deploy testing.
- **Multi-Layer Shift-Left Security**: Concurrent execution of Gitleaks, Bandit, Trivy, and Checkov acting as blocking security gates.
- **Governance & Change Control**: Deterministic Terraform Plan artifacts coupled with Manual Approval gates before apply execution.
- **Full-Stack Observability**: Centralized CloudWatch logging, EventBridge state tracking, SNS email alerts, and CloudTrail audit logging.
- **Automated Verification**: PostDeployVerification smoke testing ensuring host and HTTP application health before completion.

---

### Resource Cleanup in Dependency Order

To prevent dependency lockouts during teardown, infrastructure destruction must strictly follow this 3-step sequence:

#### Step 1: Destroy Workload Infrastructure Layer

Workload resources (EC2 instances, VPCs, Subnets, Route Tables, and Security Groups) must be destroyed first:

```bash
cd ~/fcaj-aws-devsecops/workload

# Initialize and destroy workload
terraform init
terraform destroy -auto-approve
```

#### Step 2: Destroy CI/CD Platform Layer

Once the workload layer is completely destroyed, teardown CodePipeline, CodeBuild projects, IAM roles, EventBridge rules, and SNS topics:

```bash
cd ~/fcaj-aws-devsecops/platform

# Initialize and destroy platform
terraform init
terraform destroy -auto-approve
```

#### Step 3: Purge S3 Buckets & Destroy Bootstrap Layer

S3 buckets storing state and build artifacts enforce object versioning. Purge all bucket contents before executing destroy:

```bash
# Empty state and artifact buckets
aws s3 rm "s3://${TF_STATE_BUCKET}" --recursive
aws s3 rm "s3://${ARTIFACT_BUCKET}" --recursive

# Destroy bootstrap resources
cd ~/fcaj-aws-devsecops/bootstrap
terraform init
terraform destroy -auto-approve
```

---

### Verifying Residual Resources & Billing Confirmation

Verify that no unmanaged or orphaned resources remain running in the AWS account:

```bash
# Confirm zero running EC2 instances
aws ec2 describe-instances \
  --filters "Name=instance-state-name,Values=running" \
  --query "Reservations[].Instances[].InstanceId" \
  --output text

# Confirm workshop S3 buckets are removed
aws s3 ls | grep fcaj || true
```

> [!TIP]
> Reviewing the AWS Billing & Cost Management console 24 hours after teardown confirms zero residual charges.
"""
    )

if __name__ == "__main__":
    generate_all()
    print("\nAll synthesized chapters generated successfully!")
