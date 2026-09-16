---
title: "IAM Configuration & Secrets Management"
date: 2026-08-25
weight: 3
chapter: false
pre: " <b> 5.3. </b> "
---

# 5.3. IAM Configuration & Secrets Management

This chapter covers establishing least-privilege IAM roles and managing secrets securely using AWS Systems Manager Parameter Store.

---

### Step-by-Step Implementation in Section 5.3:

- [**5.3.1. Create CodePipelineRole**](./5.3.1-create-codepipeline-role/): CI/CD orchestration role trusting codepipeline.amazonaws.com
- [**5.3.2. Create ScanBuildRole**](./5.3.2-create-scanbuild-role/): Execution role for validate and security scan with restricted read privileges
- [**5.3.3. Create TerraformPlanRole**](./5.3.3-create-terraform-plan-role/): Read-only planning role limited to EC2 Describe* and instance profile inspection
- [**5.3.4. Create TerraformDeployRole**](./5.3.4-create-terraform-deploy-role/): Deployment role authorized for EC2/VPC mutation and PassRole to EC2DemoRole
- [**5.3.5. Configure AWS Systems Manager Parameter Store**](./5.3.5-configure-ssm-parameter-store/): Generate random token stored as encrypted SecureString in SSM
- [**5.3.6. Secure Secrets Management via SecureString**](./5.3.6-securestring-secret-management/): Inject SSM secret into CodeBuild as PARAMETER_STORE without printing to logs
- [**5.3.7. Verify Principle of Least Privilege**](./5.3.7-verify-least-privilege-permissions/): Verify least-privilege role segregation between CI/CD roles and EC2 workload role

---
*Please select each sub-section from the left sidebar or the links above to view detailed instructions, source code, and verification commands.*
