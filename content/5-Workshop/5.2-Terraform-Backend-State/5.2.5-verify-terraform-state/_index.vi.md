---
title: "Kiểm tra Terraform State"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.2.5. </b> "
---

# 5.2.5. Kiểm tra Terraform State

Sau khi init/apply, kiểm tra state bằng Terraform CLI và trên S3 Console. Workload và platform phải dùng hai key riêng trong cùng state bucket.

### Kiểm tra State và Lock

```bash
terraform -chdir=platform state list
aws s3 ls "s3://${TF_STATE_BUCKET}/platform/"
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/"

# Kiểm tra lock file khi nghi ngờ có execution chồng nhau
aws s3 ls "s3://${TF_STATE_BUCKET}/workload/" | grep tflock || true
```

> [!NOTE]
> Nếu TerraformPlan báo `Error acquiring the state lock` trong lúc một TerraformApply khác đang chạy, hãy chờ execution Apply hoàn tất rồi retry. Tuyệt đối không xóa `.tflock` khi vẫn còn tiến trình Terraform hoặc CodeBuild đang thao tác với state.

