import os
from pathlib import Path
from generator_common import BASE_DIR, write_section, write_parent

def build_5_9():
    p = BASE_DIR / "5.9-Post-Deploy-Verification"
    sub_list = [
        {"num": "5.9.1", "dir": "5.9.1-codebuild-smoke-test", "title_vi": "Tạo CodeBuild Smoke Test", "title_en": "Create CodeBuild Smoke Test", "summary_vi": "Tái sử dụng project terraform-apply-smoke với RUN_MODE=smoke", "summary_en": "Reuse terraform-apply-smoke project under RUN_MODE=smoke"},
        {"num": "5.9.2", "dir": "5.9.2-verify-ec2-instance", "title_vi": "Kiểm tra EC2 Instance", "title_en": "Verify EC2 Instance Status", "summary_vi": "Cơ chế chờ đợi và retry khi EC2 thực hiện user_data bootstrap", "summary_en": "Wait and retry loop during initial EC2 user_data bootstrap"},
        {"num": "5.9.3", "dir": "5.9.3-verify-http-endpoint", "title_vi": "Kiểm tra HTTP Endpoint", "title_en": "Verify HTTP Endpoint", "summary_vi": "Trích xuất health_url trực tiếp từ Terraform outputs", "summary_en": "Extract health_url directly from Terraform workload outputs"},
        {"num": "5.9.4", "dir": "5.9.4-verify-http-status-code", "title_vi": "Kiểm tra HTTP Status Code", "title_en": "Verify HTTP Status Code", "summary_vi": "Dùng lệnh curl kiểm tra HTTP response 200 và JSON status ok", "summary_en": "Execute curl verification ensuring HTTP 200 and JSON status ok"},
        {"num": "5.9.5", "dir": "5.9.5-handle-smoke-test-failure", "title_vi": "Xử lý khi Smoke Test thất bại", "title_en": "Handle Smoke Test Failure", "summary_vi": "Thử tối đa 24 lần x 10s, kèm bộ lệnh chẩn đoán chi tiết", "summary_en": "Retry 24 times x 10s with comprehensive diagnostics via Session Manager"},
        {"num": "5.9.6", "dir": "5.9.6-confirm-deployment-success", "title_vi": "Xác nhận Deployment thành công", "title_en": "Confirm Deployment Success", "summary_vi": "Chỉ khi smoke test pass thì toàn bộ pipeline mới chuyển SUCCEEDED", "summary_en": "Pipeline transitions to SUCCEEDED only after smoke tests pass"},
    ]

    # 5.9.1
    write_section(
        p / "5.9.1-codebuild-smoke-test",
        "5.9.1",
        "Tạo CodeBuild Smoke Test",
        "Create CodeBuild Smoke Test",
        "`platform/codebuild.tf`, `cicd/buildspec-apply.yml`",
        """Không tạo project CodeBuild thứ tư; project `terraform-apply-smoke` được tái sử dụng với `RUN_MODE=smoke`. Điều này giữ đúng thiết kế chỉ có 3 buildspec/project logic chính.""",
        """No fourth CodeBuild project is created; `terraform-apply-smoke` is reused with `RUN_MODE=smoke`. This preserves the streamlined design of exactly 3 buildspec files/project logics across the architecture.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )

    # 5.9.2
    write_section(
        p / "5.9.2-verify-ec2-instance",
        "5.9.2",
        "Kiểm tra EC2 Instance",
        "Verify EC2 Instance Status",
        "AWS CodeBuild & Amazon EC2",
        """Smoke stage chạy sau TerraformApply, vì vậy Terraform state đã có `instance_id`/`public_ip`. Việc EC2 `user_data` hoàn tất có thể mất thời gian ngắn nên smoke test có cơ chế retry.""",
        """The smoke stage executes after TerraformApply, so Terraform state already holds `instance_id` and `public_ip`. Because EC2 `user_data` needs time to complete bootstrap, the smoke test incorporates a retry loop.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )

    # 5.9.3
    write_section(
        p / "5.9.3-verify-http-endpoint",
        "5.9.3",
        "Kiểm tra HTTP Endpoint",
        "Verify HTTP Endpoint",
        "`workload/outputs.tf`, `cicd/buildspec-apply.yml`",
        """```bash
HEALTH_URL="$(terraform -chdir="${WORKLOAD_DIR}" output -raw health_url)"
```""",
        """```bash
HEALTH_URL="$(terraform -chdir="${WORKLOAD_DIR}" output -raw health_url)"
```""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )

    # 5.9.4
    write_section(
        p / "5.9.4-verify-http-status-code",
        "5.9.4",
        "Kiểm tra HTTP Status Code",
        "Verify HTTP Status Code",
        "`cicd/buildspec-apply.yml`",
        """```bash
curl --fail --silent --show-error --max-time 10 "${HEALTH_URL}" | grep -q '"status":"ok"'
```

`curl --fail` yêu cầu HTTP response không thuộc nhóm lỗi; kết quả còn phải chứa JSON status ok để được xem là pass.""",
        """```bash
curl --fail --silent --show-error --max-time 10 "${HEALTH_URL}" | grep -q '"status":"ok"'
```

`curl --fail` ensures non-error HTTP response codes (non-4xx/5xx), while grep verifies the JSON payload contains `"status":"ok"`.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )

    # 5.9.5
    write_section(
        p / "5.9.5-handle-smoke-test-failure",
        "5.9.5",
        "Xử lý khi Smoke Test thất bại",
        "Handle Smoke Test Failure",
        "`cicd/buildspec-apply.yml`",
        """Smoke test thử tối đa 24 lần, mỗi lần thất bại chờ 10 giây để EC2 hoàn tất bootstrap. Nếu hết retry mà vẫn không nhận được health response đúng, build exit 1 và pipeline thất bại.

### Chẩn đoán PostDeployVerification

```bash
# Chạy trong EC2 Session Manager khi smoke test vẫn Connection refused
sudo cloud-init status --long
sudo grep -nEi 'error|failed|failure|traceback|denied|not found|pip|dnf' \\
  /var/log/cloud-init-output.log | tail -n 80 || true
sudo systemctl status fcaj-demo --no-pager || true
sudo journalctl -u fcaj-demo -n 100 --no-pager || true
sudo ss -ltnp | grep ':80' || true
curl -v http://127.0.0.1/health

# Nếu cloud-init-output.log không tồn tại
sudo journalctl -u cloud-final.service -b --no-pager -n 200
```

> [!WARNING]
> Connection refused thường nghĩa là EC2 đã reachable nhưng ứng dụng chưa listen port 80. Hãy kiểm tra cloud-init/systemd trước khi thay đổi Security Group.""",
        """Smoke test retries up to 24 times, waiting 10 seconds between attempts for EC2 bootstrap completion. If retries expire without healthy responses, the build exits 1 and the pipeline fails.

### PostDeployVerification Diagnostics via Session Manager

```bash
# Execute in EC2 Session Manager when smoke test reports Connection refused
sudo cloud-init status --long
sudo grep -nEi 'error|failed|failure|traceback|denied|not found|pip|dnf' \\
  /var/log/cloud-init-output.log | tail -n 80 || true
sudo systemctl status fcaj-demo --no-pager || true
sudo journalctl -u fcaj-demo -n 100 --no-pager || true
sudo ss -ltnp | grep ':80' || true
curl -v http://127.0.0.1/health

# If cloud-init-output.log is absent
sudo journalctl -u cloud-final.service -b --no-pager -n 200
```

> [!WARNING]
> Connection refused typically indicates the EC2 instance is reachable but the app is not yet listening on port 80. Inspect cloud-init and systemd logs before modifying Security Groups.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    # 5.9.6
    write_section(
        p / "5.9.6-confirm-deployment-success",
        "5.9.6",
        "Xác nhận Deployment thành công",
        "Confirm Deployment Success",
        "AWS CodePipeline",
        """Chỉ khi `PostDeployVerification` thành công thì toàn bộ pipeline mới chuyển trạng thái **SUCCEEDED**. Đây là kiểm tra cuối sau khi hạ tầng đã thay đổi.""",
        """Only when `PostDeployVerification` succeeds does the entire pipeline transition to **SUCCEEDED** status. This serves as the definitive verification after infrastructure changes.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=6
    )

    # Parent 5.9
    write_parent(
        p,
        "5.9",
        "Post-Deploy Verification",
        "Post-Deploy Verification",
        "Chương này hướng dẫn kiểm tra tự động sau triển khai với vòng lặp thử lại thông minh để kiểm chứng sức khỏe của ứng dụng web trước khi hoàn tất pipeline.",
        "This chapter covers configuring automated post-deploy smoke verification loops to confirm application health before pipeline completion.",
        sub_list,
        9
    )

