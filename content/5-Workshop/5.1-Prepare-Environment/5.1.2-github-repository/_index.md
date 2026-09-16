---
title: "Prepare GitHub Repository"
date: 2026-08-25
weight: 2
chapter: false
pre: " <b> 5.1.2. </b> "
---

# 5.1.2. Prepare GitHub Repository

CodePipeline pulls source code from GitHub via AWS CodeConnections. The repository is tracked on the `main` branch; repository owner and name are passed to Terraform via `github_owner` and `github_repo`.

### Initialize Repository and Push Code

```bash
git init
git add .
git commit -m "initial FCAJ DevSecOps workshop"
git branch -M main
git remote add origin https://github.com/YOUR_USER/fcaj-aws-devsecops.git
git push -u origin main
```

### Clone Existing Repository

```bash
cd ~
git clone https://github.com/<GITHUB_USER>/fcaj-aws-devsecops.git
cd fcaj-aws-devsecops
git status
git branch --show-current
ls -la
ls cicd
```

> [!IMPORTANT]
> The repository root must directly expose `app/`, `bootstrap/`, `cicd/`, `platform/`, `workload/...`; avoid nested directory structures like `fcaj-aws-devsecops/fcaj-aws-devsecops` because CodeBuild resolves buildspec paths relative to the repository root.

**Expected Outcome**: The GitHub repository contains the full source tree with the `main` branch ready for CodeConnections webhook change detection.

---

![GitHub Repository - Project repository structure on branch main](/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/%E1%BA%A3nh%20ch%E1%BB%A5p%20git%20repo.png)

*GitHub Repository - Project repository structure on branch main*

![AWS CloudShell - Clone GitHub repository into CloudShell](/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/clone%20git%20repo%20v%E1%BB%81%20aws%20cloudshell.png)

*AWS CloudShell - Clone GitHub repository into CloudShell*

