---
title: "Kiểm tra Source Trigger"
date: 2026-08-25
weight: 6
chapter: false
pre: " <b> 5.4.6. </b> "
---

# 5.4.6. Kiểm tra Source Trigger

Source action dùng provider `CodeStarSourceConnection`, `DetectChanges=true`. Sau khi connection `AVAILABLE`, một commit mới trên branch `main` phải tự tạo pipeline execution mới.

### Trigger/retrigger pipeline

```bash
cd ~/fcaj-aws-devsecops
git status
git add -A
git commit -m "workshop: trigger pipeline"
git push

# Nếu chỉ cần retrigger mà không đổi file
git commit --allow-empty -m "chore: retrigger pipeline"
git push
```

> [!NOTE]
> Execution đã `FAILED` trước lúc GitHub connection được verify sẽ không tự chạy lại. Sau khi connection `AVAILABLE`, push commit mới hoặc chọn **Release change** trên console để tạo execution mới.

