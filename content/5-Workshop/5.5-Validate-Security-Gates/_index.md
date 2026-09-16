---
title: "Build Validate, Test & Shift-Left Security"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.5. </b> "
---

# 5.5. Build Validate, Test & Shift-Left Security

This chapter guides you through establishing automated Shift-Left security guardrails using AWS CodeBuild: code formatting and linting, unit testing, and integrating 4 specialized security scanners: **Gitleaks** (Secret Detection), **Bandit** (SAST), **Trivy** (SCA/CVE), and **Checkov** (IaC).

---

### AWS CodeBuild Validate & Test Project Configuration

The `validate-security` CodeBuild project runs on the standard `standard:7.0` container image with compute size `BUILD_GENERAL1_SMALL`, consumes artifacts from CodePipeline, and assumes the `ScanBuildRole`. To optimize resource efficiency and cost, the same CodeBuild project is dynamically driven by the `RUN_MODE` environment variable across both validation and security scanning phases.

---

![AWS CodeBuild Console - CodeBuild Projects list supporting Validate and Security Gates](/images/5-Workshop/5.5-Validate-Security-Gates/image.png)

*AWS CodeBuild Console - CodeBuild Projects list supporting Validate and Security Gates*

---

### Terraform Format & Syntax Validation

Under `RUN_MODE=validate`, the pipeline validates formatting, syntax integrity, and baseline application logic:

```bash
RUN_MODE=validate
terraform fmt -check -recursive bootstrap platform workload
terraform -chdir="${WORKLOAD_DIR}" init -backend=false -input=false
terraform -chdir="${WORKLOAD_DIR}" validate
python -m compileall -q app
pytest -q app/tests
```

The `ValidateTest` stage requires all Terraform formatting, Python compilation, and Pytest test suites to succeed without error before advancing to security scans.

#### Run ValidateTest Locally Before Push

```bash
cd ~/fcaj-aws-devsecops
terraform fmt -check -recursive bootstrap platform workload
terraform -chdir=workload init -backend=false -input=false
terraform -chdir=workload validate
python3 -m compileall -q app
python3 -m pip install --user -r app/requirements.txt pytest
python3 -m pytest -q app/tests
```

> [!NOTE]
> If Pytest reports that `test_client` cannot be found, ensure `app/tests/test_app.py` correctly imports the Flask instance: `from app.app import app`.

---

### Multi-Layer Shift-Left Security Scanners

Under `RUN_MODE=security`, CodeBuild sequentially runs four independent verification scanners:

1. **Secret Scanning with Gitleaks**:
   Gitleaks inspects the repository directory against `.gitleaks.toml` rules to catch exposed secrets, tokens, or AWS credentials:
   ```bash
   gitleaks dir . --config .gitleaks.toml --redact --no-banner
   ```

2. **Static Application Security Testing with Bandit (SAST)**:
   Bandit analyzes application Python source code in the `app/` directory, focusing strictly on high-severity and high-confidence vulnerabilities:
   ```bash
   bandit -r app -lll -iii
   ```

3. **Dependency CVE Scanning with Trivy (SCA)**:
   Trivy matches dependencies in `app/requirements.txt` against global vulnerability feeds and fails the build upon finding `HIGH` or `CRITICAL` severity CVEs:
   ```bash
   trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
   ```

4. **Infrastructure as Code Scanning with Checkov**:
   Checkov analyzes workload Terraform templates to detect security misconfigurations:
   ```bash
   checkov -d "${WORKLOAD_DIR}" --framework terraform --compact
   ```
   Documented baseline exceptions are recognized for VPC Flow Logs (`CKV2_AWS_11`), Public Subnets (`CKV_AWS_130`), HTTP port 80 (`CKV_AWS_260`), and Public IPs (`CKV_AWS_88`).

#### Run Security Scans Manually

```bash
cd ~/fcaj-aws-devsecops
gitleaks dir . --config .gitleaks.toml --redact --no-banner
bandit -r app -lll -iii
trivy fs --scanners vuln --severity HIGH,CRITICAL --exit-code 1 --ignore-unfixed app/
checkov -d workload --framework terraform --compact
```

---

### Automated Security Gate Enforcement

Security Gates are strictly enforced in the delivery pipeline: `SecurityScan` must complete with zero exit codes before `TerraformPlan` is allowed to execute. Buildspecs enforce `set -euo pipefail`, ensuring that any scanner detecting a violation halts the delivery pipeline immediately.