def build_5_10():
    p = BASE_DIR / "5.10-Logging-Monitoring-Notification"
    sub_list = [
        {"num": "5.10.1", "dir": "5.10.1-cloudwatch-codebuild-logs", "title_vi": "Theo dõi CodeBuild bằng Amazon CloudWatch", "title_en": "Monitor CodeBuild via Amazon CloudWatch", "summary_vi": "Tạo 3 Log Group chuyên biệt với retention 14 ngày", "summary_en": "Provision 3 dedicated CloudWatch Log Groups with 14-day retention"},
        {"num": "5.10.2", "dir": "5.10.2-track-codepipeline-status", "title_vi": "Theo dõi trạng thái AWS CodePipeline", "title_en": "Track AWS CodePipeline Status", "summary_vi": "Quan sát trạng thái execution và chuyển biến các stage trên console", "summary_en": "Monitor pipeline stage executions and transition states in console"},
        {"num": "5.10.3", "dir": "5.10.3-eventbridge-rule-pipeline", "title_vi": "Tạo EventBridge Rule cho Pipeline Event", "title_en": "Create EventBridge Rule for Pipeline Events", "summary_vi": "Bắt các sự kiện FAILED, SUCCEEDED, CANCELED chuyển tiếp tới SNS", "summary_en": "Catch FAILED, SUCCEEDED, CANCELED events and route to SNS topic"},
        {"num": "5.10.4", "dir": "5.10.4-create-sns-topic", "title_vi": "Tạo Amazon SNS Topic", "title_en": "Create Amazon SNS Topic", "summary_vi": "Thiết lập SNS topic nhận approval và event notifications", "summary_en": "Create unified SNS topic for approval requests and state notifications"},
        {"num": "5.10.5", "dir": "5.10.5-send-email-notification", "title_vi": "Gửi Email Notification", "title_en": "Configure Email Notifications", "summary_vi": "Đăng ký email nhận thông báo cảnh báo và phê duyệt hạ tầng", "summary_en": "Subscribe email endpoints for pipeline approvals and cost alerts"},
        {"num": "5.10.6", "dir": "5.10.6-cloudtrail-audit", "title_vi": "Audit hoạt động bằng AWS CloudTrail", "title_en": "Audit Operations via AWS CloudTrail", "summary_vi": "Ghi log kiểm toán API toàn diện vào dedicated S3 bucket", "summary_en": "Capture comprehensive management API audit trails into dedicated S3 bucket"},
        {"num": "5.10.7", "dir": "5.10.7-aws-budgets-cost", "title_vi": "Theo dõi chi phí bằng AWS Budgets", "title_en": "Track Costs with AWS Budgets", "summary_vi": "Thiết lập ngân sách 5 USD/tháng và cảnh báo khi chạm 80%", "summary_en": "Configure $5/month budget with 80% threshold email notifications"},
    ]

    # 5.10.1
    write_section(
        p / "5.10.1-cloudwatch-codebuild-logs",
        "5.10.1",
        "Theo dõi CodeBuild bằng Amazon CloudWatch",
        "Monitor CodeBuild via Amazon CloudWatch",
        "`platform/codebuild.tf`",
        """Platform tạo 3 CloudWatch Log Group cho `validate-security`, `terraform-plan` và `terraform-apply-smoke`. Retention mặc định 14 ngày và được cấu hình bằng `cloudwatch_log_retention_days`.""",
        """The platform provisions 3 CloudWatch Log Groups for `validate-security`, `terraform-plan`, and `terraform-apply-smoke`. Retention defaults to 14 days configurable via `cloudwatch_log_retention_days`.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=1
    )

    # 5.10.2
    write_section(
        p / "5.10.2-track-codepipeline-status",
        "5.10.2",
        "Theo dõi trạng thái AWS CodePipeline",
        "Track AWS CodePipeline Status",
        "`platform/pipeline.tf`",
        """CodePipeline Console hiển thị trạng thái từng stage/action và execution. EventBridge rule còn theo dõi trạng thái pipeline tổng thể `FAILED`, `SUCCEEDED` và `CANCELED`.""",
        """CodePipeline Console displays status for each stage/action and execution. EventBridge rule also tracks high-level execution states `FAILED`, `SUCCEEDED`, and `CANCELED`.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=2
    )

    # 5.10.3
    write_section(
        p / "5.10.3-eventbridge-rule-pipeline",
        "5.10.3",
        "Tạo EventBridge Rule cho Pipeline Event",
        "Create EventBridge Rule for Pipeline Events",
        "`platform/pipeline.tf`",
        """### EventBridge rule + target SNS

```hcl
resource "aws_cloudwatch_event_rule" "pipeline_state" {
  name        = "${local.name}-pipeline-state"
  description = "Send pipeline success/failure state changes to SNS."
  event_pattern = jsonencode({
    source        = ["aws.codepipeline"]
    "detail-type" = ["CodePipeline Pipeline Execution State Change"]
    detail = {
      pipeline = [aws_codepipeline.main.name]
      state    = ["FAILED", "SUCCEEDED", "CANCELED"]
    }
  })
}

resource "aws_cloudwatch_event_target" "pipeline_state_sns" {
  rule      = aws_cloudwatch_event_rule.pipeline_state.name
  target_id = "PipelineSns"
  arn       = aws_sns_topic.pipeline.arn
  depends_on = [aws_sns_topic_policy.pipeline]
}
```""",
        """### EventBridge Rule + Target SNS

```hcl
resource "aws_cloudwatch_event_rule" "pipeline_state" {
  name        = "${local.name}-pipeline-state"
  description = "Send pipeline success/failure state changes to SNS."
  event_pattern = jsonencode({
    source        = ["aws.codepipeline"]
    "detail-type" = ["CodePipeline Pipeline Execution State Change"]
    detail = {
      pipeline = [aws_codepipeline.main.name]
      state    = ["FAILED", "SUCCEEDED", "CANCELED"]
    }
  })
}

resource "aws_cloudwatch_event_target" "pipeline_state_sns" {
  rule      = aws_cloudwatch_event_rule.pipeline_state.name
  target_id = "PipelineSns"
  arn       = aws_sns_topic.pipeline.arn
  depends_on = [aws_sns_topic_policy.pipeline]
}
```""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=3
    )

    # 5.10.4
    write_section(
        p / "5.10.4-create-sns-topic",
        "5.10.4",
        "Tạo Amazon SNS Topic",
        "Create Amazon SNS Topic",
        "`platform/secrets_notifications.tf`",
        """SNS topic `${local.name}-pipeline-notifications` nhận cả Manual Approval notification và EventBridge pipeline state notification. Topic policy cho phép account owner và `events.amazonaws.com` publish.""",
        """SNS topic `${local.name}-pipeline-notifications` receives both Manual Approval notifications and EventBridge pipeline state notifications. Topic policy allows account owner and `events.amazonaws.com` to publish.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=4
    )

    # 5.10.5
    write_section(
        p / "5.10.5-send-email-notification",
        "5.10.5",
        "Gửi Email Notification",
        "Configure Email Notifications",
        "`platform/secrets_notifications.tf`",
        """Nếu `notification_email` khác rỗng, Terraform tạo SNS email subscription. Người nhận phải confirm subscription trước khi email có thể nhận notification. AWS Budgets cũng dùng email này cho cảnh báo cost.

### Kiểm tra SNS email subscription

```bash
cd ~/fcaj-aws-devsecops/platform
TOPIC_ARN="$(terraform output -raw approval_topic_arn)"
aws sns list-subscriptions-by-topic \\
  --topic-arn "$TOPIC_ARN" \\
  --region ap-southeast-1 \\
  --output table
```

> [!NOTE]
> Email nhận SNS không bắt buộc trùng email đăng ký AWS. Nếu SubscriptionArn là `PendingConfirmation`, mở email AWS Notification và Confirm subscription trước khi chờ notification.""",
        """When `notification_email` is provided, Terraform establishes an SNS email subscription. Recipients must confirm the subscription email to activate alerts. AWS Budgets also utilizes this address.

### Inspect SNS Email Subscription

```bash
cd ~/fcaj-aws-devsecops/platform
TOPIC_ARN="$(terraform output -raw approval_topic_arn)"
aws sns list-subscriptions-by-topic \\
  --topic-arn "$TOPIC_ARN" \\
  --region ap-southeast-1 \\
  --output table
```

> [!NOTE]
> The subscriber email does not need to match the AWS root account email. If SubscriptionArn is `PendingConfirmation`, open the AWS Notification email and click Confirm subscription.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=5
    )

    # 5.10.6
    write_section(
        p / "5.10.6-cloudtrail-audit",
        "5.10.6",
        "Audit hoạt động bằng AWS CloudTrail",
        "Audit Operations via AWS CloudTrail",
        "`platform/cloudtrail.tf`",
        """Khi `enable_cloudtrail=true`, project tạo dedicated CloudTrail và S3 log bucket. Bucket có Block Public Access, BucketOwnerEnforced và AES256 encryption. Trail bật log file validation, global service events và logging.""",
        """When `enable_cloudtrail=true`, the project provisions a dedicated CloudTrail and S3 log bucket with BPA, BucketOwnerEnforced, and AES256 encryption. Trail enables log file validation, global service events, and active logging.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=6
    )

    # 5.10.7
    write_section(
        p / "5.10.7-aws-budgets-cost",
        "5.10.7",
        "Theo dõi chi phí bằng AWS Budgets",
        "Track Costs with AWS Budgets",
        "`platform/secrets_notifications.tf`, `platform/variables.tf`",
        """Budget mặc định là 5 USD/tháng. Nếu có notification email, Budget tạo alert khi actual cost vượt 80% budget. Đây là cơ chế cảnh báo, không tự động dừng tài nguyên.""",
        """Budget defaults to $5/month. When configured with an email address, an alert triggers if actual spend exceeds 80%. This provides advisory notification without stopping workloads.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=7
    )

    # Parent 5.10
    write_parent(
        p,
        "5.10",
        "Logging, Monitoring & Notification",
        "Logging, Monitoring & Notification",
        "Chương này hướng dẫn xây dựng hệ sinh thái giám sát vận hành toàn diện với Amazon CloudWatch, EventBridge, SNS Notifications, AWS CloudTrail Audit và kiểm soát chi phí bằng AWS Budgets.",
        "This chapter covers operational visibility, event alerts, API audit logging, and financial controls using CloudWatch, EventBridge, SNS, CloudTrail, and AWS Budgets.",
        sub_list,
        10
    )

def build_5_11():
    p = BASE_DIR / "5.11-DevSecOps-Pipeline"
    sub_list = [
        {"num": "5.11.1", "dir": "5.11.1-source-stage", "title_vi": "Source Stage", "title_en": "Source Stage", "summary_vi": "Lấy source từ GitHub qua CodeConnections xuất ra SourceOutput", "summary_en": "Pull code from GitHub via CodeConnections into SourceOutput"},
        {"num": "5.11.2", "dir": "5.11.2-validate-test-stage", "title_vi": "Validate & Test Stage", "title_en": "Validate & Test Stage", "summary_vi": "Gọi CodeBuild validate-security với RUN_MODE=validate", "summary_en": "Invoke CodeBuild validate-security with RUN_MODE=validate"},
        {"num": "5.11.3", "dir": "5.11.3-security-scan-gate-stage", "title_vi": "Security Scan & Security Gate Stage", "title_en": "Security Scan & Security Gate Stage", "summary_vi": "Chạy 4 scanner bảo mật với RUN_MODE=security", "summary_en": "Execute 4 security scanners under RUN_MODE=security"},
        {"num": "5.11.4", "dir": "5.11.4-terraform-plan-stage", "title_vi": "Terraform Plan Stage", "title_en": "Terraform Plan Stage", "summary_vi": "Tạo PlanOutput chứa tfplan, plan.txt và .terraform.lock.hcl", "summary_en": "Generate PlanOutput holding tfplan, plan.txt, and lockfile"},
        {"num": "5.11.5", "dir": "5.11.5-manual-approval-stage", "title_vi": "Manual Approval Stage", "title_en": "Manual Approval Stage", "summary_vi": "Yêu cầu reviewer đọc plan.txt và thực hiện Approve hoặc Reject", "summary_en": "Require human review of plan.txt before approval"},
        {"num": "5.11.6", "dir": "5.11.6-terraform-apply-stage", "title_vi": "Terraform Apply Stage", "title_en": "Terraform Apply Stage", "summary_vi": "Áp dụng đúng binary plan đã approve với vai trò TerraformDeployRole", "summary_en": "Apply the exact approved binary plan under TerraformDeployRole"},
        {"num": "5.11.7", "dir": "5.11.7-post-deploy-verification-stage", "title_vi": "Post-Deploy Verification Stage", "title_en": "Post-Deploy Verification Stage", "summary_vi": "Chạy smoke test kiểm tra endpoint /health tự động", "summary_en": "Execute automated smoke test against /health endpoint"},
        {"num": "5.11.8", "dir": "5.11.8-verify-end-to-end-pipeline", "title_vi": "Kiểm tra End-to-End Pipeline", "title_en": "Verify End-to-End Pipeline", "summary_vi": "Push baseline sạch và xác minh toàn bộ 7 stage hoàn thành SUCCEEDED", "summary_en": "Push clean baseline and verify end-to-end pipeline reaches SUCCEEDED"},
        {"num": "5.11.9", "dir": "5.11.9-commit-operation-rules", "title_vi": "Quy tắc vận hành khi có commit mới", "title_en": "Operational Rules on New Commits", "summary_vi": "Quy tắc tái sử dụng pipeline và xử lý lỗi an toàn khi commit mới", "summary_en": "Operational pipeline reuse rules and safe fault isolation on new commits"},
    ]

    write_section(p / "5.11.1-source-stage", "5.11.1", "Source Stage", "Source Stage", "`platform/pipeline.tf`",
        "Lấy source từ GitHub thông qua CodeConnections, output artifact là `SourceOutput`.",
        "Pulls source from GitHub via CodeConnections, producing `SourceOutput` artifact.",
        screenshot_vi=None, screenshot_en=None, weight=1)

    write_section(p / "5.11.2-validate-test-stage", "5.11.2", "Validate & Test Stage", "Validate & Test Stage", "`platform/pipeline.tf`",
        "Gọi CodeBuild `validate-security` với `RUN_MODE=validate`.",
        "Invokes CodeBuild `validate-security` with `RUN_MODE=validate`.",
        screenshot_vi=None, screenshot_en=None, weight=2)

    write_section(p / "5.11.3-security-scan-gate-stage", "5.11.3", "Security Scan & Security Gate Stage", "Security Scan & Security Gate Stage", "`platform/pipeline.tf`",
        "Gọi cùng CodeBuild project với `RUN_MODE=security`; scanner fail sẽ chặn pipeline.",
        "Invokes the same CodeBuild project with `RUN_MODE=security`; scanner failures block the pipeline.",
        screenshot_vi=None, screenshot_en=None, weight=3)

    write_section(p / "5.11.4-terraform-plan-stage", "5.11.4", "Terraform Plan Stage", "Terraform Plan Stage", "`platform/pipeline.tf`",
        "Tạo `PlanOutput` chứa `tfplan`, `plan.txt` và `.terraform.lock.hcl`.",
        "Generates `PlanOutput` holding `tfplan`, `plan.txt`, and `.terraform.lock.hcl`.",
        screenshot_vi=None, screenshot_en=None, weight=4)

    write_section(p / "5.11.5-manual-approval-stage", "5.11.5", "Manual Approval Stage", "Manual Approval Stage", "`platform/pipeline.tf`",
        "Yêu cầu reviewer đọc `plan.txt` và chọn **Approve** hoặc **Reject**.",
        "Requires human reviewer inspection of `plan.txt` before choosing **Approve** or **Reject**.",
        screenshot_vi=None, screenshot_en=None, weight=5)

    write_section(p / "5.11.6-terraform-apply-stage", "5.11.6", "Terraform Apply Stage", "Terraform Apply Stage", "`platform/pipeline.tf`",
        "Nhận `SourceOutput` + `PlanOutput`, dùng `RUN_MODE=apply` và đúng binary plan đã approve.",
        "Consumes `SourceOutput` + `PlanOutput`, executing `RUN_MODE=apply` with the exact approved binary plan.",
        screenshot_vi=None, screenshot_en=None, weight=6)

    write_section(p / "5.11.7-post-deploy-verification-stage", "5.11.7", "Post-Deploy Verification Stage", "Post-Deploy Verification Stage", "`platform/pipeline.tf`",
        "Dùng `RUN_MODE=smoke` để kiểm tra `/health` sau deployment.",
        "Runs `RUN_MODE=smoke` to verify the `/health` endpoint after deployment.",
        screenshot_vi=None, screenshot_en=None, weight=7)

    # 5.11.8 has screenshot
    write_section(p / "5.11.8-verify-end-to-end-pipeline", "5.11.8", "Kiểm tra End-to-End Pipeline", "Verify End-to-End Pipeline", "`platform/pipeline.tf`",
        """Push baseline sạch và xác minh toàn bộ stage chạy theo đúng thứ tự đến **SUCCEEDED**:

```text
Source → ValidateTest → SecurityScan → TerraformPlan → ManualApproval → TerraformApply → PostDeployVerification
```

---

> **[📝 Ảnh chụp đề xuất]**  
> CodePipeline hiển thị tất cả stage màu xanh sau một baseline deployment thành công.
""",
        """Push a clean baseline and verify all stages complete sequentially to **SUCCEEDED**:

```text
Source → ValidateTest → SecurityScan → TerraformPlan → ManualApproval → TerraformApply → PostDeployVerification
```

---

> **[📝 Recommended Screenshot]**  
> CodePipeline console showing all stages green following a successful baseline deployment.
""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=8)

    # 5.11.9 has bash
    write_section(p / "5.11.9-commit-operation-rules", "5.11.9", "Quy tắc vận hành khi có commit mới", "Operational Rules on New Commits", "`platform/pipeline.tf`",
        """Pipeline được tạo một lần ở layer platform. Mỗi commit mới vào branch `main` sẽ dùng lại pipeline hiện có: `Source` → `ValidateTest` → `SecurityScan` → `TerraformPlan` → `ManualApproval` → `TerraformApply` → `PostDeployVerification`. Nếu lỗi xảy ra trước `TerraformApply`, deployment mới bị block và hạ tầng đang chạy được giữ nguyên. Nếu lỗi xảy ra trong `TerraformApply`, có thể đã có thay đổi một phần và cần để Terraform reconcile ở execution tiếp theo.

### Workflow commit hằng ngày

```bash
cd ~/fcaj-aws-devsecops
git add -A
git status
git commit -m "feat: update application or workload"
git push

# Không cần terraform apply platform cho app/ hoặc workload/ thông thường.
# Chỉ re-apply platform nếu thay đổi platform/ hoặc iam-policy/.
```

> [!IMPORTANT]
> Tránh push/release nhiều execution liên tiếp trong lúc execution trước đang ở `TerraformApply` để giảm khả năng `TerraformPlan` mới đụng state lock.""",
        """The pipeline is created once in the platform layer. Every subsequent commit to `main` reuses the existing pipeline flow: `Source` → `ValidateTest` → `SecurityScan` → `TerraformPlan` → `ManualApproval` → `TerraformApply` → `PostDeployVerification`. If an error occurs prior to `TerraformApply`, the new deployment is blocked and live infrastructure remains untouched. If an error occurs during `TerraformApply`, partial changes may have occurred, requiring Terraform to reconcile state on the next execution.

### Daily Commit Workflow

```bash
cd ~/fcaj-aws-devsecops
git add -A
git status
git commit -m "feat: update application or workload"
git push

# No need to terraform apply platform for normal app/ or workload/ changes.
# Only re-apply platform when modifying platform/ or iam-policy/.
```

> [!IMPORTANT]
> Avoid triggering rapid consecutive executions while a prior execution is in `TerraformApply` to prevent subsequent `TerraformPlan` stages from encountering state locks.""",
        screenshot_vi=None,
        screenshot_en=None,
        weight=9)

    # Parent 5.11
    write_parent(
        p,
        "5.11",
        "Hoàn thiện AWS DevSecOps Pipeline",
        "Complete AWS DevSecOps Pipeline",
        "Chương này tổng hợp toàn bộ 7 stage của chuỗi cung ứng AWS CodePipeline thành một quy trình tự động hóa khép kín và các quy tắc vận hành commit hằng ngày.",
        "This chapter reviews the complete 7-stage AWS CodePipeline workflow and operational governance rules for ongoing commits.",
        sub_list,
        11
    )

