---
title: "Infrastructure Planning & Manual Approval"
date: 2026-08-25
weight: 6
chapter: false
pre: " <b> 5.6. </b> "
---

# 5.6. Infrastructure Planning & Manual Approval

This chapter covers configuring the AWS CodeBuild project for **Terraform Plan**, persisting plan artifacts, and setting up a **Manual Approval** gate to govern infrastructure modifications before production changes take effect.

---

### CodeBuild Terraform Plan & Runtime Variables

The `TerraformPlan` stage operates inside a dedicated CodeBuild project running under `TerraformPlanRole`. The build consumes `cicd/buildspec-plan.yml` and receives runtime parameters managed by the platform layer:

```bash
# Inspect runtime parameters supplied to CodeBuild Plan
echo "TF_STATE_BUCKET   : ${TF_STATE_BUCKET}"
echo "WORKLOAD_ROLE_ARN : ${WORKLOAD_ROLE_ARN}"
echo "WORKLOAD_DIR      : ${WORKLOAD_DIR}"
```

### Executing Terraform Init & Generating Plan Artifacts

1. **Initializing the Remote Backend**:
   CodeBuild initializes the remote S3 state backend created during the bootstrap phase:
   ```bash
   terraform -chdir="${WORKLOAD_DIR}" init      -backend-config="bucket=${TF_STATE_BUCKET}"      -backend-config="key=workload/terraform.tfstate"      -backend-config="region=${AWS_REGION}"
   ```

2. **Generating the Execution Plan**:
   `terraform plan` outputs a deterministic binary `tfplan` and generates a human-readable text summary `plan.txt`:
   ```bash
   terraform -chdir="${WORKLOAD_DIR}" plan -out=tfplan -input=false
   terraform -chdir="${WORKLOAD_DIR}" show -no-color tfplan > plan.txt
   ```

### Packaging Artifacts & Enforcing Manual Approval

- **Artifact Preservation**: The binary `tfplan`, summary `plan.txt`, and `.terraform.lock.hcl` are packaged into the `PlanOutput` artifact and stored in S3.
- **Manual Approval Gate**: The pipeline halts upon plan completion. Reviewers inspect `plan.txt` directly to review planned additions, modifications, or destructions.
- **Review Decision**:
  - Selecting **Approve** authorizes the pipeline to proceed to `TerraformApply`.
  - Selecting **Reject** terminates the execution, protecting live infrastructure from unintended alterations.

---

![Infrastructure review and approval dialog at Manual Approval stage in AWS CodePipeline](/images/5-Workshop/5.6-Terraform-Plan-Approval/manual-approval.png)

*Infrastructure review and approval dialog at Manual Approval stage in AWS CodePipeline*
