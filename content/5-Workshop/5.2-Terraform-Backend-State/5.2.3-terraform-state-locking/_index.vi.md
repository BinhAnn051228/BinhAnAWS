---
title: "Cấu hình Terraform State Locking"
date: 2026-08-25
weight: 3
chapter: false
pre: " <b> 5.2.3. </b> "
---

# 5.2.3. Cấu hình Terraform State Locking

Project sử dụng S3 backend lock file qua `use_lockfile=true`. Cả platform, workload local init, Terraform Plan và Terraform Apply đều truyền tùy chọn này khi chạy `terraform init -reconfigure`.

### Backend locking

```bash
-backend-config="encrypt=true" \
-backend-config="use_lockfile=true"
```

**Mục tiêu**: Tránh hai tiến trình Terraform đồng thời sửa cùng một state tại cùng thời điểm.

