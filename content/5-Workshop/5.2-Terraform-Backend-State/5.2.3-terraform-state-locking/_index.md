---
title: "Configure Terraform State Locking"
date: 2026-08-25
weight: 3
chapter: false
pre: " <b> 5.2.3. </b> "
---

# 5.2.3. Configure Terraform State Locking

The project uses S3 native backend lock files via `use_lockfile=true`. Platform, local workload init, Terraform Plan, and Terraform Apply all supply this setting during `terraform init -reconfigure`.

### Backend Locking

```bash
-backend-config="encrypt=true" \
-backend-config="use_lockfile=true"
```

**Objective**: Prevents two simultaneous Terraform processes from mutating the same remote state file concurrently.

