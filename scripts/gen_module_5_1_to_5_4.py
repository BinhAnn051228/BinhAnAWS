import os
from pathlib import Path
from generator_common import BASE_DIR, write_section, write_parent

def build_5_1():
    p = BASE_DIR / "5.1-Prepare-Environment"
    sub_list = [
        {"num": "5.1.1", "dir": "5.1.1-aws-account-region", "title_vi": "Chuẩn bị AWS Account và chọn Region", "title_en": "Prepare AWS Account and Select Region", "summary_vi": "Thiết lập quyền hạn AWS và cấu hình Region mặc định ap-southeast-1", "summary_en": "Set up AWS account permissions and default region ap-southeast-1"},
        {"num": "5.1.2", "dir": "5.1.2-github-repository", "title_vi": "Chuẩn bị GitHub Repository", "title_en": "Prepare GitHub Repository", "summary_vi": "Khởi tạo Git repo và đẩy toàn bộ source tree lên GitHub branch main", "summary_en": "Initialize Git repo and push complete source tree to GitHub main branch"},
        {"num": "5.1.3", "dir": "5.1.3-terraform-code-structure", "title_vi": "Chuẩn bị Terraform và cấu trúc source code", "title_en": "Prepare Terraform & Source Code Structure", "summary_vi": "Tổng quan cấu trúc project chia lớp độc lập và phiên bản công cụ", "summary_en": "Layered project structure overview and default tool versions"},
        {"num": "5.1.4", "dir": "5.1.4-overall-architecture", "title_vi": "Giới thiệu kiến trúc tổng thể Workshop", "title_en": "Workshop Overall Architecture", "summary_vi": "Sơ đồ kiến trúc tổng thể FCAJ AWS DevSecOps và các dịch vụ hỗ trợ", "summary_en": "Overall FCAJ AWS DevSecOps architecture diagram and supporting services"},
        {"num": "5.1.5", "dir": "5.1.5-devsecops-workflow", "title_vi": "Giới thiệu luồng DevSecOps triển khai", "title_en": "DevSecOps Delivery Workflow", "summary_vi": "Luồng pipeline 7 giai đoạn nghiêm ngặt từ Source đến PostDeployVerification", "summary_en": "Strict 7-stage CI/CD delivery pipeline flow from Source to Verification"},
    ]

    # 5.1.1
    write_section(
        p / "5.1.1-aws-account-region",
        "5.1.1",
        "Chuẩn bị AWS Account và chọn Region",
        "Prepare AWS Account and Select Region",
        "`bootstrap/variables.tf`, `platform/variables.tf`, `workload/variables.tf`",
        """Project sử dụng AWS Region mặc định `ap-southeast-1` (Singapore). Biến `aws_region` được khai báo nhất quán tại cả bootstrap, platform và workload để các tài nguyên được tạo trong cùng một Region.

- **AWS Account**: Cần có quyền tạo các tài nguyên Workshop: S3, IAM, CodeBuild, CodePipeline, CodeConnections, SSM, SNS, EventBridge, CloudTrail, Budgets, VPC và EC2.
- **AWS Console**: Trong AWS Console, chọn Region Asia Pacific (Singapore) - `ap-southeast-1` trước khi thực hiện các bước quan sát hoặc kiểm tra.
- **CloudShell / Terminal**: Khi dùng AWS CloudShell hoặc terminal, đặt `AWS_REGION` và `AWS_DEFAULT_REGION` là `ap-southeast-1` để khớp với Terraform variables.

### Lệnh kiểm tra môi trường

```bash
export AWS_REGION="ap-southeast-1"
export AWS_DEFAULT_REGION="ap-southeast-1"
aws sts get-caller-identity
```

### Xác nhận AWS Account và Region

```bash
export AWS_REGION="ap-southeast-1"
export AWS_DEFAULT_REGION="$AWS_REGION"
ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
echo "AWS Account: $ACCOUNT_ID"
echo "AWS Region : $AWS_REGION"
aws sts get-caller-identity
```

> [!NOTE]
> Kết quả phải trả đúng AWS Account đang dùng cho Workshop và Region `ap-southeast-1` trước khi tạo bất kỳ resource nào.""",
        """The project defaults to the AWS Region `ap-southeast-1` (Singapore). The `aws_region` variable is consistently declared across bootstrap, platform, and workload modules to ensure all resources reside in the same Region.

- **Account Permissions**: The AWS account must have permissions to provision Workshop resources: S3, IAM, CodeBuild, CodePipeline, CodeConnections, SSM, SNS, EventBridge, CloudTrail, Budgets, VPC, and EC2.
- **AWS Console**: Always select Asia Pacific (Singapore) - `ap-southeast-1` before performing visual inspections or verifications.
- **Terminal / CloudShell**: When using AWS CloudShell or local CLI, set `AWS_REGION` and `AWS_DEFAULT_REGION` to `ap-southeast-1` to match Terraform configurations.

### Environment Verification Command

```bash
export AWS_REGION="ap-southeast-1"
export AWS_DEFAULT_REGION="ap-southeast-1"
aws sts get-caller-identity
```

### Confirm AWS Account and Region

```bash
export AWS_REGION="ap-southeast-1"
export AWS_DEFAULT_REGION="$AWS_REGION"
ACCOUNT_ID="$(aws sts get-caller-identity --query Account --output text)"
echo "AWS Account: $ACCOUNT_ID"
echo "AWS Region : $AWS_REGION"
aws sts get-caller-identity
```

> [!NOTE]
> The command must return the intended AWS Account ID and Region `ap-southeast-1` prior to provisioning any infrastructure resources.""",
        images_vi=[
            ("AWS IAM Console - Cấp quyền AdministratorAccess cho tài khoản IAM", "/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A2nh%20ch%E1%BB%A5p%20c%E1%BA%A5p%20quy%E1%BB%81n%20cho%20t%C3%A0i%20kho%E1%BA%A3n%20IAM.png"),
            ("AWS CloudShell - Cấu hình AWS_REGION=ap-southeast-1 và kiểm tra get-caller-identity", "/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A3nh%20ch%E1%BB%A5p%20%C4%91%E1%BB%8Bnh%20t%C3%A0i%20kho%E1%BA%A3n%20v%C3%A0%20set%20region%20m%E1%BA%B7c%20%C4%91%E1%BB%8Bnh.png")
        ],
        images_en=[
            ("AWS IAM Console - Grant AdministratorAccess permissions to IAM user", "/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A2nh%20ch%E1%BB%A5p%20c%E1%BA%A5p%20quy%E1%BB%81n%20cho%20t%C3%A0i%20kho%E1%BA%A3n%20IAM.png"),
            ("AWS CloudShell - Set AWS_REGION=ap-southeast-1 and verify get-caller-identity", "/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A3nh%20ch%E1%BB%A5p%20%C4%91%E1%BB%8Bnh%20t%C3%A0i%20kho%E1%BA%A3n%20v%C3%A0%20set%20region%20m%E1%BA%B7c%20%C4%91%E1%BB%8Bnh.png")
        ],
        weight=1
    )

    # 5.1.2
    write_section(
        p / "5.1.2-github-repository",
        "5.1.2",
        "Chuẩn bị GitHub Repository",
        "Prepare GitHub Repository",
        "`README.md`, `platform/variables.tf`, `platform/pipeline.tf`",
        """CodePipeline lấy source từ GitHub thông qua AWS CodeConnections. Repository mặc định được theo dõi ở branch `main`; tên owner và repository được truyền vào Terraform qua `github_owner` và `github_repo`.

### Khởi tạo repository

```bash
git init
git add .
git commit -m "initial FCAJ DevSecOps workshop"
git branch -M main
git remote add origin https://github.com/YOUR_USER/fcaj-aws-devsecops.git
git push -u origin main
```

### Clone repository đã có sẵn

```bash
cd ~
git clone https://github.com/<GITHUB_USER>/fcaj-aws-devsecops.git
cd fcaj-aws-devsecops
git status
git branch --show-current
ls -la
ls cicd
```

> [!IMPORTANT]
> Repository root phải nhìn thấy trực tiếp `app/`, `bootstrap/`, `cicd/`, `platform/`, `workload/...`; không để lồng thêm một lớp `fcaj-aws-devsecops/fcaj-aws-devsecops` vì CodeBuild tìm buildspec theo đường dẫn từ repository root.

**Kết quả cần đạt**: GitHub repository chứa toàn bộ source tree và branch `main` sẵn sàng để CodeConnections theo dõi thay đổi.""",
        """CodePipeline pulls source code from GitHub via AWS CodeConnections. The repository is tracked on the `main` branch; repository owner and name are passed to Terraform via `github_owner` and `github_repo`.

### Initialize Repository and Push Code

```bash
git init
git add .
git commit -m "initial FCAJ DevSecOps workshop"
git branch -M main
git remote add origin https://github.com/YOUR_USER/fcaj-aws-devsecops.git
git push -u origin main
```

### Clone Existing Repository

```bash
cd ~
git clone https://github.com/<GITHUB_USER>/fcaj-aws-devsecops.git
cd fcaj-aws-devsecops
git status
git branch --show-current
ls -la
ls cicd
```

> [!IMPORTANT]
> The repository root must directly expose `app/`, `bootstrap/`, `cicd/`, `platform/`, `workload/...`; avoid nested directory structures like `fcaj-aws-devsecops/fcaj-aws-devsecops` because CodeBuild resolves buildspec paths relative to the repository root.

**Expected Outcome**: The GitHub repository contains the full source tree with the `main` branch ready for CodeConnections webhook change detection.""",
        images_vi=[
            ("GitHub Repository - Cấu trúc repository fcaj-aws-devsecops trên branch main", "/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/%E1%BA%A3nh%20ch%E1%BB%A5p%20git%20repo.png"),
            ("AWS CloudShell - Clone GitHub repository vào CloudShell", "/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/clone%20git%20repo%20v%E1%BB%81%20aws%20cloudshell.png")
        ],
        images_en=[
            ("GitHub Repository - Project repository structure on branch main", "/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/%E1%BA%A3nh%20ch%E1%BB%A5p%20git%20repo.png"),
            ("AWS CloudShell - Clone GitHub repository into CloudShell", "/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/clone%20git%20repo%20v%E1%BB%81%20aws%20cloudshell.png")
        ],
        weight=2
    )

    # 5.1.3
    write_section(
        p / "5.1.3-terraform-code-structure",
        "5.1.3",
        "Chuẩn bị Terraform và cấu trúc source code",
        "Prepare Terraform & Source Code Structure",
        "`README.md`, `SOURCE_MANIFEST.txt`, `platform/variables.tf`",
        """Repository được chia thành các lớp độc lập để phân tách bootstrap, platform CI/CD và workload. Terraform CLI mặc định trong CodeBuild là `1.16.2`; Gitleaks `8.30.1` và Trivy `0.74.0` được cấu hình qua biến platform.

### Cấu trúc project

```text
fcaj-aws-devsecops/
├── app/              # Demo Flask app + unit tests
├── bootstrap/        # S3 Terraform State và S3 Pipeline Artifact
├── platform/         # IAM, CodeBuild, CodeConnections, CodePipeline, SNS, EventBridge, CloudTrail, Budget, SSM
├── workload/         # VPC, Public Subnet, Internet Gateway, Route Table, Security Group và EC2 demo
├── cicd/             # 3 buildspec cho validate/security, plan, apply/smoke
├── iam-policy/       # IAM policy JSON templates cho từng vai trò
├── demo/             # Fixture và script kích hoạt các tình huống lỗi có chủ đích
├── docs/             # Tài liệu kiến trúc và sơ đồ hệ thống
├── scripts/          # Shell script hỗ trợ init và cấu hình
├── .gitleaks.toml    # Cấu hình rule quét secret
├── Makefile          # Command tiện ích chạy local test/security
└── README.md         # Hướng dẫn chi tiết dự án
```

- `bootstrap/`: Tạo S3 Terraform State và S3 Pipeline Artifact.
- `platform/`: Tạo IAM, CodeBuild, CodeConnections, CodePipeline, SNS, EventBridge, CloudTrail, Budget và SSM Parameter Store.
- `workload/`: Tạo VPC, Public Subnet, Internet Gateway, Route Table, Security Group và EC2 demo.
- `cicd/`: 3 buildspec cho validate/security, plan, apply/smoke.
- `demo/`: Fixture và script kích hoạt các tình huống lỗi có chủ đích.

### Cài/kiểm tra Terraform trên CloudShell mới

```bash
cd ~
TF_VERSION="1.16.2"
curl -fsSLo /tmp/terraform.zip \
  "https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip"
unzip -o /tmp/terraform.zip -d "$HOME/bin"
export PATH="$HOME/bin:$PATH"
terraform version
```

> [!TIP]
> CloudShell có thể bị reset. Nếu tạo lại môi trường, chỉ cần clone repo và cài lại Terraform; tài nguyên AWS/state trong S3 không mất theo CloudShell.""",
        """The repository is architected into decoupled layers separating bootstrap, CI/CD platform, and workload infrastructure. Terraform CLI default in CodeBuild is `1.16.2`; Gitleaks `8.30.1` and Trivy `0.74.0` are configured via platform variables.

### Project Directory Layout

```text
fcaj-aws-devsecops/
├── app/              # Demo Flask app + unit tests
├── bootstrap/        # S3 Terraform State and S3 Pipeline Artifact buckets
├── platform/         # IAM, CodeBuild, CodeConnections, CodePipeline, SNS, EventBridge, CloudTrail, Budget, SSM
├── workload/         # VPC, Public Subnet, Internet Gateway, Route Table, Security Group and EC2 demo
├── cicd/             # 3 buildspecs: validate/security, plan, apply/smoke
├── iam-policy/       # IAM policy JSON templates
├── demo/             # Fixtures and scripts triggering intentional security failures
├── docs/             # Architecture documentation and diagrams
├── scripts/          # Helper scripts for initialization and config
├── .gitleaks.toml    # Secret scanning rule configuration
├── Makefile          # Convenience automation targets
└── README.md         # Project documentation
```

- `bootstrap/`: Provisions S3 Terraform State and S3 Pipeline Artifact buckets.
- `platform/`: Provisions IAM, CodeBuild, CodeConnections, CodePipeline, SNS, EventBridge, CloudTrail, Budget, and SSM Parameter Store.
- `workload/`: Provisions VPC, Public Subnet, Internet Gateway, Route Table, Security Group, and EC2 demo.
- `cicd/`: Exactly 3 buildspecs for validate/security, plan, apply/smoke.
- `demo/`: Fixtures and scripts triggering intentional security failure scenarios.

### Install / Verify Terraform on CloudShell

```bash
cd ~
TF_VERSION="1.16.2"
curl -fsSLo /tmp/terraform.zip \
  "https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip"
unzip -o /tmp/terraform.zip -d "$HOME/bin"
export PATH="$HOME/bin:$PATH"
terraform version
```

> [!TIP]
> CloudShell sessions may be reset periodically. If a new environment is spun up, simply re-clone the repo and reinstall Terraform; AWS resources and remote state stored in S3 will persist safely.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )

    # 5.1.4
    write_section(
        p / "5.1.4-overall-architecture",
        "5.1.4",
        "Giới thiệu kiến trúc tổng thể Workshop",
        "Workshop Overall Architecture",
        "`docs/architecture-v6.png`",
        """Kiến trúc tổng thể phân tách rõ **execution flow** và các **support services**. Developer push code lên GitHub; source đi qua CodeConnections vào CodePipeline. Pipeline thực hiện validate/test, security scan, Terraform plan, manual approval, apply và post-deploy smoke test. Các dịch vụ S3, SSM, CloudWatch, EventBridge, SNS, CloudTrail và Budgets hỗ trợ state, artifact, secret, logging, notification, audit và cost control.

![Kiến trúc tổng thể Workshop FCAJ AWS DevSecOps](/images/2-Proposal/FCAJ_AWS_DevSecOps_Recommended_Architecture_v6.png)
*Kiến trúc tổng thể Workshop FCAJ AWS DevSecOps - v6*""",
        """The overall architecture strictly decouples the **execution flow** from **support services**. Developers push code to GitHub; source flows via CodeConnections into CodePipeline. The pipeline executes validate/test, security scan, Terraform plan, manual approval, apply, and post-deploy smoke test. Supporting AWS services S3, SSM, CloudWatch, EventBridge, SNS, CloudTrail, and Budgets manage state, artifacts, secrets, logging, notifications, audits, and cost governance.

![FCAJ AWS DevSecOps Recommended Overall Architecture](/images/2-Proposal/FCAJ_AWS_DevSecOps_Recommended_Architecture_v6.png)
*Overall FCAJ AWS DevSecOps Recommended Architecture - v6*""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )

    # 5.1.5
    write_section(
        p / "5.1.5-devsecops-workflow",
        "5.1.5",
        "Giới thiệu luồng DevSecOps triển khai",
        "DevSecOps Delivery Workflow",
        "`platform/pipeline.tf`",
        """### Luồng pipeline

```text
GitHub
  ↓
AWS CodeConnections
  ↓
Source
  ↓
ValidateTest
  ↓
SecurityScan
  ↓
TerraformPlan
  ↓
ManualApproval
  ↓
TerraformApply
  ↓
PostDeployVerification
  ↓
SUCCEEDED
```

### Nguyên tắc bảo vệ trọng yếu

- **Security Gate bắt buộc**: `SecurityScan` phải thành công trước khi `TerraformPlan` được chạy.
- **Kế hoạch bất biến (Immutable Plan)**: `TerraformApply` chỉ sử dụng binary plan đã được tạo trước đó và đã đi qua `ManualApproval`.
- **Xác minh thực tế**: Sau Apply, smoke test xác minh endpoint `/health` trước khi pipeline được xem là thành công.""",
        """### Pipeline Workflow

```text
GitHub
  ↓
AWS CodeConnections
  ↓
Source
  ↓
ValidateTest
  ↓
SecurityScan
  ↓
TerraformPlan
  ↓
ManualApproval
  ↓
TerraformApply
  ↓
PostDeployVerification
  ↓
SUCCEEDED
```

### Critical Architecture Rules

- **Mandatory Security Gate**: `SecurityScan` must succeed before `TerraformPlan` is allowed to execute.
- **Immutable Plan Execution**: `TerraformApply` consumes only the pre-generated binary plan that has passed `ManualApproval`.
- **Post-Deploy Verification**: Following Apply, automated smoke testing verifies the `/health` endpoint before the pipeline is deemed successful.""",
        images_vi=[
            ("Sơ đồ quy trình thực thi AWS DevSecOps CI/CD Delivery Workflow", "/images/5-Workshop/5.1-Prepare-Environment/5.1.5-devsecops-workflow/workflow.png")
        ],
        images_en=[
            ("AWS DevSecOps CI/CD Delivery Workflow Diagram", "/images/5-Workshop/5.1-Prepare-Environment/5.1.5-devsecops-workflow/workflow.png")
        ],
        weight=5
    )

    # Parent 5.1
    write_parent(
        p,
        "5.1",
        "Chuẩn bị môi trường & kiến trúc triển khai",
        "Environment Preparation & Deployment Architecture",
        "Phần Workshop được tổ chức theo trình tự triển khai thực tế: chuẩn bị môi trường, bootstrap backend, tạo platform CI/CD, tích hợp security gate, triển khai workload, xác minh sau deploy, giám sát và cuối cùng chạy các kịch bản kiểm thử DevSecOps.",
        "The Workshop is structured following practical deployment phases: environment preparation, backend bootstrapping, CI/CD platform setup, security gate integration, workload deployment, post-deploy verification, monitoring, and DevSecOps demo test cases.",
        sub_list,
        1
    )