def build_5_12():
    p = BASE_DIR / "5.12-DevSecOps-Scenarios"
    sub_list = [
        {"num": "5.12.1", "dir": "5.12.1-successful-deployment-scenario", "title_vi": "Kịch bản triển khai thành công", "title_en": "Successful Baseline Deployment Scenario", "summary_vi": "Triển khai toàn bộ pipeline thành công với baseline mã nguồn sạch", "summary_en": "Demonstrate clean baseline pipeline execution reaching SUCCEEDED"},
        {"num": "5.12.2", "dir": "5.12.2-public-ssh-blocked-checkov", "title_vi": "Kịch bản phát hiện Public SSH bằng Checkov", "title_en": "Public SSH Detection Scenario via Checkov", "summary_vi": "Mô phỏng mở cổng TCP/22 và chứng minh Checkov chặn trước Apply", "summary_en": "Simulate public SSH rule and prove Checkov halts pipeline before Apply"},
        {"num": "5.12.3", "dir": "5.12.3-secret-leak-blocked-gitleaks", "title_vi": "Kịch bản phát hiện Secret Leak bằng Gitleaks", "title_en": "Secret Leak Detection Scenario via Gitleaks", "summary_vi": "Mô phỏng commit fake credential và chứng minh Gitleaks chặn đứng", "summary_en": "Simulate fake credential commit and demonstrate Gitleaks halt"},
        {"num": "5.12.4", "dir": "5.12.4-vulnerable-dependency-trivy", "title_vi": "Kịch bản phát hiện Vulnerable Dependency bằng Trivy", "title_en": "Vulnerable Dependency Scenario via Trivy", "summary_vi": "Mô phỏng chèn package dính CVE nghiêm trọng và chứng minh Trivy chặn", "summary_en": "Inject vulnerable package CVE and demonstrate Trivy gate halt"},
        {"num": "5.12.5", "dir": "5.12.5-manual-approval-reject", "title_vi": "Kịch bản Manual Approval Reject", "title_en": "Manual Approval Rejection Scenario", "summary_vi": "Từ chối phê duyệt thay đổi hạ tầng và bảo đảm Apply không chạy", "summary_en": "Reject manual approval and verify Apply and Verification never run"},
        {"num": "5.12.6", "dir": "5.12.6-evaluate-security-gate-results", "title_vi": "Đánh giá kết quả Security Gate", "title_en": "Evaluate Security Gate Defense Results", "summary_vi": "Tổng kết khả năng phòng thủ tự động và bảo vệ hạ tầng của chuỗi CI/CD", "summary_en": "Summarize automated defense and infrastructure protection metrics"},
    ]

    # 5.12.1
    write_section(p / "5.12.1-successful-deployment-scenario", "5.12.1", "Kịch bản triển khai thành công", "Successful Baseline Deployment Scenario", "`demo/README.md`",
        """Push baseline repository. Kết quả mong đợi: tất cả stage chạy thành công. ManualApproval chỉ được Approve sau khi review `PlanOutput/plan.txt`.

```text
Source -> ValidateTest -> SecurityScan -> TerraformPlan -> ManualApproval -> TerraformApply -> PostDeployVerification -> SUCCEEDED
```""",
        """Push baseline repository. Expected outcome: all stages execute successfully. ManualApproval is approved only after reviewing `PlanOutput/plan.txt`.

```text
Source -> ValidateTest -> SecurityScan -> TerraformPlan -> ManualApproval -> TerraformApply -> PostDeployVerification -> SUCCEEDED
```""",
        screenshot_vi=None, screenshot_en=None, weight=1)

    # 5.12.2 has bash
    write_section(p / "5.12.2-public-ssh-blocked-checkov", "5.12.2", "Kịch bản phát hiện Public SSH bằng Checkov", "Public SSH Detection Scenario via Checkov", "`demo/scripts/enable-public-ssh.sh`, `demo/fixtures/public_ssh.tf.example`",
        """```bash
./demo/scripts/enable-public-ssh.sh
git add workload/demo_public_ssh.tf
git commit -m "demo: intentionally expose ssh"
git push
```

Fixture mở TCP/22 từ `0.0.0.0/0`. `SecurityScan` phải fail ở Checkov trước `TerraformPlan`/`Apply`. Sau demo, dùng `reset-demo.sh` để xóa file không an toàn:

```bash
./demo/scripts/reset-demo.sh
git add -A && git commit -m "demo: remove public ssh" && git push
```""",
        """```bash
./demo/scripts/enable-public-ssh.sh
git add workload/demo_public_ssh.tf
git commit -m "demo: intentionally expose ssh"
git push
```

The fixture opens TCP/22 to `0.0.0.0/0`. `SecurityScan` fails in Checkov prior to TerraformPlan/Apply. After the demo, run `reset-demo.sh` to remove the insecure rule:

```bash
./demo/scripts/reset-demo.sh
git add -A && git commit -m "demo: remove public ssh" && git push
```""",
        screenshot_vi=None, screenshot_en=None, weight=2)

    # 5.12.3 has bash
    write_section(p / "5.12.3-secret-leak-blocked-gitleaks", "5.12.3", "Kịch bản phát hiện Secret Leak bằng Gitleaks", "Secret Leak Detection Scenario via Gitleaks", "`demo/scripts/enable-secret-leak.sh`, `demo/fixtures/secret_leak.py.example`, `.gitleaks.toml`",
        """```bash
./demo/scripts/enable-secret-leak.sh
git add app/demo_secret_leak.py
git commit -m "demo: intentionally leak fake credential"
git push
```

Baseline fixture được allowlist trong thư mục `demo`. Khi copy sang `app/`, Gitleaks phải phát hiện fake AWS credential và làm `SecurityScan` thất bại. Không dùng credential thật.""",
        """```bash
./demo/scripts/enable-secret-leak.sh
git add app/demo_secret_leak.py
git commit -m "demo: intentionally leak fake credential"
git push
```

Baseline fixtures are allowlisted under `demo`. When copied into `app/`, Gitleaks detects the fake AWS credential and fails `SecurityScan`. Never use real credentials.""",
        screenshot_vi=None, screenshot_en=None, weight=3)

    # 5.12.4 has bash
    write_section(p / "5.12.4-vulnerable-dependency-trivy", "5.12.4", "Kịch bản phát hiện Vulnerable Dependency bằng Trivy", "Vulnerable Dependency Scenario via Trivy", "`demo/scripts/enable-vulnerable-dependency.sh`, `demo/fixtures/requirements-vulnerable.txt`",
        """```bash
./demo/scripts/enable-vulnerable-dependency.sh
git add app/requirements.txt
git commit -m "demo: intentionally add vulnerable dependency"
git push
```

Trivy quét `HIGH/CRITICAL` vulnerability. Vì vulnerability database thay đổi theo thời gian, fixture có thể cần được cập nhật package version trước live workshop nếu advisory cũ không còn kích hoạt.""",
        """```bash
./demo/scripts/enable-vulnerable-dependency.sh
git add app/requirements.txt
git commit -m "demo: intentionally add vulnerable dependency"
git push
```

Trivy scans for `HIGH/CRITICAL` vulnerabilities. Because vulnerability databases evolve, the fixture package version may need refreshing before live workshops if older advisories retire.""",
        screenshot_vi=None, screenshot_en=None, weight=4)

    # 5.12.5
    write_section(p / "5.12.5-manual-approval-reject", "5.12.5", "Kịch bản Manual Approval Reject", "Manual Approval Rejection Scenario", "AWS CodePipeline Console",
        """Push một thay đổi an toàn, chờ pipeline tới `ManualApproval`, review plan rồi chọn **Reject**. 

**Kết quả cần xác nhận**: `TerraformApply` và `PostDeployVerification` không được chạy.""",
        """Push a safe change, wait until `ManualApproval`, inspect the plan, and click **Reject**.

**Outcome**: Confirms that `TerraformApply` and `PostDeployVerification` are never invoked.""",
        screenshot_vi=None, screenshot_en=None, weight=5)

    # 5.12.6 has composite screenshot
    write_section(p / "5.12.6-evaluate-security-gate-results", "5.12.6", "Đánh giá kết quả Security Gate", "Evaluate Security Gate Defense Results", "FCAJ DevSecOps Pipeline Evaluation",
        """Security Gate đạt mục tiêu khi các lỗi secret leak, public SSH hoặc vulnerable dependency dừng pipeline trước khi Terraform Apply thay đổi hạ tầng. Kịch bản baseline sạch phải vẫn có thể đi qua gate và deploy thành công.

---

> **[📝 Ảnh chụp đề xuất]**  
> Ảnh CodePipeline/CodeBuild cho từng kịch bản: baseline xanh, Checkov fail, Gitleaks fail, Trivy fail và ManualApproval Reject.
""",
        """The Security Gate achieves its objective when secret leaks, public SSH, or vulnerable dependencies halt the pipeline before Terraform Apply mutates infrastructure. The clean baseline scenario must pass through the gate and deploy successfully.

---

> **[📝 Recommended Screenshot]**  
> Composite screenshot showing CodePipeline/CodeBuild for each scenario: clean baseline, Checkov fail, Gitleaks fail, Trivy fail, and ManualApproval Reject.
""",
        screenshot_vi=None, screenshot_en=None, weight=6)

    # Parent 5.12
    write_parent(
        p,
        "5.12",
        "Kiểm thử các kịch bản DevSecOps",
        "DevSecOps Demo Scenarios",
        "Chương này hướng dẫn thực hành các kịch bản kiểm thử bảo mật thực tế: baseline thành công, phát hiện Public SSH, phát hiện rò rỉ secret, chặn CVE nguy hiểm và từ chối phê duyệt.",
        "This chapter guides through practical security verification scenarios: clean baseline, public SSH detection, secret leak detection, vulnerable dependency blocking, and manual approval rejection.",
        sub_list,
        12
    )

