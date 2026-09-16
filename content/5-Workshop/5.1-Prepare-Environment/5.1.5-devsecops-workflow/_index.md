---
title: "DevSecOps Delivery Workflow"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.1.5. </b> "
---

# 5.1.5. DevSecOps Delivery Workflow

### Pipeline Workflow

```text
GitHub
  ↓
AWS CodeConnections
  ↓
Source
  ↓
ValidateTest
  ↓
SecurityScan
  ↓
TerraformPlan
  ↓
ManualApproval
  ↓
TerraformApply
  ↓
PostDeployVerification
  ↓
SUCCEEDED
```

### Critical Architecture Rules

- **Mandatory Security Gate**: `SecurityScan` must succeed before `TerraformPlan` is allowed to execute.
- **Immutable Plan Execution**: `TerraformApply` consumes only the pre-generated binary plan that has passed `ManualApproval`.
- **Post-Deploy Verification**: Following Apply, automated smoke testing verifies the `/health` endpoint before the pipeline is deemed successful.

---

![AWS DevSecOps CI/CD Delivery Workflow Diagram](/images/5-Workshop/5.1-Prepare-Environment/5.1.5-devsecops-workflow/workflow.png)

*AWS DevSecOps CI/CD Delivery Workflow Diagram*

