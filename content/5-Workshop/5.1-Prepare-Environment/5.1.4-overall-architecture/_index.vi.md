---
title: "Giới thiệu kiến trúc tổng thể Workshop"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.1.4. </b> "
---

# 5.1.4. Giới thiệu kiến trúc tổng thể Workshop

Kiến trúc tổng thể phân tách rõ **execution flow** và các **support services**. Developer push code lên GitHub; source đi qua CodeConnections vào CodePipeline. Pipeline thực hiện validate/test, security scan, Terraform plan, manual approval, apply và post-deploy smoke test. Các dịch vụ S3, SSM, CloudWatch, EventBridge, SNS, CloudTrail và Budgets hỗ trợ state, artifact, secret, logging, notification, audit và cost control.

![Kiến trúc tổng thể Workshop FCAJ AWS DevSecOps](/images/2-Proposal/FCAJ_AWS_DevSecOps_Recommended_Architecture_v6.png)
*Kiến trúc tổng thể Workshop FCAJ AWS DevSecOps - v6*

