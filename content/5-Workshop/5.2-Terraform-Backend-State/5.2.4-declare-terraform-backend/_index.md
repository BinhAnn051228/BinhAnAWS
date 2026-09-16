---
title: "Declare Terraform Backend"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.2.4. </b> "
---

# 5.2.4. Declare Terraform Backend

Both platform and workload layers declare empty S3 backend blocks in source code, dynamically receiving bucket, key, and Region during initialization. Platform uses key `platform/terraform.tfstate`; workload uses key `workload/terraform.tfstate`.

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

