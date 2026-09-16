---
title: "Tạo AWS CodeConnections"
date: 2026-08-25
weight: 2
chapter: false
pre: " <b> 5.4.2. </b> "
---

# 5.4.2. Tạo AWS CodeConnections

```hcl
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
aws codeconnections get-connection \
  --connection-arn "$CONNECTION_ARN" \
  --query 'Connection.ConnectionStatus' \
  --output text
```

> [!NOTE]
> `PENDING` ngay sau Terraform Apply là trạng thái bình thường. Hoàn tất Update pending connection / Authorize GitHub trên Console để trạng thái chuyển `AVAILABLE`.

---

![AWS CodeConnections - Kết nối GitHub ở trạng thái PENDING sau khi apply Terraform](/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.2-create-codeconnections/github%20pending.png)

*AWS CodeConnections - Kết nối GitHub ở trạng thái PENDING sau khi apply Terraform*

