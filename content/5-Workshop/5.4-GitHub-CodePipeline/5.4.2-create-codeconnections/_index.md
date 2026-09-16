---
title: "Create AWS CodeConnections"
date: 2026-08-25
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---

# 5.4.2. Create AWS CodeConnections

```hcl
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
aws codeconnections get-connection \
  --connection-arn "$CONNECTION_ARN" \
  --query 'Connection.ConnectionStatus' \
  --output text
```

> [!NOTE]
> `PENDING` status immediately following Terraform Apply is expected behavior. Complete Update pending connection / Authorize GitHub in the AWS Console to transition to `AVAILABLE`.

---

![AWS CodeConnections - GitHub connection in PENDING status following Terraform apply](/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.2-create-codeconnections/github%20pending.png)

*AWS CodeConnections - GitHub connection in PENDING status following Terraform apply*

