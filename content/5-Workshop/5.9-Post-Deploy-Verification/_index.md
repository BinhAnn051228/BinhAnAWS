---
title: "Post-Deploy Verification & Smoke Testing"
date: 2026-08-25
weight: 9
chapter: false
pre: " <b> 5.9. </b> "
---

# 5.9. Post-Deploy Verification & Smoke Testing

This chapter covers configuring the automated **PostDeployVerification (Smoke Test)** stage following `TerraformApply`, ensuring the EC2 host and demo web application are fully operational before finalizing the pipeline.

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
INSTANCE_ID=$(aws ec2 describe-instances   --filters "Name=tag:Name,Values=*fcaj*" "Name=instance-state-name,Values=running"   --query "Reservations[].Instances[].InstanceId"   --output text)

# Start secure terminal session via SSM
aws ssm start-session --target "$INSTANCE_ID"

# Inspect application status and bootstrap logs:
sudo systemctl status demo-app
cat /var/log/user-data.log
sudo journalctl -u demo-app -n 50 --no-pager
```

> [!NOTE]
> Smoke test failures indicate that while infrastructure provisioning succeeded, the application process encountered an initialization error. Checking `user-data.log` accelerates root-cause isolation.