def build_5_2():
    p = BASE_DIR / "5.2-Terraform-Backend-State"
    sub_list = [
        {"num": "5.2.1", "dir": "5.2.1-s3-state-bucket", "title_vi": "Tạo Amazon S3 Bucket lưu Terraform State", "title_en": "Create Amazon S3 Bucket for Terraform State", "summary_vi": "Tạo bucket S3 chuyên biệt để lưu trữ trạng thái hạ tầng", "summary_en": "Provision dedicated S3 bucket for infrastructure state storage"},
        {"num": "5.2.2", "dir": "5.2.2-versioning-encryption-public-access", "title_vi": "Cấu hình Versioning, Encryption và Block Public Access", "title_en": "Configure Versioning, Encryption, and Block Public Access", "summary_vi": "Bảo mật đa tầng cho State Bucket bằng SSE-S3 AES256 và BPA", "summary_en": "Multi-tier security with SSE-S3 AES256, BPA, and BucketOwnerEnforced"},
        {"num": "5.2.3", "dir": "5.2.3-terraform-state-locking", "title_vi": "Cấu hình Terraform State Locking", "title_en": "Configure Terraform State Locking", "summary_vi": "Khóa trạng thái đồng thời bằng tính năng S3 Native Lockfile use_lockfile=true", "summary_en": "State locking via S3 native lockfile use_lockfile=true"},
        {"num": "5.2.4", "dir": "5.2.4-declare-terraform-backend", "title_vi": "Khai báo Terraform Backend", "title_en": "Declare Terraform Backend", "summary_vi": "Cấu hình backend động cho hai layer platform và workload qua init script", "summary_en": "Dynamic S3 backend configuration for platform and workload layers"},
        {"num": "5.2.5", "dir": "5.2.5-verify-terraform-state", "title_vi": "Kiểm tra Terraform State", "title_en": "Verify Terraform State", "summary_vi": "Xác minh hai key riêng biệt platform/terraform.tfstate và workload/terraform.tfstate", "summary_en": "Verify separated state keys platform/terraform.tfstate and workload/terraform.tfstate"},
    ]

    # 5.2.1
    write_section(
        p / "5.2.1-s3-state-bucket",
        "5.2.1",
        "Tạo Amazon S3 Bucket lưu Terraform State",
        "Create Amazon S3 Bucket for Terraform State",
        "`bootstrap/main.tf`, `bootstrap/outputs.tf`",
        """Bootstrap tạo một S3 bucket riêng cho Terraform State. Tên bucket được ghép từ project name, AWS Account ID và Region để giảm khả năng trùng tên toàn cục.

### Terraform State bucket

```hcl
resource "aws_s3_bucket" "terraform_state" {
  bucket = "${local.prefix}-tfstate"
}
```

Sau `terraform apply`, output `terraform_state_bucket` trả về tên bucket dùng cho backend của platform và workload.

### Bootstrap S3 State và Artifact bucket

```bash
cd ~/fcaj-aws-devsecops/bootstrap
cp -n terraform.tfvars.example terraform.tfvars
terraform init
terraform fmt -check
terraform validate
terraform plan -out=bootstrap.tfplan
terraform apply bootstrap.tfplan
terraform output
```

> [!IMPORTANT]
> Luôn chạy plan/apply trong đúng thư mục `bootstrap`. File `*.tfplan` và `terraform.tfstate` local phải được `.gitignore` và không commit lên GitHub.""",
        """Bootstrap creates a dedicated S3 bucket for Terraform State. The bucket name is constructed from project name, AWS Account ID, and Region to ensure global uniqueness: `${local.prefix}-tfstate`.

### Terraform State Bucket

```hcl
resource "aws_s3_bucket" "terraform_state" {
  bucket = "${local.prefix}-tfstate"
}
```

After `terraform apply`, the output `terraform_state_bucket` returns the bucket name used for backend configuration of platform and workload.

### Bootstrap S3 State and Artifact Buckets

```bash
cd ~/fcaj-aws-devsecops/bootstrap
cp -n terraform.tfvars.example terraform.tfvars
terraform init
terraform fmt -check
terraform validate
terraform plan -out=bootstrap.tfplan
terraform apply bootstrap.tfplan
terraform output
```

> [!IMPORTANT]
> Always execute plan/apply inside the `bootstrap` directory. Local `*.tfplan` files and `terraform.tfstate` must be `.gitignore`'d and never committed to GitHub.""",
        images_vi=[
            ("Amazon S3 Console - Danh sách các S3 Bucket phục vụ Terraform State và Pipeline Artifacts", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.1-s3-state-bucket/t%E1%BA%A1o%20bucket.png")
        ],
        images_en=[
            ("Amazon S3 Console - S3 Buckets created for Terraform State and Pipeline Artifacts", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.1-s3-state-bucket/t%E1%BA%A1o%20bucket.png")
        ],
        weight=1
    )

    # 5.2.2
    write_section(
        p / "5.2.2-versioning-encryption-public-access",
        "5.2.2",
        "Cấu hình Versioning, Encryption và Block Public Access",
        "Configure Versioning, Encryption, and Block Public Access",
        "`bootstrap/main.tf`",
        """State bucket được bật Versioning, SSE-S3 (AES256), Block Public Access và BucketOwnerEnforced. Các cấu hình này giúp state có lịch sử version, mã hóa khi lưu trữ và không bị public ngoài ý muốn.

### Các control áp dụng cho Terraform State bucket

```hcl
resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_ownership_controls" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}
```""",
        """The state bucket enforces Versioning, SSE-S3 (AES256), Block Public Access, and BucketOwnerEnforced. These controls provide version history, encryption at rest, and complete isolation from public exposure.

### Security Controls Applied to Terraform State Bucket

```hcl
resource "aws_s3_bucket_versioning" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  versioning_configuration {
    status = "Enabled"
  }
}

resource "aws_s3_bucket_server_side_encryption_configuration" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  rule {
    apply_server_side_encryption_by_default {
      sse_algorithm = "AES256"
    }
  }
}

resource "aws_s3_bucket_public_access_block" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  block_public_acls       = true
  block_public_policy     = true
  ignore_public_acls      = true
  restrict_public_buckets = true
}

resource "aws_s3_bucket_ownership_controls" "terraform_state" {
  bucket = aws_s3_bucket.terraform_state.id
  rule {
    object_ownership = "BucketOwnerEnforced"
  }
}
```""",
        images_vi=[
            ("Amazon S3 Console - Bucket Versioning Enabled bảo vệ trạng thái Terraform", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/bucket%20verioning%20enable.png"),
            ("Amazon S3 Console - Server-side Default Encryption SSE-S3", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/default%20encrytion%20.png"),
            ("Amazon S3 Console - Block All Public Access ngăn chặn truy cập ngoài mong muốn", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/permissions%20block%20all%20publicj%20access%20on.png")
        ],
        images_en=[
            ("Amazon S3 Console - Bucket Versioning Enabled protecting Terraform State", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/bucket%20verioning%20enable.png"),
            ("Amazon S3 Console - Server-side Default Encryption SSE-S3", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/default%20encrytion%20.png"),
            ("Amazon S3 Console - Block All Public Access preventing unauthorized exposure", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.2-versioning-encryption-public-access/permissions%20block%20all%20publicj%20access%20on.png")
        ],
        weight=2
    )

    # 5.2.3
    write_section(
        p / "5.2.3-terraform-state-locking",
        "5.2.3",
        "Cấu hình Terraform State Locking",
        "Configure Terraform State Locking",
        "`scripts/init-platform.sh`, `scripts/init-workload-local.sh`, `cicd/buildspec-plan.yml`, `cicd/buildspec-apply.yml`",
        """Project sử dụng S3 backend lock file qua `use_lockfile=true`. Cả platform, workload local init, Terraform Plan và Terraform Apply đều truyền tùy chọn này khi chạy `terraform init -reconfigure`.

### Backend locking

```bash
-backend-config="encrypt=true" \\
-backend-config="use_lockfile=true"
```

**Mục tiêu**: Tránh hai tiến trình Terraform đồng thời sửa cùng một state tại cùng thời điểm.""",
        """The project uses S3 native backend lock files via `use_lockfile=true`. Platform, local workload init, Terraform Plan, and Terraform Apply all supply this setting during `terraform init -reconfigure`.

### Backend Locking

```bash
-backend-config="encrypt=true" \\
-backend-config="use_lockfile=true"
```

**Objective**: Prevents two simultaneous Terraform processes from mutating the same remote state file concurrently.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )

    # 5.2.4
    write_section(
        p / "5.2.4-declare-terraform-backend",
        "5.2.4",
        "Khai báo Terraform Backend",
        "Declare Terraform Backend",
        "`platform/backend.tf`, `workload/backend.tf`, `scripts/init-platform.sh`, `scripts/init-workload-local.sh`",
        """Hai layer platform và workload dùng backend S3 rỗng trong mã nguồn, sau đó nhận bucket, key và Region từ lệnh init. Platform dùng key `platform/terraform.tfstate`; workload dùng key `workload/terraform.tfstate`.

### Lấy output bootstrap và init Platform

```bash
cd ~/fcaj-aws-devsecops/bootstrap
export TF_STATE_BUCKET="$(terraform output -raw terraform_state_bucket)"
export PIPELINE_ARTIFACT_BUCKET="$(terraform output -raw pipeline_artifact_bucket)"
export AWS_REGION="ap-southeast-1"
cd ..
echo "$TF_STATE_BUCKET"
echo "$PIPELINE_ARTIFACT_BUCKET"
bash scripts/init-platform.sh
```

> [!WARNING]
> `scripts/init-platform.sh` dùng `terraform -chdir=platform`, vì vậy chạy script từ repository root. Nếu đang đứng trong `platform/` rồi chạy script, Terraform có thể tìm nhầm `platform/platform`.

### scripts/init-platform.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
: "${TF_STATE_BUCKET:?Set TF_STATE_BUCKET to bootstrap output}"
: "${AWS_REGION:=ap-southeast-1}"

terraform -chdir=platform init -reconfigure \\
  -backend-config="bucket=${TF_STATE_BUCKET}" \\
  -backend-config="key=platform/terraform.tfstate" \\
  -backend-config="region=${AWS_REGION}" \\
  -backend-config="encrypt=true" \\
  -backend-config="use_lockfile=true"
```

### scripts/init-workload-local.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
: "${TF_STATE_BUCKET:?Set TF_STATE_BUCKET to bootstrap output}"
: "${AWS_REGION:=ap-southeast-1}"

terraform -chdir=workload init -reconfigure \\
  -backend-config="bucket=${TF_STATE_BUCKET}" \\
  -backend-config="key=workload/terraform.tfstate" \\
  -backend-config="region=${AWS_REGION}" \\
  -backend-config="encrypt=true" \\
  -backend-config="use_lockfile=true"
```""",
        """Both platform and workload layers declare empty S3 backend blocks in source code, dynamically receiving bucket, key, and Region during initialization. Platform uses key `platform/terraform.tfstate`; workload uses key `workload/terraform.tfstate`.

### Extract Bootstrap Outputs and Initialize Platform

```bash
cd ~/fcaj-aws-devsecops/bootstrap
export TF_STATE_BUCKET="$(terraform output -raw terraform_state_bucket)"
export PIPELINE_ARTIFACT_BUCKET="$(terraform output -raw pipeline_artifact_bucket)"
export AWS_REGION="ap-southeast-1"
cd ..
echo "$TF_STATE_BUCKET"
echo "$PIPELINE_ARTIFACT_BUCKET"
bash scripts/init-platform.sh
```

> [!WARNING]
> `scripts/init-platform.sh` uses `terraform -chdir=platform`, so it must be run from the repository root. If run from inside `platform/`, Terraform may resolve directory paths incorrectly as `platform/platform`.

### scripts/init-platform.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
: "${TF_STATE_BUCKET:?Set TF_STATE_BUCKET to bootstrap output}"
: "${AWS_REGION:=ap-southeast-1}"

terraform -chdir=platform init -reconfigure \\
  -backend-config="bucket=${TF_STATE_BUCKET}" \\
  -backend-config="key=platform/terraform.tfstate" \\
  -backend-config="region=${AWS_REGION}" \\
  -backend-config="encrypt=true" \\
  -backend-config="use_lockfile=true"
```

### scripts/init-workload-local.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
: "${TF_STATE_BUCKET:?Set TF_STATE_BUCKET to bootstrap output}"
: "${AWS_REGION:=ap-southeast-1}"

terraform -chdir=workload init -reconfigure \\
  -backend-config="bucket=${TF_STATE_BUCKET}" \\
  -backend-config="key=workload/terraform.tfstate" \\
  -backend-config="region=${AWS_REGION}" \\
  -backend-config="encrypt=true" \\
  -backend-config="use_lockfile=true"
```""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )

    # 5.2.5
    write_section(
        p / "5.2.5-verify-terraform-state",
        "5.2.5",
        "Kiểm tra Terraform State",
        "Verify Terraform State",
        "AWS S3 & Terraform CLI",
        """Sau khi init/apply, kiểm tra state bằng Terraform CLI và trên S3 Console. Workload và platform phải dùng hai key riêng trong cùng state bucket.

### Kiểm tra State và Lock

```bash
terraform -chdir=platform state list
aws s3 ls "s3://${TF_STATE_BUCKET}/platform/"
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/"

# Kiểm tra lock file khi nghi ngờ có execution chồng nhau
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/" | grep tflock || true
```

> [!NOTE]
> Nếu TerraformPlan báo `Error acquiring the state lock` trong lúc một TerraformApply khác đang chạy, hãy chờ execution Apply hoàn tất rồi retry. Tuyệt đối không xóa `.tflock` khi vẫn còn tiến trình Terraform hoặc CodeBuild đang thao tác với state.""",
        """After init and apply, verify state using Terraform CLI and the S3 Console. Workload and platform must maintain separated state keys within the shared state bucket.

### Verify State and Lockfile

```bash
terraform -chdir=platform state list
aws s3 ls "s3://${TF_STATE_BUCKET}/platform/"
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/"

# Inspect lock files if conflicting executions are suspected
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/" | grep tflock || true
```

> [!NOTE]
> If TerraformPlan reports `Error acquiring the state lock` while a TerraformApply execution is active, wait for Apply to complete, then retry. Never remove a `.tflock` file while Terraform or CodeBuild is actively manipulating state.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    # Parent 5.2
    write_parent(
        p,
        "5.2",
        "Khởi tạo Terraform Backend & quản lý State",
        "Terraform Backend Initialization & State Management",
        "Chương này hướng dẫn tạo S3 Backend bảo mật cao cho Terraform State với Versioning, Encryption, Block Public Access và cơ chế State Locking bảo đảm tính toàn vẹn của hạ tầng.",
        "This chapter guides through provisioning a secure S3 Terraform remote backend with Versioning, Server-Side Encryption, Block Public Access, and native state locking.",
        sub_list,
        2
    )

def build_5_3():
    p = BASE_DIR / "5.3-IAM-Secrets"
    sub_list = [
        {"num": "5.3.1", "dir": "5.3.1-create-codepipeline-role", "title_vi": "Tạo CodePipelineRole", "title_en": "Create CodePipelineRole", "summary_vi": "Role điều phối chuỗi cung ứng CI/CD trust codepipeline.amazonaws.com", "summary_en": "CI/CD orchestration role trusting codepipeline.amazonaws.com"},
        {"num": "5.3.2", "dir": "5.3.2-create-scanbuild-role", "title_vi": "Tạo ScanBuildRole", "title_en": "Create ScanBuildRole", "summary_vi": "Role thực thi validate và security scan với quyền hạn đọc có giới hạn", "summary_en": "Execution role for validate and security scan with restricted read privileges"},
        {"num": "5.3.3", "dir": "5.3.3-create-terraform-plan-role", "title_vi": "Tạo TerraformPlanRole", "title_en": "Create TerraformPlanRole", "summary_vi": "Role lập kế hoạch hạ tầng chỉ đọc hiện trạng EC2/VPC", "summary_en": "Read-only planning role limited to EC2 Describe* and instance profile inspection"},
        {"num": "5.3.4", "dir": "5.3.4-create-terraform-deploy-role", "title_vi": "Tạo TerraformDeployRole", "title_en": "Create TerraformDeployRole", "summary_vi": "Role duy nhất có quyền biến đổi hạ tầng EC2/VPC và PassRole EC2DemoRole", "summary_en": "Deployment role authorized for EC2/VPC mutation and PassRole to EC2DemoRole"},
        {"num": "5.3.5", "dir": "5.3.5-configure-ssm-parameter-store", "title_vi": "Cấu hình AWS Systems Manager Parameter Store", "title_en": "Configure AWS Systems Manager Parameter Store", "summary_vi": "Tạo token ngẫu nhiên lưu trữ an toàn dạng SecureString", "summary_en": "Generate random token stored as encrypted SecureString in SSM"},
        {"num": "5.3.6", "dir": "5.3.6-securestring-secret-management", "title_vi": "Lưu Secret bằng SecureString", "title_en": "Secure Secrets Management via SecureString", "summary_vi": "Inject secret vào CodeBuild bằng biến PARAMETER_STORE không in ra log", "summary_en": "Inject SSM secret into CodeBuild as PARAMETER_STORE without printing to logs"},
        {"num": "5.3.7", "dir": "5.3.7-verify-least-privilege-permissions", "title_vi": "Kiểm tra nguyên tắc Least Privilege", "title_en": "Verify Principle of Least Privilege", "summary_vi": "Xác minh phân tách đặc quyền giữa 4 CI/CD roles và EC2 workload role", "summary_en": "Verify least-privilege role segregation between CI/CD roles and EC2 workload role"},
    ]

    # 5.3.1
    write_section(
        p / "5.3.1-create-codepipeline-role",
        "5.3.1",
        "Tạo CodePipelineRole",
        "Create CodePipelineRole",
        "`platform/iam.tf`, `iam-policy/codepipeline-policy.json.tftpl`",
        """Role cho AWS CodePipeline, trust principal `codepipeline.amazonaws.com` và được gắn policy thao tác artifact bucket, CodeConnections, CodeBuild và SNS approval notification.

```hcl
resource "aws_iam_role" "codepipeline" {
  name               = "${local.name}-CodePipelineRole"
  assume_role_policy = data.aws_iam_policy_document.codepipeline_assume.json
}
```""",
        """Execution role for AWS CodePipeline, trusting principal `codepipeline.amazonaws.com` and granted policies for artifact bucket operations, CodeConnections, CodeBuild start/get builds, and SNS approval notifications.

```hcl
resource "aws_iam_role" "codepipeline" {
  name               = "${local.name}-CodePipelineRole"
  assume_role_policy = data.aws_iam_policy_document.codepipeline_assume.json
}
```""",
        images_vi=[
            ("AWS IAM Console - Cấu hình CodePipelineRole và trust relationship", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.1-codepipeline-role.png")
        ],
        images_en=[
            ("AWS IAM Console - CodePipelineRole configuration and trust relationships", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.1-codepipeline-role.png")
        ],
        weight=1
    )

    # 5.3.2
    write_section(
        p / "5.3.2-create-scanbuild-role",
        "5.3.2",
        "Tạo ScanBuildRole",
        "Create ScanBuildRole",
        "`platform/iam.tf`, `iam-policy/scan-build-policy.json.tftpl`",
        """Role cho CodeBuild validate/security. Policy chỉ cho phép ghi CloudWatch Logs, đọc pipeline artifact và đọc đúng SSM parameter demo.

```hcl
resource "aws_iam_role" "scan_build" {
  name               = "${local.name}-ScanBuildRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```""",
        """Role for CodeBuild validate/security tasks. Policy permits only writing CloudWatch logs, reading pipeline artifacts, and reading the single designated demo SSM parameter.

```hcl
resource "aws_iam_role" "scan_build" {
  name               = "${local.name}-ScanBuildRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```""",
        images_vi=[
            ("AWS IAM Console - Cấu hình ScanBuildRole và policy quyền đọc hạn chế", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.2-scan-build-role.png")
        ],
        images_en=[
            ("AWS IAM Console - ScanBuildRole configuration and restricted read policy", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.2-scan-build-role.png")
        ],
        weight=2
    )

    # 5.3.3
    write_section(
        p / "5.3.3-create-terraform-plan-role",
        "5.3.3",
        "Tạo TerraformPlanRole",
        "Create TerraformPlanRole",
        "`platform/iam.tf`, `iam-policy/terraform-plan-policy.json.tftpl`",
        """Role cho Terraform Plan. Ngoài log/artifact/state, role có `ec2:Describe*` và `iam:GetInstanceProfile` để đọc hiện trạng hạ tầng/instance profile khi lập plan; role này không có quyền mutate workload.

```hcl
resource "aws_iam_role" "terraform_plan" {
  name               = "${local.name}-TerraformPlanRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```""",
        """Role for Terraform Plan. Beyond log/artifact/state access, the role holds `ec2:Describe*` and `iam:GetInstanceProfile` to inspect live infrastructure and instance profiles during planning; it holds no permission to mutate workloads.

```hcl
resource "aws_iam_role" "terraform_plan" {
  name               = "${local.name}-TerraformPlanRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```""",
        images_vi=[
            ("AWS IAM Console - Cấu hình TerraformPlanRole quyền đọc chỉ hạn chế EC2 Describe*", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.3-terraform-plan-role.png")
        ],
        images_en=[
            ("AWS IAM Console - TerraformPlanRole read-only policy for EC2 Describe*", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.3-terraform-plan-role.png")
        ],
        weight=3
    )

    # 5.3.4
    write_section(
        p / "5.3.4-create-terraform-deploy-role",
        "5.3.4",
        "Tạo TerraformDeployRole",
        "Create TerraformDeployRole",
        "`platform/iam.tf`, `iam-policy/terraform-deploy-policy.json.tftpl`",
        """Role cho Terraform Apply. Policy cho phép các API EC2/VPC cần thiết để tạo/xóa tài nguyên Workshop, `ec2:MonitorInstances`/`UnmonitorInstances` cho detailed monitoring, `iam:GetInstanceProfile` và `iam:PassRole` được scope tới `EC2DemoRole`, cùng quyền state/artifact cần thiết.

```hcl
resource "aws_iam_role" "terraform_deploy" {
  name               = "${local.name}-TerraformDeployRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```""",
        """Role for Terraform Apply. Policy authorizes required EC2/VPC APIs for provisioning/teardown, `ec2:MonitorInstances`/`UnmonitorInstances` for detailed monitoring, `iam:GetInstanceProfile` and scoped `iam:PassRole` to `EC2DemoRole`, alongside necessary remote state and artifact access.

```hcl
resource "aws_iam_role" "terraform_deploy" {
  name               = "${local.name}-TerraformDeployRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```""",
        images_vi=[
            ("AWS IAM Console - Cấu hình TerraformDeployRole giới hạn quyền deploy EC2/VPC", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.4-terraform-deploy-role.png")
        ],
        images_en=[
            ("AWS IAM Console - TerraformDeployRole scoped deployment policies for EC2/VPC", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.4-terraform-deploy-role.png")
        ],
        weight=4
    )

    # 5.3.5
    write_section(
        p / "5.3.5-configure-ssm-parameter-store",
        "5.3.5",
        "Cấu hình AWS Systems Manager Parameter Store",
        "Configure AWS Systems Manager Parameter Store",
        "`platform/secrets_notifications.tf`, `platform/locals.tf`",
        """Platform tạo một random token và lưu tại SSM Parameter Store với type `SecureString`. Path được tạo theo mẫu `/<project>/<environment>/demo_token`.

### SSM SecureString

```hcl
resource "aws_ssm_parameter" "demo_token" {
  name        = local.demo_token_path
  description = "Demo SecureString consumed by CodeBuild without printing the value."
  type        = "SecureString"
  value       = random_password.demo_token.result
  overwrite   = true
}
```""",
        """The platform generates a random token stored in SSM Parameter Store as type `SecureString`. The path follows the pattern `/<project>/<environment>/demo_token`.

### SSM SecureString Declaration

```hcl
resource "aws_ssm_parameter" "demo_token" {
  name        = local.demo_token_path
  description = "Demo SecureString consumed by CodeBuild without printing the value."
  type        = "SecureString"
  value       = random_password.demo_token.result
  overwrite   = true
}
```""",
        images_vi=[
            ("AWS Systems Manager Parameter Store - Quản lý Secret SecureString", "/images/5-Workshop/5.3-IAM-Secrets/5.3.2-ssm-parameter-store/check%20SSM.png")
        ],
        images_en=[
            ("AWS Systems Manager Parameter Store - SecureString Secret Management", "/images/5-Workshop/5.3-IAM-Secrets/5.3.2-ssm-parameter-store/check%20SSM.png")
        ],
        weight=5
    )

    # 5.3.6
    write_section(
        p / "5.3.6-securestring-secret-management",
        "5.3.6",
        "Lưu Secret bằng SecureString",
        "Secure Secrets Management via SecureString",
        "`platform/codebuild.tf`, `cicd/buildspec-validate-security.yml`",
        """CodeBuild inject parameter vào biến `DEMO_TOKEN` bằng environment variable type `PARAMETER_STORE`. Build chỉ xác minh biến tồn tại và cố ý không in giá trị ra log:

```hcl
environment_variable {
  name  = "DEMO_TOKEN"
  value = aws_ssm_parameter.demo_token.name
  type  = "PARAMETER_STORE"
}
```

### buildspec snippet

```bash
test -n "${DEMO_TOKEN:-}" || { echo "SecureString injection failed"; exit 1; }
echo "SSM SecureString was injected successfully; value intentionally not printed."
```""",
        """CodeBuild injects the secret into variable `DEMO_TOKEN` via environment variable type `PARAMETER_STORE`. The build script validates token presence without printing the value:

```hcl
environment_variable {
  name  = "DEMO_TOKEN"
  value = aws_ssm_parameter.demo_token.name
  type  = "PARAMETER_STORE"
}
```

### buildspec snippet

```bash
test -n "${DEMO_TOKEN:-}" || { echo "SecureString injection failed"; exit 1; }
echo "SSM SecureString was injected successfully; value intentionally not printed."
```""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=6
    )

    # 5.3.7
    write_section(
        p / "5.3.7-verify-least-privilege-permissions",
        "5.3.7",
        "Kiểm tra nguyên tắc Least Privilege",
        "Verify Principle of Least Privilege",
        "`iam-policy/`",
        """Least Privilege được thể hiện qua việc tách 4 CI/CD service role theo trách nhiệm và một EC2 workload role riêng. ScanBuildRole không có quyền deploy; TerraformPlanRole chủ yếu đọc; TerraformDeployRole chỉ có quyền mutation cần cho Workshop; EC2DemoRole chỉ gắn `AmazonSSMManagedInstanceCore` để quản trị instance qua Session Manager.

- **CodePipelineRole**: orchestration, artifact, CodeConnections, CodeBuild, SNS.
- **ScanBuildRole**: log + read artifact + read đúng SSM parameter.
- **TerraformPlanRole**: state/artifact + EC2 Describe* + đọc đúng EC2 Instance Profile.
- **TerraformDeployRole**: state/artifact + EC2/VPC mutation + PassRole EC2DemoRole + detailed monitoring.

### Xác minh EC2 IAM Role/Instance Profile

```bash
aws iam get-role \\
  --role-name fcaj-devsecops-dev-EC2DemoRole \\
  --query 'Role.Arn' --output text

aws iam get-instance-profile \\
  --instance-profile-name fcaj-devsecops-dev-EC2DemoProfile \\
  --query 'InstanceProfile.{Name:InstanceProfileName,Arn:Arn}' \\
  --output table
```

> [!NOTE]
> Nếu vừa sửa `platform/iam.tf` hoặc `iam-policy/`, cần `terraform plan/apply` lại layer platform để policy thật trên AWS được cập nhật trước khi chạy pipeline.""",
        """Least Privilege is demonstrated through strict separation across 4 CI/CD service roles and 1 EC2 workload role. ScanBuildRole cannot deploy; TerraformPlanRole is primarily read-only; TerraformDeployRole only holds mutation permissions required for the workshop; EC2DemoRole only attaches `AmazonSSMManagedInstanceCore` for administration via Session Manager.

- **CodePipelineRole**: orchestration, artifacts, CodeConnections, CodeBuild, SNS.
- **ScanBuildRole**: logs + read artifacts + read designated SSM parameter.
- **TerraformPlanRole**: state/artifacts + EC2 Describe* + inspect EC2 Instance Profile.
- **TerraformDeployRole**: state/artifacts + EC2/VPC mutation + PassRole EC2DemoRole + detailed monitoring.

### Verify EC2 IAM Role / Instance Profile

```bash
aws iam get-role \\
  --role-name fcaj-devsecops-dev-EC2DemoRole \\
  --query 'Role.Arn' --output text

aws iam get-instance-profile \\
  --instance-profile-name fcaj-devsecops-dev-EC2DemoProfile \\
  --query 'InstanceProfile.{Name:InstanceProfileName,Arn:Arn}' \\
  --output table
```

> [!NOTE]
> If modifications are made to `platform/iam.tf` or `iam-policy/`, re-run `terraform plan/apply` on the platform layer so AWS IAM policies are updated before the pipeline executes.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=7
    )

    # Parent 5.3
    write_parent(
        p,
        "5.3",
        "Cấu hình IAM & quản lý Secrets",
        "IAM Configuration & Secrets Management",
        "Chương này hướng dẫn thiết lập hệ thống IAM Role phân quyền chặt chẽ theo nguyên tắc Least Privilege và quản lý thông tin bí mật an toàn với AWS Systems Manager Parameter Store.",
        "This chapter covers establishing least-privilege IAM roles and managing secrets securely using AWS Systems Manager Parameter Store.",
        sub_list,
        3
    )

def build_5_4():
    p = BASE_DIR / "5.4-GitHub-CodePipeline"
    sub_list = [
        {"num": "5.4.1", "dir": "5.4.1-prepare-repo-branch", "title_vi": "Chuẩn bị Repository và Branch", "title_en": "Prepare Repository and Branch", "summary_vi": "Cấu hình biến GitHub owner, repo và branch main cho pipeline", "summary_en": "Configure GitHub owner, repo name, and main branch for CodePipeline"},
        {"num": "5.4.2", "dir": "5.4.2-create-codeconnections", "title_vi": "Tạo AWS CodeConnections", "title_en": "Create AWS CodeConnections", "summary_vi": "Khởi tạo resource aws_codeconnections_connection ở trạng thái PENDING", "summary_en": "Provision aws_codeconnections_connection resource initially in PENDING status"},
        {"num": "5.4.3", "dir": "5.4.3-connect-github-repo", "title_vi": "Kết nối GitHub Repository", "title_en": "Connect GitHub Repository", "summary_vi": "Thao tác trên AWS Console xác thực GitHub App chuyển sang AVAILABLE", "summary_en": "Authorize GitHub App via AWS Console transitioning connection to AVAILABLE"},
        {"num": "5.4.4", "dir": "5.4.4-s3-artifact-bucket", "title_vi": "Tạo Amazon S3 Pipeline Artifact Bucket", "title_en": "Create Amazon S3 Pipeline Artifact Bucket", "summary_vi": "Tạo bucket lưu trữ artifact trung gian với lifecycle 30 ngày", "summary_en": "Create pipeline artifact bucket with 30-day lifecycle expiration"},
        {"num": "5.4.5", "dir": "5.4.5-create-codepipeline", "title_vi": "Khởi tạo AWS CodePipeline", "title_en": "Initialize AWS CodePipeline", "summary_vi": "Định nghĩa pipeline V1 chế độ SUPERSEDED liên kết toàn diện 7 stage", "summary_en": "Declare V1 SUPERSEDED pipeline orchestrating 7 sequential delivery stages"},
        {"num": "5.4.6", "dir": "5.4.6-verify-source-trigger", "title_vi": "Kiểm tra Source Trigger", "title_en": "Verify Source Trigger", "summary_vi": "Commit push mã nguồn và xác minh CodePipeline tự động kích hoạt", "summary_en": "Push commit to main branch and verify automated webhook execution"},
    ]

    # 5.4.1
    write_section(
        p / "5.4.1-prepare-repo-branch",
        "5.4.1",
        "Chuẩn bị Repository và Branch",
        "Prepare Repository and Branch",
        "`platform/variables.tf`, `platform/locals.tf`",
        """GitHub owner, repository và branch được truyền qua biến Terraform. `local.repo_full_name` ghép owner/repo để cấp cho Source action. Branch mặc định là `main`.""",
        """GitHub owner, repository, and branch are passed via Terraform variables. `local.repo_full_name` concatenates owner/repo for the Source action. Branch defaults to `main`.""",
        images_vi=[
            ("Cấu hình file terraform.tfvars với repo GitHub và branch main", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.1-prepare-repo-branch/chuan%20bi%20repo%20v%C3%A0%20branch.png")
        ],
        images_en=[
            ("Configure terraform.tfvars with GitHub repository and main branch parameters", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.1-prepare-repo-branch/chuan%20bi%20repo%20v%C3%A0%20branch.png")
        ],
        weight=1
    )

    # 5.4.2
    write_section(
        p / "5.4.2-create-codeconnections",
        "5.4.2",
        "Tạo AWS CodeConnections",
        "Create AWS CodeConnections",
        "`platform/pipeline.tf`",
        """```hcl
resource "aws_codeconnections_connection" "github" {
  name          = "${local.name}-github"
  provider_type = "GitHub"
}
```

Terraform tạo connection object. Sau khi apply, connection có thể ở trạng thái `PENDING` và cần hoàn tất authorization với GitHub trên AWS Console.

### Kiểm tra CodeConnection

```bash
cd ~/fcaj-aws-devsecops/platform
terraform output
terraform output github_connection_status
CONNECTION_ARN="$(terraform output -raw github_connection_arn)"
aws codeconnections get-connection \\
  --connection-arn "$CONNECTION_ARN" \\
  --query 'Connection.ConnectionStatus' \\
  --output text
```

> [!NOTE]
> `PENDING` ngay sau Terraform Apply là trạng thái bình thường. Hoàn tất Update pending connection / Authorize GitHub trên Console để trạng thái chuyển `AVAILABLE`.""",
        """```hcl
resource "aws_codeconnections_connection" "github" {
  name          = "${local.name}-github"
  provider_type = "GitHub"
}
```

Terraform provisions the connection object. Immediately post-apply, the connection sits in `PENDING` status awaiting manual OAuth authorization with GitHub in the AWS Console.

### Inspect CodeConnection Status

```bash
cd ~/fcaj-aws-devsecops/platform
terraform output
terraform output github_connection_status
CONNECTION_ARN="$(terraform output -raw github_connection_arn)"
aws codeconnections get-connection \\
  --connection-arn "$CONNECTION_ARN" \\
  --query 'Connection.ConnectionStatus' \\
  --output text
```

> [!NOTE]
> `PENDING` status immediately following Terraform Apply is expected behavior. Complete Update pending connection / Authorize GitHub in the AWS Console to transition to `AVAILABLE`.""",
        screenshot_vi=None,
        screenshot_en=None,
        images_vi=[
            ("AWS CodeConnections - Kết nối GitHub ở trạng thái PENDING sau khi apply Terraform", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.2-create-codeconnections/github%20pending.png")
        ],
        images_en=[
            ("AWS CodeConnections - GitHub connection in PENDING status following Terraform apply", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.2-create-codeconnections/github%20pending.png")
        ],
        weight=2
    )

    # 5.4.3
    write_section(
        p / "5.4.3-connect-github-repo",
        "5.4.3",
        "Kết nối GitHub Repository",
        "Connect GitHub Repository",
        "AWS Management Console",
        """Trong AWS Console, mở **Developer Tools > Connections**, chọn connection do Terraform tạo, thực hiện **Update pending connection** và authorize repository. Khi hoàn tất, status cần chuyển thành **AVAILABLE**.""",
        """In the AWS Console, navigate to **Developer Tools > Connections**, select the connection created by Terraform, click **Update pending connection**, and authorize the GitHub App and repository access. Once authorized, the status updates to **AVAILABLE**.""",
        images_vi=[
            ("AWS CodeConnections - Hoàn tất kết nối GitHub repository chuyển sang trạng thái AVAILABLE", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.3-connect-github-repo/connect%20git%20hub%20repo.png")
        ],
        images_en=[
            ("AWS CodeConnections - Complete GitHub repository handshake showing AVAILABLE status", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.3-connect-github-repo/connect%20git%20hub%20repo.png")
        ],
        weight=3
    )

    # 5.4.4
    write_section(
        p / "5.4.4-s3-artifact-bucket",
        "5.4.4",
        "Tạo Amazon S3 Pipeline Artifact Bucket",
        "Create Amazon S3 Pipeline Artifact Bucket",
        "`bootstrap/main.tf`, `bootstrap/outputs.tf`",
        """Artifact bucket được tạo ngay trong bootstrap, tách biệt với Terraform State. Bucket bật Versioning, SSE-S3, Block Public Access, BucketOwnerEnforced và lifecycle xóa artifact cũ sau 30 ngày; noncurrent version hết hạn sau 7 ngày.

### Khai báo Lifecycle Configuration

```hcl
resource "aws_s3_bucket_lifecycle_configuration" "pipeline_artifacts" {
  bucket = aws_s3_bucket.pipeline_artifacts.id
  rule {
    id     = "expire-old-pipeline-artifacts"
    status = "Enabled"
    filter {}
    expiration {
      days = 30
    }
    noncurrent_version_expiration {
      noncurrent_days = 7
    }
  }
}
```""",
        """The artifact bucket is created during bootstrap, fully decoupled from Terraform State. The bucket enforces Versioning, SSE-S3, Block Public Access, BucketOwnerEnforced, and lifecycle rules expiring old artifacts after 30 days (noncurrent versions after 7 days).

### Lifecycle Configuration

```hcl
resource "aws_s3_bucket_lifecycle_configuration" "pipeline_artifacts" {
  bucket = aws_s3_bucket.pipeline_artifacts.id
  rule {
    id     = "expire-old-pipeline-artifacts"
    status = "Enabled"
    filter {}
    expiration {
      days = 30
    }
    noncurrent_version_expiration {
      noncurrent_days = 7
    }
  }
}
```""",
        images_vi=[
            ("Khai báo tài nguyên S3 Artifact Bucket trong bootstrap/main.tf", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%201.png"),
            ("Khai báo output pipeline_artifact_bucket trong bootstrap/outputs.tf", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%202.png")
        ],
        images_en=[
            ("S3 Artifact Bucket resource configuration in bootstrap/main.tf", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%201.png"),
            ("Export pipeline_artifact_bucket output in bootstrap/outputs.tf", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%202.png")
        ],
        weight=4
    )

    # 5.4.5
    write_section(
        p / "5.4.5-create-codepipeline",
        "5.4.5",
        "Khởi tạo AWS CodePipeline",
        "Initialize AWS CodePipeline",
        "`platform/pipeline.tf`",
        """Pipeline dùng loại V1, execution mode `SUPERSEDED`, artifact store là S3 artifact bucket. Các stage được khai báo theo thứ tự: `Source`, `ValidateTest`, `SecurityScan`, `TerraformPlan`, `ManualApproval`, `TerraformApply` và `PostDeployVerification`.

### CodePipeline definition

```hcl
resource "aws_codepipeline" "main" {
  name          = "${local.name}-pipeline"
  role_arn      = aws_iam_role.codepipeline.arn
  pipeline_type = "V1"
  execution_mode = "SUPERSEDED"

  artifact_store {
    location = var.pipeline_artifact_bucket
    type     = "S3"
  }

  stage {
    name = "Source"
    action {
      name             = "GitHubSource"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = "1"
      output_artifacts = ["SourceOutput"]
      configuration = {
        ConnectionArn    = aws_codeconnections_connection.github.arn
        FullRepositoryId = local.repo_full_name
        BranchName       = var.github_branch
        DetectChanges    = "true"
      }
    }
  }

  stage {
    name = "ValidateTest"
    action {
      name            = "ValidateAndUnitTest"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.validate_security.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "validate", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "SecurityScan"
    action {
      name            = "ShiftLeftSecurity"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.validate_security.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "security", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "TerraformPlan"
    action {
      name             = "CreatePlan"
      category         = "Build"
      owner            = "AWS"
      provider         = "CodeBuild"
      version          = "1"
      input_artifacts  = ["SourceOutput"]
      output_artifacts = ["PlanOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.terraform_plan.name
      }
    }
  }

  stage {
    name = "ManualApproval"
    action {
      name     = "ReviewTerraformPlan"
      category = "Approval"
      owner    = "AWS"
      provider = "Manual"
      version  = "1"
      configuration = {
        NotificationArn = aws_sns_topic.pipeline.arn
        CustomData      = "Review PlanOutput/plan.txt. Approve only if the planned infrastructure change is expected and safe."
      }
    }
  }

  stage {
    name = "TerraformApply"
    action {
      name            = "ApplyApprovedPlan"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput", "PlanOutput"]
      configuration = {
        ProjectName   = aws_codebuild_project.terraform_apply_smoke.name
        PrimarySource = "SourceOutput"
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "apply", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "PostDeployVerification"
    action {
      name            = "SmokeTest"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.terraform_apply_smoke.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "smoke", type = "PLAINTEXT" }
        ])
      }
    }
  }

  depends_on = [aws_iam_role_policy.codepipeline]
}
```""",
        """The pipeline uses V1 type, `SUPERSEDED` execution mode, and the S3 artifact bucket as artifact store. Stages are declared sequentially: `Source`, `ValidateTest`, `SecurityScan`, `TerraformPlan`, `ManualApproval`, `TerraformApply`, and `PostDeployVerification`.

### CodePipeline Definition

```hcl
resource "aws_codepipeline" "main" {
  name          = "${local.name}-pipeline"
  role_arn      = aws_iam_role.codepipeline.arn
  pipeline_type = "V1"
  execution_mode = "SUPERSEDED"

  artifact_store {
    location = var.pipeline_artifact_bucket
    type     = "S3"
  }

  stage {
    name = "Source"
    action {
      name             = "GitHubSource"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = "1"
      output_artifacts = ["SourceOutput"]
      configuration = {
        ConnectionArn    = aws_codeconnections_connection.github.arn
        FullRepositoryId = local.repo_full_name
        BranchName       = var.github_branch
        DetectChanges    = "true"
      }
    }
  }

  stage {
    name = "ValidateTest"
    action {
      name            = "ValidateAndUnitTest"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.validate_security.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "validate", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "SecurityScan"
    action {
      name            = "ShiftLeftSecurity"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.validate_security.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "security", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "TerraformPlan"
    action {
      name             = "CreatePlan"
      category         = "Build"
      owner            = "AWS"
      provider         = "CodeBuild"
      version          = "1"
      input_artifacts  = ["SourceOutput"]
      output_artifacts = ["PlanOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.terraform_plan.name
      }
    }
  }

  stage {
    name = "ManualApproval"
    action {
      name     = "ReviewTerraformPlan"
      category = "Approval"
      owner    = "AWS"
      provider = "Manual"
      version  = "1"
      configuration = {
        NotificationArn = aws_sns_topic.pipeline.arn
        CustomData      = "Review PlanOutput/plan.txt. Approve only if the planned infrastructure change is expected and safe."
      }
    }
  }

  stage {
    name = "TerraformApply"
    action {
      name            = "ApplyApprovedPlan"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput", "PlanOutput"]
      configuration = {
        ProjectName   = aws_codebuild_project.terraform_apply_smoke.name
        PrimarySource = "SourceOutput"
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "apply", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "PostDeployVerification"
    action {
      name            = "SmokeTest"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.terraform_apply_smoke.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "smoke", type = "PLAINTEXT" }
        ])
      }
    }
  }

  depends_on = [aws_iam_role_policy.codepipeline]
}
```""",
        images_vi=[
            ("AWS CodePipeline Console - Giao diện trực quan chuỗi CI/CD 7 giai đoạn hoạt động thành công", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.5-create-codepipeline/%E1%BA%A2nh%20ch%E1%BB%A5p%20m%C3%A0n%20h%C3%ACnh%202026-09-16%20024115.png")
        ],
        images_en=[
            ("AWS CodePipeline Console - End-to-end 7-stage CI/CD pipeline execution overview", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.5-create-codepipeline/%E1%BA%A2nh%20ch%E1%BB%A5p%20m%C3%A0n%20h%C3%ACnh%202026-09-16%20024115.png")
        ],
        weight=5
    )

    # 5.4.6
    write_section(
        p / "5.4.6-verify-source-trigger",
        "5.4.6",
        "Kiểm tra Source Trigger",
        "Verify Source Trigger",
        "AWS CodePipeline & GitHub",
        """Source action dùng provider `CodeStarSourceConnection`, `DetectChanges=true`. Sau khi connection `AVAILABLE`, một commit mới trên branch `main` phải tự tạo pipeline execution mới.

### Trigger/retrigger pipeline

```bash
cd ~/fcaj-aws-devsecops
git status
git add -A
git commit -m "workshop: trigger pipeline"
git push

# Nếu chỉ cần retrigger mà không đổi file
git commit --allow-empty -m "chore: retrigger pipeline"
git push
```

> [!NOTE]
> Execution đã `FAILED` trước lúc GitHub connection được verify sẽ không tự chạy lại. Sau khi connection `AVAILABLE`, push commit mới hoặc chọn **Release change** trên console để tạo execution mới.""",
        """The Source action utilizes provider `CodeStarSourceConnection` with `DetectChanges=true`. Once the connection reaches `AVAILABLE` status, pushing commits to the `main` branch automatically triggers a new pipeline execution.

### Trigger / Retrigger Pipeline

```bash
cd ~/fcaj-aws-devsecops
git status
git add -A
git commit -m "workshop: trigger pipeline"
git push

# If retriggering without source modifications
git commit --allow-empty -m "chore: retrigger pipeline"
git push
```

> [!NOTE]
> Executions that `FAILED` prior to connection authorization will not automatically restart. After the connection turns `AVAILABLE`, push a new commit or click **Release change** in the console to initiate a run.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=6
    )

    # Parent 5.4
    write_parent(
        p,
        "5.4",
        "Kết nối GitHub với AWS CodePipeline",
        "Connect GitHub with AWS CodePipeline",
        "Chương này hướng dẫn tích hợp AWS CodeConnections với GitHub repository, cấu hình S3 Artifact Store và xây dựng chuỗi cung ứng AWS CodePipeline 7 giai đoạn tự động.",
        "This chapter covers establishing GitHub connections via AWS CodeConnections, configuring the S3 Artifact Store, and building the 7-stage automated AWS CodePipeline delivery flow.",
        sub_list,
        4
    )

if __name__ == "__main__":
    build_5_1()
    build_5_2()
    build_5_3()
    build_5_4()
    print("Modules 5.1 - 5.4 built successfully!")
