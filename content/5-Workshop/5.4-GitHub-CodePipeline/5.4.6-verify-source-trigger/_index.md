---
title: "Verify Source Trigger"
date: 2026-08-25
weight: 6
chapter: false
pre: " <b> 5.4.6. </b> "
---

# 5.4.6. Verify Source Trigger

The Source action utilizes provider `CodeStarSourceConnection` with `DetectChanges=true`. Once the connection reaches `AVAILABLE` status, pushing commits to the `main` branch automatically triggers a new pipeline execution.

### Trigger / Retrigger Pipeline

```bash
cd ~/fcaj-aws-devsecops
git status
git add -A
git commit -m "workshop: trigger pipeline"
git push

# If retriggering without source modifications
git commit --allow-empty -m "chore: retrigger pipeline"
git push
```

> [!NOTE]
> Executions that `FAILED` prior to connection authorization will not automatically restart. After the connection turns `AVAILABLE`, push a new commit or click **Release change** in the console to initiate a run.

