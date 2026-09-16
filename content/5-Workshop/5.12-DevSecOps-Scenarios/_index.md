---
title: "DevSecOps Demonstration Scenarios"
date: 2026-08-25
weight: 12
chapter: false
pre: " <b> 5.12. </b> "
---

# 5.12. DevSecOps Demonstration Scenarios

This chapter demonstrates the real-world efficacy of **Security Gates** across five practical scenarios: clean baseline deployment, automated blocking of open SSH ingress, credential leakage detection, vulnerable dependency discovery, and manual approval rejection.

---

### Scenario 1: Clean Baseline Deployment (Success)

- **Objective**: Validate the end-to-end pipeline operates reliably when code and infrastructure definitions adhere to security best practices.
- **Result**: All 7 stages from Source to PostDeployVerification transition to `SUCCEEDED` (green). The demo web app is deployed and returns HTTP `200 OK`.

---

### Scenario 2: Checkov Blocks Dangerous Open SSH Ingress

- **Simulation**: Introducing a security group rule opening port `22` (SSH) to `0.0.0.0/0` from `demo/fixtures/public_ssh.tf.example`.
- **Execution**:
  ```bash
  cp demo/fixtures/public_ssh.tf.example workload/public_ssh.tf
  git add workload/public_ssh.tf && git commit -m "test: simulate public ssh vulnerability" && git push
  ```
- **Result**: Checkov identifies violation `CKV_AWS_24`, exits with a failure code, and **halts the pipeline at SecurityScan**, preventing Terraform Plan from running.

---

### Scenario 3: Gitleaks Blocks Leaked Secrets & Credentials

- **Simulation**: Adding code containing a simulated AWS Access Key into `app/leak.py`.
- **Execution**:
  ```bash
  echo 'AWS_SECRET_KEY = "AKIAIOSFODNN7EXAMPLEEXAMPLE"' > app/leak.py
  git add app/leak.py && git commit -m "test: simulate credential leak" && git push
  ```
- **Result**: Gitleaks matches the AWS credential pattern, redacts output in build logs, and **fails the build immediately**.

---

### Scenario 4: Trivy Blocks Vulnerable Third-Party Dependencies

- **Simulation**: Adding an outdated dependency containing `HIGH/CRITICAL` CVEs into `app/requirements.txt`.
- **Execution**:
  ```bash
  cat demo/fixtures/requirements-vulnerable.txt >> app/requirements.txt
  git add app/requirements.txt && git commit -m "test: simulate vulnerable dependency" && git push
  ```
- **Result**: Trivy identifies qualifying CVEs and exits with code `1`, halting execution before deployment.

---

### Scenario 5: Rejecting Infrastructure Changes at Manual Approval

- **Simulation**: The pipeline completes scanning and enters approval. The reviewer inspects `plan.txt` and discovers unauthorized changes.
- **Action**: The reviewer clicks **Reject** in the AWS CodePipeline console providing rationale.
- **Result**: Execution terminates; `TerraformApply` is never invoked, protecting live environments from unapproved drift.

---

### Summary of Security Gate Efficacy

Through real-world test scenarios, the DevSecOps delivery pipeline proves its ability to identify and block common industry vulnerabilities early in the software lifecycle (Shift-Left): leaked secrets, vulnerable dependencies, and infrastructure misconfigurations.
