---
title: "Week 2 Worklog"
date: 2026-08-10
weight: 2
chapter: false
pre: " <b> 1.2. </b> "
---

### Week 2 Objectives:
* Learn Amazon S3 security and Bucket Policy.
* Practice IAM Role and AWS CLI.
* Learn EC2 User Data.
* Learn Amazon RDS MySQL.
* Connect EC2 with Amazon RDS.
* Deploy a simple web application on AWS.

### Tasks to be carried out this week:
| Day | Task | Start Date | Completion Date | Reference Material |
| --- | --- | --- | --- | --- |
| 1 | - Learn Amazon S3 Policy.<br>- Create an S3 Bucket.<br>- Configure Bucket Policy.<br>- Test public access. | 10/08/2026 | 10/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 2 | - Learn IAM Role.<br>- Attach IAM Role to EC2.<br>- Test Amazon S3 access using AWS CLI. | 11/08/2026 | 11/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 3 | - Learn EC2 User Data script.<br>- Automate Apache and PHP installation using User Data.<br>- Verify automated application deployment without manual SSH. | 12/08/2026 | 12/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 4 | - Learn Amazon RDS MySQL.<br>- Create DB Subnet Group in private subnets.<br>- Launch an Amazon RDS MySQL instance.<br>- Configure Security Group allowing port 3306 from EC2. | 13/08/2026 | 13/08/2026 | <https://cloudjourney.awsstudygroup.com/> |
| 5 | - Connect EC2 instance with Amazon RDS MySQL.<br>- Deploy a database-driven web application on AWS.<br>- Test database connection and verify data persistence. | 14/08/2026 | 14/08/2026 | <https://cloudjourney.awsstudygroup.com/> |

### Week 2 Achievements:
* Mastered Amazon S3 security and Bucket Policy:
  * Created S3 Buckets with restricted private access.
  * Configured JSON Bucket Policy for fine-grained access control.
  * Verified public access blocks and access prevention.
* Mastered IAM Role and AWS CLI:
  * Created and attached IAM Role to EC2 instances.
  * Eliminated hardcoded AWS credentials from application instances.
  * Successfully performed S3 operations via AWS CLI (`aws s3 ls`, `aws s3 cp`).
* Implemented EC2 User Data:
  * Automated package installation and service startup at instance boot.
* Deployed Amazon RDS MySQL:
  * Provisioned RDS database instance within isolated private subnets.
  * Applied restrictive Security Group inbound rules for port 3306.
* Connected EC2 with Amazon RDS:
  * Successfully deployed and tested dynamic web app with persistent SQL storage.
