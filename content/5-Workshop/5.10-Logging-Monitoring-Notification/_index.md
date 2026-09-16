---
title: "Logging, Monitoring & Notifications"
date: 2026-08-25
weight: 10
chapter: false
pre: " <b> 5.10. </b> "
---

# 5.10. Logging, Monitoring & Notifications

This chapter covers establishing full-stack observability for the DevSecOps pipeline, integrating **Amazon CloudWatch**, **Amazon EventBridge**, **Amazon SNS**, **AWS CloudTrail**, and **AWS Budgets** for centralized logging, event notifications, and cost governance.

---

### Centralized Logging & Pipeline Progress Monitoring

- **Amazon CloudWatch Logs**: Automatically collects and persists build output logs across all CodeBuild projects (`validate-security`, `terraform-plan`, `terraform-apply`), providing transparent trace logs for scanner violations and Terraform errors.
- **CodePipeline Visual Tracking**: The CodePipeline dashboard delivers real-time visibility across all 7 delivery stages.

---

### Event-Driven Notifications via EventBridge & SNS

1. **Amazon EventBridge Rule**:
   Listens for state change events emitted by CodePipeline (specifically capturing `FAILED` and `SUCCEEDED` triggers):
   ```json
   {
     "source": ["aws.codepipeline"],
     "detail-type": ["CodePipeline Pipeline Execution State Change"],
     "detail": {
       "pipeline": ["fcaj-devsecops-pipeline"],
       "state": ["FAILED", "SUCCEEDED"]
     }
   }
   ```

2. **Amazon SNS Topic & Email Alerts**:
   EventBridge routes events to the `fcaj-devsecops-notifications` SNS topic, which fans out email alerts to designated engineering contacts:
   ```bash
   # Verify confirmed subscriptions on the SNS topic
   aws sns list-subscriptions-by-topic --topic-arn "$SNS_TOPIC_ARN"
   ```

---

### Audit Logging via CloudTrail & Cost Governance via AWS Budgets

- **AWS CloudTrail**: Logs all API activity touching AWS resources (IAM, S3, CodePipeline, EC2) for compliance reporting and incident forensics.
- **AWS Budgets**: Enforces cost governance by alerting team leads when actual or forecasted monthly expenditures exceed target thresholds.
