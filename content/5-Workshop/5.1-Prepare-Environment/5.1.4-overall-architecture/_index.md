---
title: "Workshop Overall Architecture"
date: 2026-08-25
weight: 4
chapter: false
pre: " <b> 5.1.4. </b> "
---

# 5.1.4. Workshop Overall Architecture

The overall architecture strictly decouples the **execution flow** from **support services**. Developers push code to GitHub; source flows via CodeConnections into CodePipeline. The pipeline executes validate/test, security scan, Terraform plan, manual approval, apply, and post-deploy smoke test. Supporting AWS services S3, SSM, CloudWatch, EventBridge, SNS, CloudTrail, and Budgets manage state, artifacts, secrets, logging, notifications, audits, and cost governance.

![FCAJ AWS DevSecOps Recommended Overall Architecture](/images/2-Proposal/FCAJ_AWS_DevSecOps_Recommended_Architecture_v6.png)
*Overall FCAJ AWS DevSecOps Recommended Architecture - v6*

