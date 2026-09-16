---
title: "Giới thiệu luồng DevSecOps triển khai"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.1.5. </b> "
---

# 5.1.5. Giới thiệu luồng DevSecOps triển khai

### Luồng pipeline

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

### Nguyên tắc bảo vệ trọng yếu

- **Security Gate bắt buộc**: `SecurityScan` phải thành công trước khi `TerraformPlan` được chạy.
- **Kế hoạch bất biến (Immutable Plan)**: `TerraformApply` chỉ sử dụng binary plan đã được tạo trước đó và đã đi qua `ManualApproval`.
- **Xác minh thực tế**: Sau Apply, smoke test xác minh endpoint `/health` trước khi pipeline được xem là thành công.

---

![Sơ đồ quy trình thực thi AWS DevSecOps CI/CD Delivery Workflow](/images/5-Workshop/5.1-Prepare-Environment/5.1.5-devsecops-workflow/workflow.png)

*Sơ đồ quy trình thực thi AWS DevSecOps CI/CD Delivery Workflow*

