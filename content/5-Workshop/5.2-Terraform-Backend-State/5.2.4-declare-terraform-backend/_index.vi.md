---
title: "Khai báo Terraform Backend"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.2.4. </b> "
---

# 5.2.4. Khai báo Terraform Backend

Hai layer platform và workload dùng backend S3 rỗng trong mã nguồn, sau đó nhận bucket, key và Region từ lệnh init. Platform dùng key `platform/terraform.tfstate`; workload dùng key `workload/terraform.tfstate`.

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

terraform -chdir=platform init -reconfigure \
  -backend-config="bucket=${TF_STATE_BUCKET}" \
  -backend-config="key=platform/terraform.tfstate" \
  -backend-config="region=${AWS_REGION}" \
  -backend-config="encrypt=true" \
  -backend-config="use_lockfile=true"
```

### scripts/init-workload-local.sh

```bash
#!/usr/bin/env bash
set -euo pipefail
: "${TF_STATE_BUCKET:?Set TF_STATE_BUCKET to bootstrap output}"
: "${AWS_REGION:=ap-southeast-1}"

terraform -chdir=workload init -reconfigure \
  -backend-config="bucket=${TF_STATE_BUCKET}" \
  -backend-config="key=workload/terraform.tfstate" \
  -backend-config="region=${AWS_REGION}" \
  -backend-config="encrypt=true" \
  -backend-config="use_lockfile=true"
```