def build_5_13():
    p = BASE_DIR / "5.13-Results-Cleanup"
    sub_list = [
        {"num": "5.13.1", "dir": "5.13.1-verify-entire-pipeline", "title_vi": "Kiểm tra toàn bộ Pipeline", "title_en": "Verify Entire Pipeline", "summary_vi": "Xác nhận thứ tự stage, luồng artifact và độ hoàn thiện chuỗi CI/CD", "summary_en": "Confirm stage sequencing, artifact flow, and CI/CD completeness"},
        {"num": "5.13.2", "dir": "5.13.2-verify-deployed-aws-resources", "title_vi": "Kiểm tra tài nguyên AWS đã triển khai", "title_en": "Verify Deployed AWS Resources", "summary_vi": "Kiểm tra VPC, Internet Gateway, Subnet, Security Group và EC2", "summary_en": "Verify VPC, IGW, Subnet, Route Table, SG, and EC2 resources"},
        {"num": "5.13.3", "dir": "5.13.3-verify-security-scan-results", "title_vi": "Kiểm tra Security Scan Results", "title_en": "Verify Security Scan Results", "summary_vi": "Đối chiếu kết quả quét Gitleaks, Bandit, Trivy và Checkov", "summary_en": "Cross-reference logs across Gitleaks, Bandit, Trivy, and Checkov"},
        {"num": "5.13.4", "dir": "5.13.4-verify-logs-audit-notification", "title_vi": "Kiểm tra Logs, Audit và Notification", "title_en": "Verify Logs, Audit, and Notification", "summary_vi": "Xác minh CloudWatch Logs, CloudTrail trail, EventBridge và Budgets", "summary_en": "Audit CloudWatch Logs, CloudTrail, EventBridge, and AWS Budgets"},
        {"num": "5.13.5", "dir": "5.13.5-evaluate-workshop-acceptance", "title_vi": "Đánh giá kết quả Workshop", "title_en": "Evaluate Workshop Acceptance Criteria", "summary_vi": "Tổng kết dự án đáp ứng toàn diện các tiêu chí nghiệm thu DevSecOps", "summary_en": "Conclude workshop evaluation against DevSecOps acceptance criteria"},
        {"num": "5.13.6", "dir": "5.13.6-terraform-destroy-workload", "title_vi": "Terraform Destroy Target Environment", "title_en": "Terraform Destroy Target Workload Environment", "summary_vi": "Hủy toàn bộ tài nguyên theo đúng thứ tự Workload -> Platform -> Bootstrap", "summary_en": "Tear down resources following strict dependency: Workload -> Platform -> Bootstrap"},
        {"num": "5.13.7", "dir": "5.13.7-destroy-platform-codepipeline", "title_vi": "Xóa CodePipeline, CodeBuild và CodeConnections", "title_en": "Destroy Platform CodePipeline & Build Resources", "summary_vi": "Thực hiện terraform destroy cho toàn bộ layer platform CI/CD", "summary_en": "Execute terraform destroy across the platform CI/CD layer"},
        {"num": "5.13.8", "dir": "5.13.8-destroy-s3-parameter-store", "title_vi": "Xóa S3, Parameter Store và các tài nguyên hỗ trợ", "title_en": "Clean S3 Buckets & Supporting Parameters", "summary_vi": "Xóa sạch object version trong S3 bucket trước khi destroy bootstrap", "summary_en": "Empty versioned S3 buckets and clean residual resources"},
        {"num": "5.13.9", "dir": "5.13.9-verify-residual-resources-costs", "title_vi": "Kiểm tra tài nguyên còn lại và chi phí", "title_en": "Verify Residual Resources and Zero Lingering Cost", "summary_vi": "Xác minh 0 tài nguyên tồn đọng và không phát sinh chi phí ngoài ý muốn", "summary_en": "Verify zero active resources and zero unexpected ongoing costs"},
    ]

    write_section(p / "5.13.1-verify-entire-pipeline", "5.13.1", "Kiểm tra toàn bộ Pipeline", "Verify Entire Pipeline", "CodePipeline",
        "Xác nhận stage order, artifact flow, ManualApproval và PostDeployVerification đúng với thiết kế.",
        "Confirms stage order, artifact flow, ManualApproval, and PostDeployVerification match design specifications.",
        screenshot_vi=None, screenshot_en=None, weight=1)

    write_section(p / "5.13.2-verify-deployed-aws-resources", "5.13.2", "Kiểm tra tài nguyên AWS đã triển khai", "Verify Deployed AWS Resources", "AWS Management Console",
        "Kiểm tra VPC, Internet Gateway, Subnet, Route Table, Security Group, EC2 và endpoint ứng dụng.",
        "Verifies VPC, Internet Gateway, Subnet, Route Table, Security Group, EC2 instance, and application endpoint.",
        screenshot_vi=None, screenshot_en=None, weight=2)

    write_section(p / "5.13.3-verify-security-scan-results", "5.13.3", "Kiểm tra Security Scan Results", "Verify Security Scan Results", "CodeBuild Logs",
        "Đối chiếu log Gitleaks, Bandit, Trivy và Checkov ở cả baseline và demo fail scenario.",
        "Cross-references Gitleaks, Bandit, Trivy, and Checkov logs between clean baseline and demo failure scenarios.",
        screenshot_vi=None, screenshot_en=None, weight=3)

    write_section(p / "5.13.4-verify-logs-audit-notification", "5.13.4", "Kiểm tra Logs, Audit và Notification", "Verify Logs, Audit, and Notification", "CloudWatch, EventBridge, SNS, CloudTrail, Budgets",
        "Kiểm tra CloudWatch logs, EventBridge event, SNS email, CloudTrail và Budget alert configuration.",
        "Verifies CloudWatch logs, EventBridge events, SNS notifications, CloudTrail audit records, and Budget alerts.",
        screenshot_vi=None, screenshot_en=None, weight=4)

    write_section(p / "5.13.5-evaluate-workshop-acceptance", "5.13.5", "Đánh giá kết quả Workshop", "Evaluate Workshop Acceptance Criteria", "Workshop Acceptance Criteria",
        "Kết luận project chứng minh được thay đổi không an toàn bị chặn trước Apply, trong khi baseline sạch có thể deploy và xác minh sau deploy.",
        "Concludes the project proves that unsafe changes are blocked before Apply, while clean baselines deploy and verify smoothly.",
        screenshot_vi=None, screenshot_en=None, weight=5)

    # 5.13.6 has bash
    write_section(p / "5.13.6-terraform-destroy-workload", "5.13.6", "Terraform Destroy Target Environment", "Terraform Destroy Target Workload Environment", "`README.md`, `scripts/init-workload-local.sh`",
        """### Cleanup theo đúng dependency

```bash
cd ~/fcaj-aws-devsecops
export AWS_REGION="ap-southeast-1"
export TF_STATE_BUCKET="<BOOTSTRAP_STATE_BUCKET>"

# 1) Workload
bash scripts/init-workload-local.sh
terraform -chdir=workload plan -destroy
terraform -chdir=workload destroy

# 2) Platform
cd platform
terraform destroy

# 3) Bootstrap cuối cùng (chỉ khi đã empty versioned buckets nếu cần)
cd ../bootstrap
terraform destroy
```

> [!IMPORTANT]
> **Thứ tự cleanup**: Workload phải được destroy trước Platform; Bootstrap/state bucket được giữ tới cuối để backend vẫn tồn tại trong lúc destroy workload và platform.""",
        """### Cleanup Following Exact Dependency Order

```bash
cd ~/fcaj-aws-devsecops
export AWS_REGION="ap-southeast-1"
export TF_STATE_BUCKET="<BOOTSTRAP_STATE_BUCKET>"

# 1) Workload
bash scripts/init-workload-local.sh
terraform -chdir=workload plan -destroy
terraform -chdir=workload destroy

# 2) Platform
cd platform
terraform destroy

# 3) Bootstrap last (only after emptying versioned buckets if required)
cd ../bootstrap
terraform destroy
```

> [!IMPORTANT]
> **Cleanup Sequence**: Workload must be destroyed before Platform; Bootstrap/state bucket is retained until the end so the remote backend remains available while destroying workload and platform.""",
        screenshot_vi=None, screenshot_en=None, weight=6)

    # 5.13.7
    write_section(p / "5.13.7-destroy-platform-codepipeline", "5.13.7", "Xóa CodePipeline, CodeBuild và CodeConnections", "Destroy Platform CodePipeline & Build Resources", "`platform/`",
        """Thực hiện `terraform destroy` trong thư mục platform. Các resource CodePipeline, CodeBuild, IAM role, CodeConnections, SNS, EventBridge, SSM, CloudTrail và Budget thuộc platform sẽ được Terraform quản lý và xóa theo dependency graph:

```bash
cd platform
terraform destroy
```""",
        """Execute `terraform destroy` inside the platform directory. Platform resources including CodePipeline, CodeBuild, IAM roles, CodeConnections, SNS, EventBridge, SSM, CloudTrail, and Budgets are removed along the dependency graph:

```bash
cd platform
terraform destroy
```""",
        screenshot_vi=None, screenshot_en=None, weight=7)

    # 5.13.8
    write_section(p / "5.13.8-destroy-s3-parameter-store", "5.13.8", "Xóa S3, Parameter Store và các tài nguyên hỗ trợ", "Clean S3 Buckets & Supporting Parameters", "`bootstrap/`",
        """Sau platform destroy, nếu S3 versioned bucket còn object version/delete marker thì cần empty bucket trước khi bootstrap destroy. Parameter Store demo thuộc platform và được xóa cùng platform state.""",
        """Following platform destroy, empty versioned S3 buckets of remaining object versions/delete markers before destroying bootstrap. The demo Parameter Store belongs to platform and was destroyed with its state.""",
        screenshot_vi=None, screenshot_en=None, weight=8)

    # 5.13.9 has screenshot
    write_section(p / "5.13.9-verify-residual-resources-costs", "5.13.9", "Kiểm tra tài nguyên còn lại và chi phí", "Verify Residual Resources and Zero Lingering Cost", "AWS Console & Billing",
        """Cuối cùng chạy `terraform destroy` trong bootstrap để xóa state/artifact buckets sau khi đã empty:

```bash
cd ../bootstrap
terraform destroy
```

Kiểm tra Resource Explorer/Console và Billing/Budgets để chắc chắn Workshop không còn tài nguyên phát sinh chi phí ngoài dự kiến.

---

> **[📝 Ảnh chụp đề xuất]**  
> Terraform destroy hoàn tất và kiểm tra Console không còn EC2/VPC/CodePipeline/CodeBuild của project.
""",
        """Finally execute `terraform destroy` in bootstrap to remove state and artifact buckets after they have been emptied:

```bash
cd ../bootstrap
terraform destroy
```

Inspect Resource Explorer/Console and Billing/Budgets to guarantee zero lingering resources or unexpected costs.

---

> **[📝 Recommended Screenshot]**  
> Terraform destroy completed and AWS Console confirms zero active EC2/VPC/CodePipeline/CodeBuild resources.
""",
        screenshot_vi=None, screenshot_en=None, weight=9)

    # Parent 5.13
    write_parent(
        p,
        "5.13",
        "Kiểm tra kết quả & dọn dẹp tài nguyên",
        "Workshop Evaluation & Resource Teardown",
        "Chương này hướng dẫn nghiệm thu toàn bộ các tiêu chí thành công của Workshop và quy trình dọn dẹp tài nguyên tuần tự (Workload -> Platform -> S3 -> Bootstrap) để bảo đảm không phát sinh chi phí sau thực hành.",
        "This chapter guides through workshop acceptance criteria verification and strict sequential resource teardown (Workload -> Platform -> S3 -> Bootstrap) to prevent lingering cloud costs.",
        sub_list,
        13
    )

if __name__ == "__main__":
    build_5_9()
    build_5_10()
    build_5_11()
    build_5_12()
    build_5_13()
    print("Modules 5.9 - 5.13 built successfully!")
