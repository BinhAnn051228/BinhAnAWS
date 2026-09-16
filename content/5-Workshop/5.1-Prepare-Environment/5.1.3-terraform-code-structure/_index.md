---
title: "Prepare Terraform & Source Code Structure"
date: 2026-08-25
weight: 3
chapter: false
pre: " <b> 5.1.3. </b> "
---

# 5.1.3. Prepare Terraform & Source Code Structure

The repository is architected into decoupled layers separating bootstrap, CI/CD platform, and workload infrastructure. Terraform CLI default in CodeBuild is `1.16.2`; Gitleaks `8.30.1` and Trivy `0.74.0` are configured via platform variables.

### Project Directory Layout

```text
fcaj-aws-devsecops/
├── app/              # Demo Flask app + unit tests
├── bootstrap/        # S3 Terraform State and S3 Pipeline Artifact buckets
├── platform/         # IAM, CodeBuild, CodeConnections, CodePipeline, SNS, EventBridge, CloudTrail, Budget, SSM
├── workload/         # VPC, Public Subnet, Internet Gateway, Route Table, Security Group and EC2 demo
├── cicd/             # 3 buildspecs: validate/security, plan, apply/smoke
├── iam-policy/       # IAM policy JSON templates
├── demo/             # Fixtures and scripts triggering intentional security failures
├── docs/             # Architecture documentation and diagrams
├── scripts/          # Helper scripts for initialization and config
├── .gitleaks.toml    # Secret scanning rule configuration
├── Makefile          # Convenience automation targets
└── README.md         # Project documentation
```

- `bootstrap/`: Provisions S3 Terraform State and S3 Pipeline Artifact buckets.
- `platform/`: Provisions IAM, CodeBuild, CodeConnections, CodePipeline, SNS, EventBridge, CloudTrail, Budget, and SSM Parameter Store.
- `workload/`: Provisions VPC, Public Subnet, Internet Gateway, Route Table, Security Group, and EC2 demo.
- `cicd/`: Exactly 3 buildspecs for validate/security, plan, apply/smoke.
- `demo/`: Fixtures and scripts triggering intentional security failure scenarios.

### Install / Verify Terraform on CloudShell

```bash
cd ~
TF_VERSION="1.16.2"
curl -fsSLo /tmp/terraform.zip   "https://releases.hashicorp.com/terraform/${TF_VERSION}/terraform_${TF_VERSION}_linux_amd64.zip"
unzip -o /tmp/terraform.zip -d "$HOME/bin"
export PATH="$HOME/bin:$PATH"
terraform version
```

> [!TIP]
> CloudShell sessions may be reset periodically. If a new environment is spun up, simply re-clone the repo and reinstall Terraform; AWS resources and remote state stored in S3 will persist safely.

