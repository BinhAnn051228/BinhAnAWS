import os
from pathlib import Path
from generator_common import BASE_DIR, write_section, write_parent

def build_5_5():
    p = BASE_DIR / "5.5-Validate-Security-Gates"
    sub_list = [
        {"num": "5.5.1", "dir": "5.5.1-codebuild-validate-test", "title_vi": "Tạo AWS CodeBuild cho Validate & Test", "title_en": "Create AWS CodeBuild for Validate & Test", "summary_vi": "Khởi tạo CodeBuild validate-security dùng chung qua biến RUN_MODE", "summary_en": "Provision reusable CodeBuild validate-security project driven by RUN_MODE"},
        {"num": "5.5.2", "dir": "5.5.2-terraform-format-validate", "title_vi": "Kiểm tra Terraform Format và Validate", "title_en": "Verify Terraform Format and Validate", "summary_vi": "Kiểm tra cú pháp HCL, biên dịch Python và unit test Pytest", "summary_en": "Lint HCL syntax, verify Python compilation, and execute Pytest suite"},
        {"num": "5.5.3", "dir": "5.5.3-gitleaks-secret-scan", "title_vi": "Tích hợp Gitleaks Secret Scanning", "title_en": "Integrate Gitleaks Secret Scanning", "summary_vi": "Quét phát hiện rò rỉ secret, khóa API và credential trong mã nguồn", "summary_en": "Detect leaked API keys and hardcoded credentials via Gitleaks"},
        {"num": "5.5.4", "dir": "5.5.4-bandit-sast", "title_vi": "Tích hợp Bandit SAST", "title_en": "Integrate Bandit SAST", "summary_vi": "Phân tích tĩnh mã nguồn Python phát hiện lỗ hổng mức độ cao", "summary_en": "Perform Python Static Application Security Testing with Bandit"},
        {"num": "5.5.5", "dir": "5.5.5-trivy-sca-cve", "title_vi": "Tích hợp Trivy SCA/CVE Scanning", "title_en": "Integrate Trivy SCA/CVE Scanning", "summary_vi": "Quét dependency CVEs mức HIGH/CRITICAL trong thư viện bên thứ ba", "summary_en": "Scan third-party Python dependencies for HIGH/CRITICAL CVEs via Trivy"},
        {"num": "5.5.6", "dir": "5.5.6-checkov-iac-scan", "title_vi": "Tích hợp Checkov IaC Scanning", "title_en": "Integrate Checkov IaC Scanning", "summary_vi": "Quét vi phạm bảo mật và sai cấu hình hạ tầng Terraform", "summary_en": "Scan Terraform IaC templates for security misconfigurations via Checkov"},
        {"num": "5.5.7", "dir": "5.5.7-configure-security-gate", "title_vi": "Cấu hình Security Gate", "title_en": "Configure Security Gate", "summary_vi": "Thiết lập cổng chặn an toàn tuyệt đối trước khi sang bước Terraform Plan", "summary_en": "Enforce strict security gate blocking progression upon any scanner non-zero exit"},
    ]

    # 5.5.1
    write_section(
        p / "5.5.1-codebuild-validate-test",
        "5.5.1",
        "Tạo AWS CodeBuild cho Validate & Test",
        "Create AWS CodeBuild for Validate & Test",
        "`platform/codebuild.tf`, `cicd/buildspec-validate-security.yml`",
        """Project `validate-security` dùng CodeBuild standard:7.0, compute `BUILD_GENERAL1_SMALL`, source/artifact từ CodePipeline và role `ScanBuildRole`. Cùng một CodeBuild project được tái sử dụng cho hai stage thông qua biến `RUN_MODE`.""",
        """Project `validate-security` uses CodeBuild standard:7.0, compute size `BUILD_GENERAL1_SMALL`, source/artifacts from CodePipeline, and role `ScanBuildRole`. The same CodeBuild project is reused across both stages via the `RUN_MODE` variable.""",
        images_vi=[
            ("AWS CodeBuild Console - Danh sách các CodeBuild Projects phục vụ Validate và Security Gates", "/images/5-Workshop/5.5-Validate-Security-Gates/image.png")
        ],
        images_en=[
            ("AWS CodeBuild Console - CodeBuild Projects list supporting Validate and Security Gates", "/images/5-Workshop/5.5-Validate-Security-Gates/image.png")
        ],
        weight=1
    )

    # 5.5.2
    write_section(
        p / "5.5.2-terraform-format-validate",
        "5.5.2",
        "Kiểm tra Terraform Format và Validate",
        "Verify Terraform Format and Validate",
        "`cicd/buildspec-validate-security.yml`, `app/tests/test_app.py`",
        """```bash
RUN_MODE=validate
terraform fmt -check -recursive bootstrap platform workload
terraform -chdir="${WORKLOAD_DIR}" init -backend=false -input=false
terraform -chdir="${WORKLOAD_DIR}" validate
python -m compileall -q app
pytest -q app/tests
```

Stage `ValidateTest` chỉ đi tiếp khi Terraform format/validate, Python compile và Pytest đều thành công.

### Chạy ValidateTest trước khi push

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
> Nếu pytest báo module `app.app` không có `test_client`, file `app/tests/test_app.py` phải import Flask instance bằng: `from app.app import app`.""",
        """```bash
RUN_MODE=validate
terraform fmt -check -recursive bootstrap platform workload
terraform -chdir="${WORKLOAD_DIR}" init -backend=false -input=false
terraform -chdir="${WORKLOAD_DIR}" validate
python -m compileall -q app
pytest -q app/tests
```

The `ValidateTest` stage proceeds only when Terraform format/validate, Python compilation, and Pytest all succeed.

### Run ValidateTest Locally Before Push

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
> If pytest reports module `app.app` has no `test_client`, file `app/tests/test_app.py` must import the Flask instance using: `from app.app import app`.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )

    # 5.5.3
    write_section(
        p / "5.5.3-gitleaks-secret-scan",
        "5.5.3",
        "Tích hợp Gitleaks Secret Scanning",
        "Integrate Gitleaks Secret Scanning",
        "`cicd/buildspec-validate-security.yml`, `.gitleaks.toml`",
        """```bash
gitleaks dir . --config .gitleaks.toml --redact --no-banner
```

Gitleaks quét repository ở chế độ directory và redact kết quả để tránh hiển thị secret trong log. Fixture demo trong `demo/fixtures` được allowlist để baseline repository không bị fail; khi copy fixture sang `app/`, scan sẽ bắt lỗi.""",
        """```bash
gitleaks dir . --config .gitleaks.toml --redact --no-banner
```

Gitleaks scans the repository in directory mode and redacts output to avoid printing secrets in build logs. Demo fixtures in `demo/fixtures` are allowlisted so the baseline repository does not fail; copying fixtures into `app/` triggers detection.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )

    # 5.5.4
    write_section(
        p / "5.5.4-bandit-sast",
        "5.5.4",
        "Tích hợp Bandit SAST",
        "Integrate Bandit SAST",
        "`cicd/buildspec-validate-security.yml`",
        """```bash
bandit -r app -lll -iii
```

Bandit quét source Python trong thư mục `app`. Tham số hiện tại tập trung vào issue severity/confidence cao theo cấu hình của command.""",
        """```bash
bandit -r app -lll -iii
```

Bandit scans Python source code in the `app` folder. Parameters focus strictly on high severity and high confidence issues.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )

    # 5.5.5
    write_section(
        p / "5.5.5-trivy-sca-cve",
        "5.5.5",
        "Tích hợp Trivy SCA/CVE Scanning",
        "Integrate Trivy SCA/CVE Scanning",
        "`cicd/buildspec-validate-security.yml`, `demo/fixtures/requirements-vulnerable.txt`",
        """```bash
trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
```

Trivy quét dependency vulnerability ở mức `HIGH/CRITICAL`. Khi phát hiện vulnerability phù hợp điều kiện, exit code 1 làm SecurityScan thất bại.""",
        """```bash
trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
```

Trivy scans dependency vulnerabilities at `HIGH/CRITICAL` severity levels. Upon detecting qualifying vulnerabilities, exit code 1 causes SecurityScan to fail.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    # 5.5.6
    write_section(
        p / "5.5.6-checkov-iac-scan",
        "5.5.6",
        "Tích hợp Checkov IaC Scanning",
        "Integrate Checkov IaC Scanning",
        "`cicd/buildspec-validate-security.yml`, `workload/main.tf`, `demo/fixtures/public_ssh.tf.example`",
        """```bash
checkov -d "${WORKLOAD_DIR}" --framework terraform --compact
```

Checkov quét Terraform workload. Baseline có các exception PoC được ghi chú trực tiếp trong source cho VPC Flow Logs (`CKV2_AWS_11`), Public Subnet (`CKV_AWS_130`), Public HTTP/80 (`CKV_AWS_260`) và Public IP (`CKV_AWS_88`). Default Security Group bị khóa và EC2 có IAM Instance Profile nên các control tương ứng pass. Public SSH không nằm trong baseline và được dùng làm kịch bản lỗi.

### Chạy SecurityScan thủ công

```bash
cd ~/fcaj-aws-devsecops
gitleaks dir . --config .gitleaks.toml --redact --no-banner
bandit -r app -lll -iii
trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
checkov -d workload --framework terraform --compact
```

> [!TIP]
> Checkov được chạy bằng CLI `checkov`, không dùng `python3 -m checkov`. Baseline hợp lệ có thể có `SKIPPED` cho các exception PoC đã document, nhưng không còn `FAILED` ngoài các tình huống demo có chủ đích.""",
        """```bash
checkov -d "${WORKLOAD_DIR}" --framework terraform --compact
```

Checkov scans the Terraform workload. Baseline PoC exceptions are documented directly in source for VPC Flow Logs (`CKV2_AWS_11`), Public Subnet (`CKV_AWS_130`), Public HTTP/80 (`CKV_AWS_260`), and Public IP (`CKV_AWS_88`). The default security group is locked down and EC2 has an IAM instance profile, passing those controls. Public SSH is excluded from baseline and serves as a failure test case.

### Run SecurityScan Manually

```bash
cd ~/fcaj-aws-devsecops
gitleaks dir . --config .gitleaks.toml --redact --no-banner
bandit -r app -lll -iii
trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
checkov -d workload --framework terraform --compact
```

> [!TIP]
> Execute Checkov using the `checkov` binary directly rather than `python3 -m checkov`. A valid baseline may report `SKIPPED` for documented PoC exceptions, but must contain zero `FAILED` checks outside intentional demo scenarios.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=6
    )

    # 5.5.7
    write_section(
        p / "5.5.7-configure-security-gate",
        "5.5.7",
        "Cấu hình Security Gate",
        "Configure Security Gate",
        "`platform/pipeline.tf`, `cicd/buildspec-validate-security.yml`",
        """Security Gate được hình thành bằng chuỗi CodePipeline: `SecurityScan` phải trả về trạng thái thành công trước khi `TerraformPlan` được bắt đầu. Buildspec dùng `set -euo pipefail`; bất kỳ scanner nào trả non-zero đều làm stage thất bại và dừng luồng trước deployment.""",
        """The Security Gate is enforced through CodePipeline sequence: `SecurityScan` must complete successfully before `TerraformPlan` begins. Buildspecs enforce `set -euo pipefail`; any scanner returning a non-zero exit code halts the pipeline before infrastructure changes occur.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=7
    )

    # Parent 5.5
    write_parent(
        p,
        "5.5",
        "Xây dựng Validate, Test & Shift-Left Security",
        "Validate, Test & Shift-Left Security",
        "Chương này hướng dẫn xây dựng các tầng phòng thủ Shift-Left Security tự động với CodeBuild: linting, unit testing, Gitleaks (Secret), Bandit (SAST), Trivy (SCA) và Checkov (IaC).",
        "This chapter guides through implementing automated Shift-Left security layers in CodeBuild: linting, unit testing, Gitleaks, Bandit, Trivy, and Checkov.",
        sub_list,
        5
    )

def build_5_6():
    p = BASE_DIR / "5.6-Terraform-Plan-Approval"
    sub_list = [
        {"num": "5.6.1", "dir": "5.6.1-codebuild-terraform-plan", "title_vi": "Tạo CodeBuild Project cho Terraform Plan", "title_en": "Create CodeBuild Project for Terraform Plan", "summary_vi": "Cấu hình CodeBuild terraform-plan với quyền hạn chỉ đọc TerraformPlanRole", "summary_en": "Configure terraform-plan CodeBuild project under read-only TerraformPlanRole"},
        {"num": "5.6.2", "dir": "5.6.2-execute-terraform-init", "title_vi": "Thực hiện Terraform Init", "title_en": "Execute Terraform Init", "summary_vi": "Khởi tạo backend workload với S3 native locking use_lockfile=true", "summary_en": "Initialize workload backend with S3 native locking use_lockfile=true"},
        {"num": "5.6.3", "dir": "5.6.3-generate-terraform-plan", "title_vi": "Sinh Terraform Plan", "title_en": "Generate Terraform Plan", "summary_vi": "Tạo file nhị phân tfplan và xuất plan.txt cho reviewer kiểm tra", "summary_en": "Generate binary tfplan and readable plan.txt for human review"},
        {"num": "5.6.4", "dir": "5.6.4-store-tfplan-artifact", "title_vi": "Lưu tfplan làm Artifact", "title_en": "Store tfplan as Artifact", "summary_vi": "Đóng gói tfplan và lockfile thành PlanOutput artifact bất biến", "summary_en": "Package tfplan and lockfile into immutable PlanOutput pipeline artifact"},
        {"num": "5.6.5", "dir": "5.6.5-create-manual-approval-stage", "title_vi": "Tạo Manual Approval Stage", "title_en": "Create Manual Approval Stage", "summary_vi": "Khai báo stage ManualApproval tích hợp SNS notification", "summary_en": "Declare ManualApproval stage integrated with SNS topic notifications"},
        {"num": "5.6.6", "dir": "5.6.6-review-approve-infrastructure", "title_vi": "Review và phê duyệt thay đổi hạ tầng", "title_en": "Review and Approve Infrastructure Changes", "summary_vi": "Đọc plan.txt và ra quyết định Approve hoặc Reject trên console", "summary_en": "Review plan.txt and execute Approve or Reject in CodePipeline console"},
    ]

    # 5.6.1
    write_section(
        p / "5.6.1-codebuild-terraform-plan",
        "5.6.1",
        "Tạo CodeBuild Project cho Terraform Plan",
        "Create CodeBuild Project for Terraform Plan",
        "`platform/codebuild.tf`, `cicd/buildspec-plan.yml`",
        """Project Terraform Plan dùng `TerraformPlanRole`, source/artifact từ CodePipeline, backend S3 của workload và các `TF_VAR` cần thiết để sinh cùng một cấu hình mà Apply sẽ sử dụng.

### Kiểm tra runtime variable của Terraform Plan

```bash
aws codebuild batch-get-projects \\
  --names fcaj-devsecops-dev-terraform-plan \\
  --query 'projects[0].environment.environmentVariables[?name==`TF_VAR_instance_profile_name`].[name,value]' \\
  --output table
```

> [!WARNING]
> Nếu source `platform/codebuild.tf` đã có `TF_VAR_instance_profile_name` nhưng lệnh này không trả biến, cấu hình CodeBuild thật trên AWS chưa được platform Terraform apply lại.""",
        """Project Terraform Plan uses `TerraformPlanRole`, CodePipeline source/artifacts, workload S3 backend, and required `TF_VAR` variables to produce the exact configuration that Apply will deploy.

### Inspect Terraform Plan Runtime Variables

```bash
aws codebuild batch-get-projects \\
  --names fcaj-devsecops-dev-terraform-plan \\
  --query 'projects[0].environment.environmentVariables[?name==`TF_VAR_instance_profile_name`].[name,value]' \\
  --output table
```

> [!WARNING]
> If `platform/codebuild.tf` contains `TF_VAR_instance_profile_name` but this CLI command returns empty, the actual AWS CodeBuild project configuration has not been updated via platform Terraform apply.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )

    # 5.6.2
    write_section(
        p / "5.6.2-execute-terraform-init",
        "5.6.2",
        "Thực hiện Terraform Init",
        "Execute Terraform Init",
        "`cicd/buildspec-plan.yml`",
        """```bash
terraform -chdir="${WORKLOAD_DIR}" init -input=false -reconfigure \\
  -backend-config="bucket=${TF_STATE_BUCKET}" \\
  -backend-config="key=${TF_STATE_KEY}" \\
  -backend-config="region=${AWS_DEFAULT_REGION}" \\
  -backend-config="encrypt=true" \\
  -backend-config="use_lockfile=true"
```""",
        """```bash
terraform -chdir="${WORKLOAD_DIR}" init -input=false -reconfigure \\
  -backend-config="bucket=${TF_STATE_BUCKET}" \\
  -backend-config="key=${TF_STATE_KEY}" \\
  -backend-config="region=${AWS_DEFAULT_REGION}" \\
  -backend-config="encrypt=true" \\
  -backend-config="use_lockfile=true"
```""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )

    # 5.6.3
    write_section(
        p / "5.6.3-generate-terraform-plan",
        "5.6.3",
        "Sinh Terraform Plan",
        "Generate Terraform Plan",
        "`cicd/buildspec-plan.yml`",
        """```bash
terraform -chdir="${WORKLOAD_DIR}" validate
terraform -chdir="${WORKLOAD_DIR}" plan -input=false -out=tfplan
terraform -chdir="${WORKLOAD_DIR}" show -no-color tfplan > "${WORKLOAD_DIR}/plan.txt"
```

`tfplan` là binary plan dùng cho Apply; `plan.txt` là bản text để reviewer đọc trước khi phê duyệt.""",
        """```bash
terraform -chdir="${WORKLOAD_DIR}" validate
terraform -chdir="${WORKLOAD_DIR}" plan -input=false -out=tfplan
terraform -chdir="${WORKLOAD_DIR}" show -no-color tfplan > "${WORKLOAD_DIR}/plan.txt"
```

`tfplan` is the binary plan consumed by Apply; `plan.txt` is the human-readable text review file for approvers.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )

    # 5.6.4
    write_section(
        p / "5.6.4-store-tfplan-artifact",
        "5.6.4",
        "Lưu tfplan làm Artifact",
        "Store tfplan as Artifact",
        "`cicd/buildspec-plan.yml`",
        """```yaml
artifacts:
  base-directory: workload
  files:
    - tfplan
    - plan.txt
    - .terraform.lock.hcl
  discard-paths: yes
```

CodePipeline nhận output artifact tên `PlanOutput`. Apply stage lấy đúng `tfplan` và `.terraform.lock.hcl` từ artifact này.""",
        """```yaml
artifacts:
  base-directory: workload
  files:
    - tfplan
    - plan.txt
    - .terraform.lock.hcl
  discard-paths: yes
```

CodePipeline captures the output artifact named `PlanOutput`. The Apply stage consumes `tfplan` and `.terraform.lock.hcl` directly from this artifact.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )

    # 5.6.5
    write_section(
        p / "5.6.5-create-manual-approval-stage",
        "5.6.5",
        "Tạo Manual Approval Stage",
        "Create Manual Approval Stage",
        "`platform/pipeline.tf`, `platform/secrets_notifications.tf`",
        """ManualApproval dùng provider Manual và gửi notification qua SNS topic của pipeline. CustomData yêu cầu reviewer mở `PlanOutput/plan.txt` và chỉ approve khi thay đổi là đúng và an toàn.""",
        """ManualApproval utilizes the Manual approval provider and notifies operators via the pipeline SNS topic. CustomData prompts reviewers to inspect `PlanOutput/plan.txt` and approve only safe, expected changes.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    # 5.6.6
    write_section(
        p / "5.6.6-review-approve-infrastructure",
        "5.6.6",
        "Review và phê duyệt thay đổi hạ tầng",
        "Review and Approve Infrastructure Changes",
        "AWS CodePipeline Console",
        """Khi pipeline dừng tại `ManualApproval`, reviewer đọc `plan.txt`, kiểm tra resource create/change/destroy, sau đó chọn **Approve** hoặc **Reject** trên CodePipeline Console. Chỉ Approve mới cho phép TerraformApply chạy.

### Bash/Checklist mẫu - trước Manual Approval

```bash
# Review nhanh state lock trước khi approve execution mới
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/" | grep tflock || true

# Trong CodePipeline Console:
# TerraformPlan -> PlanOutput/plan.txt -> Review
# ManualApproval -> Approve hoặc Reject
```

> [!IMPORTANT]
> Không chạy nhiều execution chồng lên nhau trong lúc TerraformApply đang giữ state lock. Nếu một Plan mới bị lock, chờ Apply cũ kết thúc rồi retry execution mới.

---

> **[📝 Ảnh chụp đề xuất]**  
> CodePipeline ManualApproval ở trạng thái Waiting for approval, kèm nội dung review plan.
""",
        """When the pipeline pauses at `ManualApproval`, reviewers read `plan.txt`, inspect resources to create/change/destroy, and select **Approve** or **Reject** in the CodePipeline Console. Only approval unlocks TerraformApply.

### Sample Checklist / Bash - Before Manual Approval

```bash
# Quick state lock check before approving a new execution
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/" | grep tflock || true

# In CodePipeline Console:
# TerraformPlan -> PlanOutput/plan.txt -> Review
# ManualApproval -> Approve or Reject
```

> [!IMPORTANT]
> Avoid triggering overlapping pipeline executions while TerraformApply holds state lock. If a new Plan is locked, wait for prior Apply completion and retry.

---

> **[📝 Recommended Screenshot]**  
> CodePipeline ManualApproval in Waiting for approval state showing plan review details.
""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=6
    )

    # Parent 5.6
    write_parent(
        p,
        "5.6",
        "Terraform Plan & Manual Approval",
        "Terraform Plan & Manual Approval",
        "Chương này hướng dẫn sinh kế hoạch thay đổi hạ tầng tfplan an toàn, đóng gói artifact và thiết lập cổng phê duyệt thủ công có kiểm soát trước khi áp dụng vào môi trường AWS.",
        "This chapter covers generating immutable Terraform plans, packaging artifacts, and enforcing gated manual approvals prior to cloud mutation.",
        sub_list,
        6
    )

def build_5_7():
    p = BASE_DIR / "5.7-Terraform-Apply"
    sub_list = [
        {"num": "5.7.1", "dir": "5.7.1-codebuild-terraform-apply", "title_vi": "Tạo CodeBuild Project cho Terraform Apply", "title_en": "Create CodeBuild Project for Terraform Apply", "summary_vi": "Khởi tạo project terraform-apply-smoke dùng chung cho cả apply và smoke", "summary_en": "Provision terraform-apply-smoke project supporting both apply and smoke modes"},
        {"num": "5.7.2", "dir": "5.7.2-assume-deploy-role", "title_vi": "Assume TerraformDeployRole", "title_en": "Assume TerraformDeployRole", "summary_vi": "Chạy với service_role là TerraformDeployRole có quyền hạn mutation chuẩn", "summary_en": "Execute with TerraformDeployRole service role enforcing bounded mutation scope"},
        {"num": "5.7.3", "dir": "5.7.3-consume-approved-plan", "title_vi": "Sử dụng Terraform Plan đã được phê duyệt", "title_en": "Consume Approved Terraform Plan", "summary_vi": "Sao chép chính xác tfplan và lockfile từ PlanOutput artifact", "summary_en": "Copy exact tfplan and lockfile from PlanOutput without re-planning"},
        {"num": "5.7.4", "dir": "5.7.4-execute-terraform-apply", "title_vi": "Thực hiện Terraform Apply", "title_en": "Execute Terraform Apply", "summary_vi": "Áp dụng thay đổi và trích xuất các outputs không nhạy cảm", "summary_en": "Apply changes via approved plan and extract non-sensitive workload outputs"},
        {"num": "5.7.5", "dir": "5.7.5-verify-deployment-status", "title_vi": "Kiểm tra trạng thái Deployment", "title_en": "Verify Deployment Status", "summary_vi": "Xác nhận hạ tầng tạo thành công trước khi chuyển sang bước smoke test", "summary_en": "Verify deployment status in CodeBuild and remote state reconciliation"},
    ]

    # 5.7.1
    write_section(
        p / "5.7.1-codebuild-terraform-apply",
        "5.7.1",
        "Tạo CodeBuild Project cho Terraform Apply",
        "Create CodeBuild Project for Terraform Apply",
        "`platform/codebuild.tf`, `cicd/buildspec-apply.yml`",
        """Project `terraform-apply-smoke` sử dụng `TerraformDeployRole` và cùng buildspec cho hai chế độ `apply` và `smoke`. Ở apply mode, project nhận `SourceOutput` và `PlanOutput` từ CodePipeline.""",
        """Project `terraform-apply-smoke` uses `TerraformDeployRole` and a shared buildspec for both `apply` and `smoke` modes. In apply mode, it accepts `SourceOutput` and `PlanOutput` from CodePipeline.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )

    # 5.7.2
    write_section(
        p / "5.7.2-assume-deploy-role",
        "5.7.2",
        "Assume TerraformDeployRole",
        "Assume TerraformDeployRole",
        "`platform/iam.tf`, `platform/codebuild.tf`",
        """CodeBuild project chạy trực tiếp với `service_role` là `TerraformDeployRole`; vì vậy mọi API Terraform gọi trong Apply đều bị giới hạn bởi deploy policy của role này.

### Cập nhật Platform khi sửa IAM/CodeBuild/Pipeline

```bash
cd ~/fcaj-aws-devsecops/platform
terraform validate
terraform plan -out=platform-fix.tfplan
terraform show -no-color platform-fix.tfplan | tail -n 30
terraform apply platform-fix.tfplan
```

> [!TIP]
> Chỉ cần chạy block này khi thay đổi chính layer `platform/` hoặc `iam-policy/`. Với thay đổi `app/` hoặc `workload/` thông thường, chỉ commit/push để pipeline hiện có xử lý.""",
        """The CodeBuild project runs directly with `service_role` set to `TerraformDeployRole`; all Terraform APIs invoked during Apply are bounded by this role's policy.

### Update Platform Layer on IAM / CodeBuild / Pipeline Changes

```bash
cd ~/fcaj-aws-devsecops/platform
terraform validate
terraform plan -out=platform-fix.tfplan
terraform show -no-color platform-fix.tfplan | tail -n 30
terraform apply platform-fix.tfplan
```

> [!TIP]
> Execute this block only when modifying `platform/` or `iam-policy/`. For normal `app/` or `workload/` edits, simply commit and push to let the existing pipeline process them.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )

    # 5.7.3
    write_section(
        p / "5.7.3-consume-approved-plan",
        "5.7.3",
        "Sử dụng Terraform Plan đã được phê duyệt",
        "Consume Approved Terraform Plan",
        "`cicd/buildspec-apply.yml`",
        """```bash
cp "${CODEBUILD_SRC_DIR_PlanOutput}/.terraform.lock.hcl" "${WORKLOAD_DIR}/.terraform.lock.hcl"
cp "${CODEBUILD_SRC_DIR_PlanOutput}/tfplan" "${WORKLOAD_DIR}/tfplan"
```

Apply không chạy `terraform plan` lần nữa; nó sao chép binary plan và lock file từ `PlanOutput` để bảo đảm thay đổi được triển khai đúng với nội dung đã review.""",
        """```bash
cp "${CODEBUILD_SRC_DIR_PlanOutput}/.terraform.lock.hcl" "${WORKLOAD_DIR}/.terraform.lock.hcl"
cp "${CODEBUILD_SRC_DIR_PlanOutput}/tfplan" "${WORKLOAD_DIR}/tfplan"
```

Apply never re-runs `terraform plan`; it copies the binary plan and lock file directly from `PlanOutput` to ensure changes strictly match what was reviewed.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )

    # 5.7.4
    write_section(
        p / "5.7.4-execute-terraform-apply",
        "5.7.4",
        "Thực hiện Terraform Apply",
        "Execute Terraform Apply",
        "`cicd/buildspec-apply.yml`",
        """```bash
terraform -chdir="${WORKLOAD_DIR}" apply -input=false tfplan
```

Sau Apply, buildspec chạy `terraform output` để in các output không nhạy cảm của workload như VPC ID, instance ID, public IP, `app_url` và `health_url`.""",
        """```bash
terraform -chdir="${WORKLOAD_DIR}" apply -input=false tfplan
```

Post-apply, the buildspec executes `terraform output` to display non-sensitive workload attributes including VPC ID, instance ID, public IP, `app_url`, and `health_url`.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )

    # 5.7.5
    write_section(
        p / "5.7.5-verify-deployment-status",
        "5.7.5",
        "Kiểm tra trạng thái Deployment",
        "Verify Deployment Status",
        "AWS CodeBuild & AWS Management Console",
        """Kiểm tra CodeBuild build status, Terraform state và các resource trên AWS Console. Apply phải hoàn tất trước khi `PostDeployVerification` bắt đầu.

> [!WARNING]
> **Lưu ý khi Apply lỗi giữa chừng**: Terraform có thể đã tạo một phần VPC/Subnet/SG trước khi lỗi ở EC2. Không destroy/xóa tay theo phản xạ. Sửa nguyên nhân, cập nhật platform nếu cần, rồi để execution mới plan/apply reconcile theo remote state.""",
        """Verify CodeBuild build status, Terraform state, and provisioned resources in the AWS Console. Apply must complete before `PostDeployVerification` starts.

> [!WARNING]
> **Mid-Apply Failure Recovery**: Terraform may have created partial resources (VPC/Subnet/SG) before failing on EC2. Avoid manual ad-hoc deletions. Fix root causes, update configurations if needed, and let a new pipeline execution reconcile state automatically.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    # Parent 5.7
    write_parent(
        p,
        "5.7",
        "Terraform Apply & triển khai hạ tầng AWS",
        "Terraform Apply & AWS Infrastructure Deployment",
        "Chương này hướng dẫn thực thi triển khai hạ tầng an toàn bằng đúng file tfplan đã được phê duyệt, áp dụng nguyên tắc đặc quyền tối thiểu với TerraformDeployRole.",
        "This chapter covers executing approved binary plans under TerraformDeployRole, ensuring immutable deployment without regenerating plans.",
        sub_list,
        7
    )

def build_5_8():
    p = BASE_DIR / "5.8-Target-Environment"
    sub_list = [
        {"num": "5.8.1", "dir": "5.8.1-create-vpc", "title_vi": "Khởi tạo Amazon VPC", "title_en": "Create Amazon VPC", "summary_vi": "Tạo VPC 10.20.0.0/16 với DNS hostnames và Checkov skip hợp lệ", "summary_en": "Provision VPC 10.20.0.0/16 with DNS hostnames and documented Checkov skip"},
        {"num": "5.8.2", "dir": "5.8.2-create-internet-gateway", "title_vi": "Khởi tạo Internet Gateway", "title_en": "Create Internet Gateway", "summary_vi": "Tạo và attach IGW vào VPC làm default route ra ngoài Internet", "summary_en": "Create and attach IGW providing default route to public internet"},
        {"num": "5.8.3", "dir": "5.8.3-create-public-subnet-route-table", "title_vi": "Khởi tạo Public Subnet và Route Table", "title_en": "Create Public Subnet & Route Table", "summary_vi": "Tạo Public Subnet 10.20.10.0/24 và Route Table trỏ ra IGW", "summary_en": "Configure Public Subnet 10.20.10.0/24 with default route targeting IGW"},
        {"num": "5.8.4", "dir": "5.8.4-create-security-group", "title_vi": "Khởi tạo Security Group", "title_en": "Create Security Group", "summary_vi": "Mở HTTP port 80 công khai cho demo app, tuyệt đối chặn SSH", "summary_en": "Allow HTTP port 80 for demo app while strictly blocking SSH"},
        {"num": "5.8.5", "dir": "5.8.5-create-ec2-instance", "title_vi": "Khởi tạo Amazon EC2", "title_en": "Create Amazon EC2 Instance", "summary_vi": "Tạo EC2 AL2023 t3.micro với IMDSv2 bắt buộc và SSM Instance Profile", "summary_en": "Launch EC2 AL2023 t3.micro with enforced IMDSv2 and SSM Instance Profile"},
        {"num": "5.8.6", "dir": "5.8.6-deploy-demo-web-application", "title_vi": "Triển khai Demo Web Application", "title_en": "Deploy Demo Web Application", "summary_vi": "Tự động cài đặt Flask app qua user_data và quản trị systemd service", "summary_en": "Bootstrap Flask demo application via user_data and systemd service"},
        {"num": "5.8.7", "dir": "5.8.7-verify-application-access", "title_vi": "Kiểm tra truy cập ứng dụng", "title_en": "Verify Application Accessibility", "summary_vi": "Kiểm tra endpoint / và /health trả về status 200 OK", "summary_en": "Verify live accessibility of / and /health endpoints returning HTTP 200"},
    ]

    # 5.8.1
    write_section(
        p / "5.8.1-create-vpc",
        "5.8.1",
        "Khởi tạo Amazon VPC",
        "Create Amazon VPC",
        "`workload/main.tf`, `workload/variables.tf`",
        """Workload tạo VPC CIDR mặc định `10.20.0.0/16`, bật DNS support và DNS hostnames. VPC Flow Logs được bỏ qua có chủ đích để giữ Workshop nhỏ và chi phí thấp, có Checkov skip comment trong source.""",
        """Workload provisions a VPC with default CIDR `10.20.0.0/16`, enabling DNS support and hostnames. VPC Flow Logs are intentionally omitted to keep workshop costs minimal, accompanied by explicit Checkov skip comments.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )

    # 5.8.2
    write_section(
        p / "5.8.2-create-internet-gateway",
        "5.8.2",
        "Khởi tạo Internet Gateway",
        "Create Internet Gateway",
        "`workload/main.tf`",
        """Internet Gateway được attach trực tiếp vào VPC và dùng làm target cho default route của public route table.""",
        """The Internet Gateway attaches directly to the VPC, serving as the target for the default route (`0.0.0.0/0`) in the public route table.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )

    # 5.8.3
    write_section(
        p / "5.8.3-create-public-subnet-route-table",
        "5.8.3",
        "Khởi tạo Public Subnet và Route Table",
        "Create Public Subnet & Route Table",
        "`workload/main.tf`",
        """Public Subnet mặc định `10.20.10.0/24`, nằm ở Availability Zone đầu tiên trong danh sách available và bật `map_public_ip_on_launch=true`. Route table có route `0.0.0.0/0` qua Internet Gateway.""",
        """Public Subnet defaults to `10.20.10.0/24`, placed in the first available AZ with `map_public_ip_on_launch=true`. The route table routes `0.0.0.0/0` outbound through the Internet Gateway.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )

    # 5.8.4
    write_section(
        p / "5.8.4-create-security-group",
        "5.8.4",
        "Khởi tạo Security Group",
        "Create Security Group",
        "`workload/main.tf`",
        """Security Group baseline cho phép HTTP TCP/80 từ `allowed_http_cidr` mặc định `0.0.0.0/0` để demo endpoint có thể truy cập công khai. Egress cho phép all để EC2 bootstrap cài package. Baseline không tạo rule SSH public.""",
        """The baseline Security Group allows HTTP TCP/80 from `allowed_http_cidr` (default `0.0.0.0/0`) for public accessibility. Egress permits all outbound traffic for bootstrap package installation. Baseline contains zero public SSH rules.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )

    # 5.8.5
    write_section(
        p / "5.8.5-create-ec2-instance",
        "5.8.5",
        "Khởi tạo Amazon EC2",
        "Create Amazon EC2 Instance",
        "`workload/main.tf`",
        """EC2 dùng AMI Amazon Linux 2023 mới nhất, instance type mặc định `t3.micro`, public IPv4, encrypted gp3 root volume, detailed monitoring, EBS optimized và IMDSv2 bắt buộc (`http_tokens=required`). EC2 gắn `EC2DemoProfile`/`EC2DemoRole` có `AmazonSSMManagedInstanceCore` để truy cập Session Manager mà không cần mở SSH public.""",
        """EC2 runs the latest Amazon Linux 2023 AMI, instance type `t3.micro`, public IPv4, encrypted gp3 root volume, detailed monitoring, EBS optimization, and enforced IMDSv2 (`http_tokens=required`). It attaches `EC2DemoProfile`/`EC2DemoRole` with `AmazonSSMManagedInstanceCore` for SSH-free administration via Session Manager.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    # 5.8.6
    write_section(
        p / "5.8.6-deploy-demo-web-application",
        "5.8.6",
        "Triển khai Demo Web Application",
        "Deploy Demo Web Application",
        "`workload/user_data.sh.tftpl`, `app/app.py`, `app/requirements.txt`",
        """Terraform base64-encode `app.py` và `requirements.txt` vào `user_data`. EC2 cài Python/pip bằng dnf, giải mã source vào `/opt/fcaj-demo`, cài dependency và tạo systemd service chạy Flask app ở port 80.

### Bootstrap EC2

```bash
# Trích đoạn user_data ổn định trên Amazon Linux 2023
dnf install -y python3 python3-pip
mkdir -p /opt/fcaj-demo
python3 -m pip install -r /opt/fcaj-demo/requirements.txt
systemctl daemon-reload
systemctl enable --now fcaj-demo.service
```

> [!WARNING]
> Trên Amazon Linux 2023 **không chạy** `python3 -m pip install --upgrade pip` vì pip hệ thống được RPM quản lý và có thể làm cloud-init fail. Nếu user_data thay đổi, `aws_instance.web` dùng `user_data_replace_on_change=true` nên Terraform có thể replace EC2 để chạy bootstrap mới.

### app/app.py

```python
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(
        service="fcaj-devsecops-demo",
        message="AWS DevSecOps workshop application is running",
        status="ok",
    )

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    host = os.environ.get("APP_HOST", "127.0.0.1")
    port = int(os.environ.get("APP_PORT", "8080"))
    app.run(host=host, port=port, debug=False)
```""",
        """Terraform base64-encodes `app.py` and `requirements.txt` into `user_data`. EC2 installs Python/pip via dnf, decodes source into `/opt/fcaj-demo`, installs dependencies, and creates a systemd service running Flask on port 80.

### EC2 Bootstrap Snippet

```bash
# Stable user_data snippet for Amazon Linux 2023
dnf install -y python3 python3-pip
mkdir -p /opt/fcaj-demo
python3 -m pip install -r /opt/fcaj-demo/requirements.txt
systemctl daemon-reload
systemctl enable --now fcaj-demo.service
```

> [!WARNING]
> On Amazon Linux 2023, **do not execute** `python3 -m pip install --upgrade pip` as system pip is RPM-managed and upgrading can break cloud-init. If user_data changes, `user_data_replace_on_change=true` allows Terraform to replace the instance cleanly.

### app/app.py

```python
import os
from flask import Flask, jsonify

app = Flask(__name__)

@app.get("/")
def index():
    return jsonify(
        service="fcaj-devsecops-demo",
        message="AWS DevSecOps workshop application is running",
        status="ok",
    )

@app.get("/health")
def health():
    return jsonify(status="ok"), 200

if __name__ == "__main__":
    host = os.environ.get("APP_HOST", "127.0.0.1")
    port = int(os.environ.get("APP_PORT", "8080"))
    app.run(host=host, port=port, debug=False)
```""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=6
    )

    # 5.8.7
    write_section(
        p / "5.8.7-verify-application-access",
        "5.8.7",
        "Kiểm tra truy cập ứng dụng",
        "Verify Application Accessibility",
        "`workload/outputs.tf`",
        """Workload xuất `app_url` và `health_url` từ public IP của EC2. Endpoint `/` trả thông tin service và status; `/health` trả JSON `{"status":"ok"}` với HTTP 200.

```bash
terraform -chdir=workload output app_url
terraform -chdir=workload output health_url
curl "$(terraform -chdir=workload output -raw health_url)"
```

### Kiểm tra EC2 và health endpoint

```bash
aws ec2 describe-instances \\
  --filters "Name=tag:Name,Values=fcaj-devsecops-dev-web" \\
  --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,IP:PublicIpAddress}' \\
  --output table

HEALTH_URL="$(terraform -chdir=workload output -raw health_url)"
echo "$HEALTH_URL"
curl --fail --show-error "$HEALTH_URL"
```""",
        """Workload exports `app_url` and `health_url` computed from the EC2 public IP. Endpoint `/` returns service info and status; `/health` returns JSON `{"status":"ok"}` with HTTP 200.

```bash
terraform -chdir=workload output app_url
terraform -chdir=workload output health_url
curl "$(terraform -chdir=workload output -raw health_url)"
```

### Inspect EC2 and Health Endpoint

```bash
aws ec2 describe-instances \\
  --filters "Name=tag:Name,Values=fcaj-devsecops-dev-web" \\
  --query 'Reservations[].Instances[].{ID:InstanceId,State:State.Name,IP:PublicIpAddress}' \\
  --output table

HEALTH_URL="$(terraform -chdir=workload output -raw health_url)"
echo "$HEALTH_URL"
curl --fail --show-error "$HEALTH_URL"
```""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=7
    )

    # Parent 5.8
    write_parent(
        p,
        "5.8",
        "Triển khai Target AWS Environment",
        "Target AWS Environment Deployment",
        "Chương này hướng dẫn xây dựng hạ tầng mạng VPC an toàn và khởi tạo máy chủ Amazon EC2 chạy ứng dụng web demo tự động bằng user_data.",
        "This chapter guides through provisioning target network VPC infrastructure and deploying an EC2 instance hosting the demo Flask web application.",
        sub_list,
        8
    )

if __name__ == "__main__":
    build_5_5()
    build_5_6()
    build_5_7()
    build_5_8()
    print("Modules 5.5 - 5.8 built successfully!")
