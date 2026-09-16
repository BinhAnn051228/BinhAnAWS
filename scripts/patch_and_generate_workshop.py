import sys
from pathlib import Path

BASE_DIR = Path(r"c:\Users\ASUS\Desktop\Năm cuối\Prj thực tập\BinhAnAWS")
sys.path.insert(0, str(BASE_DIR / "scripts"))

import update_workshop_images

def patch_5_1_to_5_4():
    path = BASE_DIR / "scripts" / "gen_module_5_1_to_5_4.py"
    content = path.read_text(encoding="utf-8")

    # 1. Update 5.1.1
    old_5_1_1 = """        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )

    # 5.1.2"""
    new_5_1_1 = """        images_vi=[
            ("AWS IAM Console - Cấp quyền AdministratorAccess cho tài khoản IAM", "/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A2nh%20ch%E1%BB%A5p%20c%E1%BA%A5p%20quy%E1%BB%81n%20cho%20t%C3%A0i%20kho%E1%BA%A3n%20IAM.png"),
            ("AWS CloudShell - Cấu hình AWS_REGION=ap-southeast-1 và kiểm tra get-caller-identity", "/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A3nh%20ch%E1%BB%A5p%20%C4%91%E1%BB%8Bnh%20t%C3%A0i%20kho%E1%BA%A3n%20v%C3%A0%20set%20region%20m%E1%BA%B7c%20%C4%91%E1%BB%8Bnh.png")
        ],
        images_en=[
            ("AWS IAM Console - Grant AdministratorAccess permissions to IAM user", "/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A2nh%20ch%E1%BB%A5p%20c%E1%BA%A5p%20quy%E1%BB%81n%20cho%20t%C3%A0i%20kho%E1%BA%A3n%20IAM.png"),
            ("AWS CloudShell - Set AWS_REGION=ap-southeast-1 and verify get-caller-identity", "/images/5-Workshop/5.1-Prepare-Environment/5.1.1-aws-account-region/%E1%BA%A3nh%20ch%E1%BB%A5p%20%C4%91%E1%BB%8Bnh%20t%C3%A0i%20kho%E1%BA%A3n%20v%C3%A0%20set%20region%20m%E1%BA%B7c%20%C4%91%E1%BB%8Bnh.png")
        ],
        weight=1
    )

    # 5.1.2"""
    if old_5_1_1 in content:
        content = content.replace(old_5_1_1, new_5_1_1, 1)

    # 2. Update 5.1.2
    old_5_1_2 = """        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )

    # 5.1.3"""
    new_5_1_2 = """        images_vi=[
            ("GitHub Repository - Cấu trúc repository fcaj-aws-devsecops trên branch main", "/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/%E1%BA%A3nh%20ch%E1%BB%A5p%20git%20repo.png"),
            ("AWS CloudShell - Clone GitHub repository vào CloudShell", "/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/clone%20git%20repo%20v%E1%BB%81%20aws%20cloudshell.png")
        ],
        images_en=[
            ("GitHub Repository - Project repository structure on branch main", "/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/%E1%BA%A3nh%20ch%E1%BB%A5p%20git%20repo.png"),
            ("AWS CloudShell - Clone GitHub repository into CloudShell", "/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/clone%20git%20repo%20v%E1%BB%81%20aws%20cloudshell.png")
        ],
        weight=2
    )

    # 5.1.3"""
    if old_5_1_2 in content:
        content = content.replace(old_5_1_2, new_5_1_2, 1)

    # 3. Update 5.1.5
    old_5_1_5 = """        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )"""
    new_5_1_5 = """        images_vi=[
            ("Sơ đồ quy trình thực thi AWS DevSecOps CI/CD Delivery Workflow", "/images/5-Workshop/5.1-Prepare-Environment/5.1.5-devsecops-workflow/workflow.png")
        ],
        images_en=[
            ("AWS DevSecOps CI/CD Delivery Workflow Diagram", "/images/5-Workshop/5.1-Prepare-Environment/5.1.5-devsecops-workflow/workflow.png")
        ],
        weight=5
    )"""
    # Note: replace only the first occurrence (which is in 5.1.5)
    if old_5_1_5 in content:
        content = content.replace(old_5_1_5, new_5_1_5, 1)

    # 4. Update 5.2.1
    old_5_2_1 = """        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )

    # 5.2.2"""
    new_5_2_1 = """        images_vi=[
            ("Amazon S3 Console - Danh sách các S3 Bucket phục vụ Terraform State và Pipeline Artifacts", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.1-s3-state-bucket/t%E1%BA%A1o%20bucket.png")
        ],
        images_en=[
            ("Amazon S3 Console - S3 Buckets created for Terraform State and Pipeline Artifacts", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.1-s3-state-bucket/t%E1%BA%A1o%20bucket.png")
        ],
        weight=1
    )

    # 5.2.2"""
    if old_5_2_1 in content:
        content = content.replace(old_5_2_1, new_5_2_1, 1)

    # 5. Update 5.2.2
    old_5_2_2 = """        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )

    # 5.2.3"""
    new_5_2_2 = """        images_vi=[
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

    # 5.2.3"""
    if old_5_2_2 in content:
        content = content.replace(old_5_2_2, new_5_2_2, 1)

    # 6. Update 5.2.5
    old_5_2_5 = """        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    write_parent(
        p,
        "5.2","""
    new_5_2_5 = """        images_vi=[
            ("AWS CloudShell - Thực thi terraform apply và kiểm tra output terraform_state_bucket", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.5-verify-terraform-state/verify%20kh%E1%BB%9Fi%20t%E1%BA%A1o%20s3%20b%E1%BA%B1ng%20cloudshell.png")
        ],
        images_en=[
            ("AWS CloudShell - Execute terraform apply and verify terraform_state_bucket output", "/images/5-Workshop/5.2-Terraform-Backend-State/5.2.5-verify-terraform-state/verify%20kh%E1%BB%9Fi%20t%E1%BA%A1o%20s3%20b%E1%BA%B1ng%20cloudshell.png")
        ],
        weight=5
    )

    write_parent(
        p,
        "5.2","""
    if old_5_2_5 in content:
        content = content.replace(old_5_2_5, new_5_2_5, 1)

    # 7. Update 5.3.1 to 5.3.5
    old_5_3_1 = """    # 5.3.1
    write_section(
        p / "5.3.1-create-codepipeline-role",
        "5.3.1",
        "Tạo CodePipelineRole",
        "Create CodePipelineRole",
        "`platform/iam.tf`, `iam-policy/codepipeline-policy.json.tftpl`",
        \"\"\"Role cho AWS CodePipeline, trust principal `codepipeline.amazonaws.com` và được gắn policy thao tác artifact bucket, CodeConnections, CodeBuild và SNS approval notification.\"\"\",
        \"\"\"Execution role for AWS CodePipeline, trusting principal `codepipeline.amazonaws.com` and granted policies for artifact bucket operations, CodeConnections, CodeBuild start/get builds, and SNS approval notifications.\"\"\",
        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )"""
    new_5_3_1 = """    # 5.3.1
    write_section(
        p / "5.3.1-create-codepipeline-role",
        "5.3.1",
        "Tạo CodePipelineRole",
        "Create CodePipelineRole",
        "`platform/iam.tf`, `iam-policy/codepipeline-policy.json.tftpl`",
        \"\"\"Role cho AWS CodePipeline, trust principal `codepipeline.amazonaws.com` và được gắn policy thao tác artifact bucket, CodeConnections, CodeBuild và SNS approval notification.

```hcl
resource "aws_iam_role" "codepipeline" {
  name               = "${local.name}-CodePipelineRole"
  assume_role_policy = data.aws_iam_policy_document.codepipeline_assume.json
}
```\"\"\",
        \"\"\"Execution role for AWS CodePipeline, trusting principal `codepipeline.amazonaws.com` and granted policies for artifact bucket operations, CodeConnections, CodeBuild start/get builds, and SNS approval notifications.

```hcl
resource "aws_iam_role" "codepipeline" {
  name               = "${local.name}-CodePipelineRole"
  assume_role_policy = data.aws_iam_policy_document.codepipeline_assume.json
}
```\"\"\",
        images_vi=[
            ("AWS IAM Console - Cấu hình CodePipelineRole và trust relationship", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.1-codepipeline-role.png")
        ],
        images_en=[
            ("AWS IAM Console - CodePipelineRole configuration and trust relationships", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.1-codepipeline-role.png")
        ],
        weight=1
    )"""
    if old_5_3_1 in content:
        content = content.replace(old_5_3_1, new_5_3_1, 1)

    old_5_3_2 = """    # 5.3.2
    write_section(
        p / "5.3.2-create-scanbuild-role",
        "5.3.2",
        "Tạo ScanBuildRole",
        "Create ScanBuildRole",
        "`platform/iam.tf`, `iam-policy/scan-build-policy.json.tftpl`",
        \"\"\"Role cho CodeBuild validate/security. Policy chỉ cho phép ghi CloudWatch Logs, đọc pipeline artifact và đọc đúng SSM parameter demo.\"\"\",
        \"\"\"Role for CodeBuild validate/security tasks. Policy permits only writing CloudWatch logs, reading pipeline artifacts, and reading the single designated demo SSM parameter.\"\"\",
        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )"""
    new_5_3_2 = """    # 5.3.2
    write_section(
        p / "5.3.2-create-scanbuild-role",
        "5.3.2",
        "Tạo ScanBuildRole",
        "Create ScanBuildRole",
        "`platform/iam.tf`, `iam-policy/scan-build-policy.json.tftpl`",
        \"\"\"Role cho CodeBuild validate/security. Policy chỉ cho phép ghi CloudWatch Logs, đọc pipeline artifact và đọc đúng SSM parameter demo.

```hcl
resource "aws_iam_role" "scan_build" {
  name               = "${local.name}-ScanBuildRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```\"\"\",
        \"\"\"Role for CodeBuild validate/security tasks. Policy permits only writing CloudWatch logs, reading pipeline artifacts, and reading the single designated demo SSM parameter.

```hcl
resource "aws_iam_role" "scan_build" {
  name               = "${local.name}-ScanBuildRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```\"\"\",
        images_vi=[
            ("AWS IAM Console - Cấu hình ScanBuildRole và policy quyền đọc hạn chế", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.2-scan-build-role.png")
        ],
        images_en=[
            ("AWS IAM Console - ScanBuildRole configuration and restricted read policy", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.2-scan-build-role.png")
        ],
        weight=2
    )"""
    if old_5_3_2 in content:
        content = content.replace(old_5_3_2, new_5_3_2, 1)

    old_5_3_3 = """    # 5.3.3
    write_section(
        p / "5.3.3-create-terraform-plan-role",
        "5.3.3",
        "Tạo TerraformPlanRole",
        "Create TerraformPlanRole",
        "`platform/iam.tf`, `iam-policy/terraform-plan-policy.json.tftpl`",
        \"\"\"Role cho Terraform Plan. Ngoài log/artifact/state, role có `ec2:Describe*` và `iam:GetInstanceProfile` để đọc hiện trạng hạ tầng/instance profile khi lập plan; role này không có quyền mutate workload.\"\"\",
        \"\"\"Role for Terraform Plan. Beyond log/artifact/state access, the role holds `ec2:Describe*` and `iam:GetInstanceProfile` to inspect live infrastructure and instance profiles during planning; it holds no permission to mutate workloads.\"\"\",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )"""
    new_5_3_3 = """    # 5.3.3
    write_section(
        p / "5.3.3-create-terraform-plan-role",
        "5.3.3",
        "Tạo TerraformPlanRole",
        "Create TerraformPlanRole",
        "`platform/iam.tf`, `iam-policy/terraform-plan-policy.json.tftpl`",
        \"\"\"Role cho Terraform Plan. Ngoài log/artifact/state, role có `ec2:Describe*` và `iam:GetInstanceProfile` để đọc hiện trạng hạ tầng/instance profile khi lập plan; role này không có quyền mutate workload.

```hcl
resource "aws_iam_role" "terraform_plan" {
  name               = "${local.name}-TerraformPlanRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```\"\"\",
        \"\"\"Role for Terraform Plan. Beyond log/artifact/state access, the role holds `ec2:Describe*` and `iam:GetInstanceProfile` to inspect live infrastructure and instance profiles during planning; it holds no permission to mutate workloads.

```hcl
resource "aws_iam_role" "terraform_plan" {
  name               = "${local.name}-TerraformPlanRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```\"\"\",
        images_vi=[
            ("AWS IAM Console - Cấu hình TerraformPlanRole quyền đọc chỉ hạn chế EC2 Describe*", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.3-terraform-plan-role.png")
        ],
        images_en=[
            ("AWS IAM Console - TerraformPlanRole read-only policy for EC2 Describe*", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.3-terraform-plan-role.png")
        ],
        weight=3
    )"""
    if old_5_3_3 in content:
        content = content.replace(old_5_3_3, new_5_3_3, 1)

    old_5_3_4 = """    # 5.3.4
    write_section(
        p / "5.3.4-create-terraform-deploy-role",
        "5.3.4",
        "Tạo TerraformDeployRole",
        "Create TerraformDeployRole",
        "`platform/iam.tf`, `iam-policy/terraform-deploy-policy.json.tftpl`",
        \"\"\"Role cho Terraform Apply. Policy cho phép các API EC2/VPC cần thiết để tạo/xóa tài nguyên Workshop, `ec2:MonitorInstances`/`UnmonitorInstances` cho detailed monitoring, `iam:GetInstanceProfile` và `iam:PassRole` được scope tới `EC2DemoRole`, cùng quyền state/artifact cần thiết.\"\"\",
        \"\"\"Role for Terraform Apply. Policy authorizes required EC2/VPC APIs for provisioning/teardown, `ec2:MonitorInstances`/`UnmonitorInstances` for detailed monitoring, `iam:GetInstanceProfile` and scoped `iam:PassRole` to `EC2DemoRole`, alongside necessary remote state and artifact access.\"\"\",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )"""
    new_5_3_4 = """    # 5.3.4
    write_section(
        p / "5.3.4-create-terraform-deploy-role",
        "5.3.4",
        "Tạo TerraformDeployRole",
        "Create TerraformDeployRole",
        "`platform/iam.tf`, `iam-policy/terraform-deploy-policy.json.tftpl`",
        \"\"\"Role cho Terraform Apply. Policy cho phép các API EC2/VPC cần thiết để tạo/xóa tài nguyên Workshop, `ec2:MonitorInstances`/`UnmonitorInstances` cho detailed monitoring, `iam:GetInstanceProfile` và `iam:PassRole` được scope tới `EC2DemoRole`, cùng quyền state/artifact cần thiết.

```hcl
resource "aws_iam_role" "terraform_deploy" {
  name               = "${local.name}-TerraformDeployRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```\"\"\",
        \"\"\"Role for Terraform Apply. Policy authorizes required EC2/VPC APIs for provisioning/teardown, `ec2:MonitorInstances`/`UnmonitorInstances` for detailed monitoring, `iam:GetInstanceProfile` and scoped `iam:PassRole` to `EC2DemoRole`, alongside necessary remote state and artifact access.

```hcl
resource "aws_iam_role" "terraform_deploy" {
  name               = "${local.name}-TerraformDeployRole"
  assume_role_policy = data.aws_iam_policy_document.codebuild_assume.json
}
```\"\"\",
        images_vi=[
            ("AWS IAM Console - Cấu hình TerraformDeployRole giới hạn quyền deploy EC2/VPC", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.4-terraform-deploy-role.png")
        ],
        images_en=[
            ("AWS IAM Console - TerraformDeployRole scoped deployment policies for EC2/VPC", "/images/5-Workshop/5.3-IAM-Secrets/5.3.1-pipeline-iam-roles/5.3.4-terraform-deploy-role.png")
        ],
        weight=4
    )"""
    if old_5_3_4 in content:
        content = content.replace(old_5_3_4, new_5_3_4, 1)

    old_5_3_5 = """    # 5.3.5
    write_section(
        p / "5.3.5-configure-ssm-parameter-store",
        "5.3.5",
        "Cấu hình AWS Systems Manager Parameter Store",
        "Configure AWS Systems Manager Parameter Store",
        "`platform/secrets_notifications.tf`, `platform/locals.tf`",
        \"\"\"Platform tạo một random token và lưu tại SSM Parameter Store với type `SecureString`. Path được tạo theo mẫu `/<project>/<environment>/demo_token`.

### SSM SecureString

```hcl
resource "aws_ssm_parameter" "demo_token" {
  name        = local.demo_token_path
  description = "Demo SecureString consumed by CodeBuild without printing the value."
  type        = "SecureString"
  value       = random_password.demo_token.result
  overwrite   = true
}
```\"\"\",
        \"\"\"The platform generates a random token stored in SSM Parameter Store as type `SecureString`. The path follows the pattern `/<project>/<environment>/demo_token`.

### SSM SecureString Declaration

```hcl
resource "aws_ssm_parameter" "demo_token" {
  name        = local.demo_token_path
  description = "Demo SecureString consumed by CodeBuild without printing the value."
  type        = "SecureString"
  value       = random_password.demo_token.result
  overwrite   = true
}
```\"\"\",
        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )"""
    new_5_3_5 = """    # 5.3.5
    write_section(
        p / "5.3.5-configure-ssm-parameter-store",
        "5.3.5",
        "Cấu hình AWS Systems Manager Parameter Store",
        "Configure AWS Systems Manager Parameter Store",
        "`platform/secrets_notifications.tf`, `platform/locals.tf`",
        \"\"\"Platform tạo một random token và lưu tại SSM Parameter Store với type `SecureString`. Path được tạo theo mẫu `/<project>/<environment>/demo_token`.

### SSM SecureString

```hcl
resource "aws_ssm_parameter" "demo_token" {
  name        = local.demo_token_path
  description = "Demo SecureString consumed by CodeBuild without printing the value."
  type        = "SecureString"
  value       = random_password.demo_token.result
  overwrite   = true
}
```\"\"\",
        \"\"\"The platform generates a random token stored in SSM Parameter Store as type `SecureString`. The path follows the pattern `/<project>/<environment>/demo_token`.

### SSM SecureString Declaration

```hcl
resource "aws_ssm_parameter" "demo_token" {
  name        = local.demo_token_path
  description = "Demo SecureString consumed by CodeBuild without printing the value."
  type        = "SecureString"
  value       = random_password.demo_token.result
  overwrite   = true
}
```\"\"\",
        images_vi=[
            ("AWS Systems Manager Parameter Store - Quản lý Secret SecureString", "/images/5-Workshop/5.3-IAM-Secrets/5.3.2-ssm-parameter-store/check%20SSM.png")
        ],
        images_en=[
            ("AWS Systems Manager Parameter Store - SecureString Secret Management", "/images/5-Workshop/5.3-IAM-Secrets/5.3.2-ssm-parameter-store/check%20SSM.png")
        ],
        weight=5
    )"""
    if old_5_3_5 in content:
        content = content.replace(old_5_3_5, new_5_3_5, 1)

    # 8. Update 5.4 sub_list to match directory names with user static images
    old_5_4_sublist = """    sub_list = [
        {"num": "5.4.1", "dir": "5.4.1-prepare-repo-branch", "title_vi": "Chuẩn bị Repository và Branch", "title_en": "Prepare Repository and Branch", "summary_vi": "Cấu hình biến GitHub owner, repo và branch main cho pipeline", "summary_en": "Configure GitHub owner, repo name, and main branch for CodePipeline"},
        {"num": "5.4.2", "dir": "5.4.2-create-aws-codeconnections", "title_vi": "Tạo AWS CodeConnections", "title_en": "Create AWS CodeConnections", "summary_vi": "Khởi tạo resource aws_codeconnections_connection ở trạng thái PENDING", "summary_en": "Provision aws_codeconnections_connection resource initially in PENDING status"},
        {"num": "5.4.3", "dir": "5.4.3-connect-github-repo", "title_vi": "Kết nối GitHub Repository", "title_en": "Connect GitHub Repository", "summary_vi": "Thao tác trên AWS Console xác thực GitHub App chuyển sang AVAILABLE", "summary_en": "Authorize GitHub App via AWS Console transitioning connection to AVAILABLE"},
        {"num": "5.4.4", "dir": "5.4.4-create-s3-artifact-bucket", "title_vi": "Tạo Amazon S3 Pipeline Artifact Bucket", "title_en": "Create Amazon S3 Pipeline Artifact Bucket", "summary_vi": "Tạo bucket lưu trữ artifact trung gian với lifecycle 30 ngày", "summary_en": "Create pipeline artifact bucket with 30-day lifecycle expiration"},
        {"num": "5.4.5", "dir": "5.4.5-init-aws-codepipeline", "title_vi": "Khởi tạo AWS CodePipeline", "title_en": "Initialize AWS CodePipeline", "summary_vi": "Định nghĩa pipeline V1 chế độ SUPERSEDED liên kết toàn diện 7 stage", "summary_en": "Declare V1 SUPERSEDED pipeline orchestrating 7 sequential delivery stages"},
        {"num": "5.4.6", "dir": "5.4.6-verify-source-trigger", "title_vi": "Kiểm tra Source Trigger", "title_en": "Verify Source Trigger", "summary_vi": "Commit push mã nguồn và xác minh CodePipeline tự động kích hoạt", "summary_en": "Push commit to main branch and verify automated webhook execution"},
    ]"""
    new_5_4_sublist = """    sub_list = [
        {"num": "5.4.1", "dir": "5.4.1-prepare-repo-branch", "title_vi": "Chuẩn bị Repository và Branch", "title_en": "Prepare Repository and Branch", "summary_vi": "Cấu hình biến GitHub owner, repo và branch main cho pipeline", "summary_en": "Configure GitHub owner, repo name, and main branch for CodePipeline"},
        {"num": "5.4.2", "dir": "5.4.2-create-codeconnections", "title_vi": "Tạo AWS CodeConnections", "title_en": "Create AWS CodeConnections", "summary_vi": "Khởi tạo resource aws_codeconnections_connection ở trạng thái PENDING", "summary_en": "Provision aws_codeconnections_connection resource initially in PENDING status"},
        {"num": "5.4.3", "dir": "5.4.3-connect-github-repo", "title_vi": "Kết nối GitHub Repository", "title_en": "Connect GitHub Repository", "summary_vi": "Thao tác trên AWS Console xác thực GitHub App chuyển sang AVAILABLE", "summary_en": "Authorize GitHub App via AWS Console transitioning connection to AVAILABLE"},
        {"num": "5.4.4", "dir": "5.4.4-s3-artifact-bucket", "title_vi": "Tạo Amazon S3 Pipeline Artifact Bucket", "title_en": "Create Amazon S3 Pipeline Artifact Bucket", "summary_vi": "Tạo bucket lưu trữ artifact trung gian với lifecycle 30 ngày", "summary_en": "Create pipeline artifact bucket with 30-day lifecycle expiration"},
        {"num": "5.4.5", "dir": "5.4.5-create-codepipeline", "title_vi": "Khởi tạo AWS CodePipeline", "title_en": "Initialize AWS CodePipeline", "summary_vi": "Định nghĩa pipeline V1 chế độ SUPERSEDED liên kết toàn diện 7 stage", "summary_en": "Declare V1 SUPERSEDED pipeline orchestrating 7 sequential delivery stages"},
        {"num": "5.4.6", "dir": "5.4.6-verify-source-trigger", "title_vi": "Kiểm tra Source Trigger", "title_en": "Verify Source Trigger", "summary_vi": "Commit push mã nguồn và xác minh CodePipeline tự động kích hoạt", "summary_en": "Push commit to main branch and verify automated webhook execution"},
    ]"""
    if old_5_4_sublist in content:
        content = content.replace(old_5_4_sublist, new_5_4_sublist, 1)

    # 9. Update 5.4.1
    old_5_4_1 = """    # 5.4.1
    write_section(
        p / "5.4.1-prepare-repo-branch",
        "5.4.1",
        "Chuẩn bị Repository và Branch",
        "Prepare Repository and Branch",
        "`platform/variables.tf`, `platform/locals.tf`",
        \"\"\"GitHub owner, repository và branch được truyền qua biến Terraform. `local.repo_full_name` ghép owner/repo để cấp cho Source action. Branch mặc định là `main`.\"\"\",
        \"\"\"GitHub owner, repository, and branch are passed via Terraform variables. `local.repo_full_name` concatenates owner/repo for the Source action. Branch defaults to `main`.\"\"\",
        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )"""
    new_5_4_1 = """    # 5.4.1
    write_section(
        p / "5.4.1-prepare-repo-branch",
        "5.4.1",
        "Chuẩn bị Repository và Branch",
        "Prepare Repository and Branch",
        "`platform/variables.tf`, `platform/locals.tf`",
        \"\"\"GitHub owner, repository và branch được truyền qua biến Terraform. `local.repo_full_name` ghép owner/repo để cấp cho Source action. Branch mặc định là `main`.\"\"\",
        \"\"\"GitHub owner, repository, and branch are passed via Terraform variables. `local.repo_full_name` concatenates owner/repo for the Source action. Branch defaults to `main`.\"\"\",
        images_vi=[
            ("Cấu hình file terraform.tfvars với repo GitHub và branch main", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.1-prepare-repo-branch/chuan%20bi%20repo%20v%C3%A0%20branch.png")
        ],
        images_en=[
            ("Configure terraform.tfvars with GitHub repository and main branch parameters", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.1-prepare-repo-branch/chuan%20bi%20repo%20v%C3%A0%20branch.png")
        ],
        weight=1
    )"""
    if old_5_4_1 in content:
        content = content.replace(old_5_4_1, new_5_4_1, 1)

    # 10. Update 5.4.2
    old_5_4_2 = """    # 5.4.2
    write_section(
        p / "5.4.2-create-aws-codeconnections","""
    new_5_4_2 = """    # 5.4.2
    write_section(
        p / "5.4.2-create-codeconnections","""
    if old_5_4_2 in content:
        content = content.replace(old_5_4_2, new_5_4_2, 1)

    old_5_4_2_end = """        weight=2
    )

    # 5.4.3"""
    new_5_4_2_end = """        images_vi=[
            ("AWS CodeConnections - Kết nối GitHub ở trạng thái PENDING sau khi apply Terraform", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.2-create-codeconnections/github%20pending.png")
        ],
        images_en=[
            ("AWS CodeConnections - GitHub connection in PENDING status following Terraform apply", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.2-create-codeconnections/github%20pending.png")
        ],
        weight=2
    )

    # 5.4.3"""
    # Replace only in 5.4.2 context
    if "p / \"5.4.2-create-codeconnections\"" in content:
        # Find where 5.4.2 ends
        idx = content.find("p / \"5.4.2-create-codeconnections\"")
        end_idx = content.find(old_5_4_2_end, idx)
        if end_idx != -1:
            content = content[:end_idx] + new_5_4_2_end + content[end_idx + len(old_5_4_2_end):]

    # 11. Update 5.4.3 (User specifically asked for 5.4.3!)
    old_5_4_3 = """    # 5.4.3
    write_section(
        p / "5.4.3-connect-github-repo",
        "5.4.3",
        "Kết nối GitHub Repository",
        "Connect GitHub Repository",
        "AWS Management Console",
        \"\"\"Trong AWS Console, mở **Developer Tools > Connections**, chọn connection do Terraform tạo, thực hiện **Update pending connection** và authorize repository. Khi hoàn tất, status cần chuyển thành **AVAILABLE**.

---

> **[📝 Ảnh chụp đề xuất]**  
> AWS CodeConnections hiển thị connection GitHub với trạng thái AVAILABLE.
\"\"\",
        \"\"\"In the AWS Console, navigate to **Developer Tools > Connections**, select the connection created by Terraform, click **Update pending connection**, and authorize the GitHub App and repository access. Once authorized, the status updates to **AVAILABLE**.

---

> **[📝 Recommended Screenshot]**  
> AWS CodeConnections console displaying the GitHub connection in AVAILABLE status.
\"\"\",
        screenshot_vi=None,  # Included in text directly to avoid extra duplicate box
        screenshot_en=None,
        weight=3
    )"""
    new_5_4_3 = """    # 5.4.3
    write_section(
        p / "5.4.3-connect-github-repo",
        "5.4.3",
        "Kết nối GitHub Repository",
        "Connect GitHub Repository",
        "AWS Management Console",
        \"\"\"Trong AWS Console, mở **Developer Tools > Connections**, chọn connection do Terraform tạo, thực hiện **Update pending connection** và authorize repository. Khi hoàn tất, status cần chuyển thành **AVAILABLE**.\"\"\",
        \"\"\"In the AWS Console, navigate to **Developer Tools > Connections**, select the connection created by Terraform, click **Update pending connection**, and authorize the GitHub App and repository access. Once authorized, the status updates to **AVAILABLE**.\"\"\",
        images_vi=[
            ("AWS CodeConnections - Hoàn tất kết nối GitHub repository chuyển sang trạng thái AVAILABLE", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.3-connect-github-repo/connect%20git%20hub%20repo.png")
        ],
        images_en=[
            ("AWS CodeConnections - Complete GitHub repository handshake showing AVAILABLE status", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.3-connect-github-repo/connect%20git%20hub%20repo.png")
        ],
        weight=3
    )"""
    if old_5_4_3 in content:
        content = content.replace(old_5_4_3, new_5_4_3, 1)

    # 12. Update 5.4.4
    old_5_4_4 = """    # 5.4.4
    write_section(
        p / "5.4.4-create-s3-artifact-bucket",
        "5.4.4",
        "Tạo Amazon S3 Pipeline Artifact Bucket",
        "Create Amazon S3 Pipeline Artifact Bucket",
        "`bootstrap/main.tf`, `bootstrap/outputs.tf`",
        \"\"\"Artifact bucket được tạo ngay trong bootstrap, tách biệt với Terraform State. Bucket bật Versioning, SSE-S3, Block Public Access, BucketOwnerEnforced và lifecycle xóa artifact cũ sau 30 ngày; noncurrent version hết hạn sau 7 ngày.\"\"\",
        \"\"\"The artifact bucket is created during bootstrap, fully decoupled from Terraform State. The bucket enforces Versioning, SSE-S3, Block Public Access, BucketOwnerEnforced, and lifecycle rules expiring old artifacts after 30 days (noncurrent versions after 7 days).\"\"\",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )"""
    new_5_4_4 = """    # 5.4.4
    write_section(
        p / "5.4.4-s3-artifact-bucket",
        "5.4.4",
        "Tạo Amazon S3 Pipeline Artifact Bucket",
        "Create Amazon S3 Pipeline Artifact Bucket",
        "`bootstrap/main.tf`, `bootstrap/outputs.tf`",
        \"\"\"Artifact bucket được tạo ngay trong bootstrap, tách biệt với Terraform State. Bucket bật Versioning, SSE-S3, Block Public Access, BucketOwnerEnforced và lifecycle xóa artifact cũ sau 30 ngày; noncurrent version hết hạn sau 7 ngày.

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
```\"\"\",
        \"\"\"The artifact bucket is created during bootstrap, fully decoupled from Terraform State. The bucket enforces Versioning, SSE-S3, Block Public Access, BucketOwnerEnforced, and lifecycle rules expiring old artifacts after 30 days (noncurrent versions after 7 days).

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
```\"\"\",
        images_vi=[
            ("Khai báo tài nguyên S3 Artifact Bucket trong bootstrap/main.tf", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%201.png"),
            ("Khai báo output pipeline_artifact_bucket trong bootstrap/outputs.tf", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%202.png")
        ],
        images_en=[
            ("S3 Artifact Bucket resource configuration in bootstrap/main.tf", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%201.png"),
            ("Export pipeline_artifact_bucket output in bootstrap/outputs.tf", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.4-s3-artifact-bucket/cau%20hinh%20s3%20bucket%20anh%202.png")
        ],
        weight=4
    )"""
    if old_5_4_4 in content:
        content = content.replace(old_5_4_4, new_5_4_4, 1)

    # 13. Update 5.4.5
    old_5_4_5_header = """    # 5.4.5
    write_section(
        p / "5.4.5-init-aws-codepipeline","""
    new_5_4_5_header = """    # 5.4.5
    write_section(
        p / "5.4.5-create-codepipeline","""
    if old_5_4_5_header in content:
        content = content.replace(old_5_4_5_header, new_5_4_5_header, 1)

    old_5_4_5_end = """        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    # 5.4.6"""
    new_5_4_5_end = """        images_vi=[
            ("AWS CodePipeline Console - Giao diện trực quan chuỗi CI/CD 7 giai đoạn hoạt động thành công", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.5-create-codepipeline/%E1%BA%A2nh%20ch%E1%BB%A5p%20m%C3%A0n%20h%C3%ACnh%202026-09-16%20024115.png")
        ],
        images_en=[
            ("AWS CodePipeline Console - End-to-end 7-stage CI/CD pipeline execution overview", "/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.5-create-codepipeline/%E1%BA%A2nh%20ch%E1%BB%A5p%20m%C3%A0n%20h%C3%ACnh%202026-09-16%20024115.png")
        ],
        weight=5
    )

    # 5.4.6"""
    if "p / \"5.4.5-create-codepipeline\"" in content:
        idx = content.find("p / \"5.4.5-create-codepipeline\"")
        end_idx = content.find(old_5_4_5_end, idx)
        if end_idx != -1:
            content = content[:end_idx] + new_5_4_5_end + content[end_idx + len(old_5_4_5_end):]

    path.write_text(content, encoding="utf-8")
    print("Patched gen_module_5_1_to_5_4.py successfully!")

