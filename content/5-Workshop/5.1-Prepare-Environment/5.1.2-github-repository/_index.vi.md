---
title: "Chuẩn bị GitHub Repository"
date: 2026-08-25
weight: 2
chapter: false
pre: " <b> 5.1.2. </b> "
---

# 5.1.2. Chuẩn bị GitHub Repository

CodePipeline lấy source từ GitHub thông qua AWS CodeConnections. Repository mặc định được theo dõi ở branch `main`; tên owner và repository được truyền vào Terraform qua `github_owner` và `github_repo`.

### Khởi tạo repository

```bash
git init
git add .
git commit -m "initial FCAJ DevSecOps workshop"
git branch -M main
git remote add origin https://github.com/YOUR_USER/fcaj-aws-devsecops.git
git push -u origin main
```

### Clone repository đã có sẵn

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
> Repository root phải nhìn thấy trực tiếp `app/`, `bootstrap/`, `cicd/`, `platform/`, `workload/...`; không để lồng thêm một lớp `fcaj-aws-devsecops/fcaj-aws-devsecops` vì CodeBuild tìm buildspec theo đường dẫn từ repository root.

**Kết quả cần đạt**: GitHub repository chứa toàn bộ source tree và branch `main` sẵn sàng để CodeConnections theo dõi thay đổi.

---

![GitHub Repository - Cấu trúc repository fcaj-aws-devsecops trên branch main](/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/%E1%BA%A3nh%20ch%E1%BB%A5p%20git%20repo.png)

*GitHub Repository - Cấu trúc repository fcaj-aws-devsecops trên branch main*

![AWS CloudShell - Clone GitHub repository vào CloudShell](/images/5-Workshop/5.1-Prepare-Environment/5.1.2-github-repository/clone%20git%20repo%20v%E1%BB%81%20aws%20cloudshell.png)

*AWS CloudShell - Clone GitHub repository vào CloudShell*

