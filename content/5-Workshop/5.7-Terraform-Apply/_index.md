---
title: "Automated Infrastructure Deployment"
date: 2026-08-25
weight: 7
chapter: false
pre: " <b> 5.7. </b> "
---

# 5.7. Automated Infrastructure Deployment

This chapter covers configuring the AWS CodeBuild project for **Terraform Apply**, executing infrastructure changes securely under the least-privilege `TerraformDeployRole` strictly consuming the pre-approved plan binary.

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
   terraform -chdir="${WORKLOAD_DIR}" init      -backend-config="bucket=${TF_STATE_BUCKET}"      -backend-config="key=workload/terraform.tfstate"      -backend-config="region=${AWS_REGION}"
   terraform -chdir="${WORKLOAD_DIR}" apply -input=false -auto-approve tfplan
   ```
3. **Emitting Workload Outputs**:
   Upon apply completion, output values such as `ec2_public_ip` and `app_health_url` are emitted for subsequent verification.