def patch_5_5_to_5_8():
    path = BASE_DIR / "scripts" / "gen_module_5_5_to_5_8.py"
    content = path.read_text(encoding="utf-8")

    # Update 5.5.1
    old_5_5_1 = """    # 5.5.1
    write_section(
        p / "5.5.1-codebuild-validate-test",
        "5.5.1",
        "Tạo AWS CodeBuild cho Validate & Test",
        "Create AWS CodeBuild for Validate & Test",
        "`platform/codebuild.tf`, `cicd/buildspec-validate-security.yml`",
        \"\"\"Project `validate-security` dùng CodeBuild standard:7.0, compute `BUILD_GENERAL1_SMALL`, source/artifact từ CodePipeline và role `ScanBuildRole`. Cùng một CodeBuild project được tái sử dụng cho hai stage thông qua biến `RUN_MODE`.\"\"\",
        \"\"\"Project `validate-security` uses CodeBuild standard:7.0, compute size `BUILD_GENERAL1_SMALL`, source/artifacts from CodePipeline, and role `ScanBuildRole`. The same CodeBuild project is reused across both stages via the `RUN_MODE` variable.\"\"\",
        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )"""
    new_5_5_1 = """    # 5.5.1
    write_section(
        p / "5.5.1-codebuild-validate-test",
        "5.5.1",
        "Tạo AWS CodeBuild cho Validate & Test",
        "Create AWS CodeBuild for Validate & Test",
        "`platform/codebuild.tf`, `cicd/buildspec-validate-security.yml`",
        \"\"\"Project `validate-security` dùng CodeBuild standard:7.0, compute `BUILD_GENERAL1_SMALL`, source/artifact từ CodePipeline và role `ScanBuildRole`. Cùng một CodeBuild project được tái sử dụng cho hai stage thông qua biến `RUN_MODE`.\"\"\",
        \"\"\"Project `validate-security` uses CodeBuild standard:7.0, compute size `BUILD_GENERAL1_SMALL`, source/artifacts from CodePipeline, and role `ScanBuildRole`. The same CodeBuild project is reused across both stages via the `RUN_MODE` variable.\"\"\",
        images_vi=[
            ("AWS CodeBuild Console - Danh sách các CodeBuild Projects phục vụ Validate và Security Gates", "/images/5-Workshop/5.5-Validate-Security-Gates/image.png")
        ],
        images_en=[
            ("AWS CodeBuild Console - CodeBuild Projects list supporting Validate and Security Gates", "/images/5-Workshop/5.5-Validate-Security-Gates/image.png")
        ],
        weight=1
    )"""
    if old_5_5_1 in content:
        content = content.replace(old_5_5_1, new_5_5_1, 1)

    path.write_text(content, encoding="utf-8")
    print("Patched gen_module_5_5_to_5_8.py successfully!")

if __name__ == "__main__":
    patch_5_1_to_5_4()
    patch_5_5_to_5_8()
