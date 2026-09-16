---
title: "Sharing and Feedback"
date: 2026-07-14
weight: 7
chapter: false
pre: " <b> 7. </b> "
---

Having completed the **Workforce Bootcamp - First Cloud AI Journey** internship at **AWS Viet Nam**, as a student majoring in **Computer Networks and Data Communication** from **Hanoi University of Civil Engineering (HUCE)**, I would like to share my reflections, practical experiences, and constructive feedback for upcoming cohorts:

### General Program Evaluation

**1. Learning & Working Environment**  
The program is structured with high academic and practical rigor. Curricula and lab challenges are seamlessly coupled with the capstone project (**FCAJ AWS DevSecOps Pipeline Workshop**). Having clear roadmap milestones empowered interns to proactively manage time and cultivate engineering independence.

**2. Mentorship & Administrative Support**  
Mentors demonstrated profound technical mastery and dedication. When encountering complex challenges—such as designing least-privilege IAM policies, configuring multi-stage CodeBuild security gates, or resolving Terraform state lock contention—mentors consistently guided me through log analysis (CloudWatch Logs) and root-cause troubleshooting rather than simply handing out answers. The administrative team was equally responsive in provisioning cloud sandboxes and technical assistance.

**3. Alignment with Computer Networks & Data Communication Major**  
As a student of **Computer Networks and Data Communication**, I found the project directly reinforced my academic foundations:
*   Direct application of fundamental networking principles—routing protocols, subnetting, CIDR allocation, and Internet Gateways—when architecting the workload's **Amazon VPC**.
*   In-depth comprehension of traffic flow filtering and network security through **Security Groups** and **Network ACLs**, notably enforcing security compliance by completely closing public SSH access (port 22) and utilizing **AWS Systems Manager (SSM) Session Manager**.
*   Hands-on experience automating network infrastructure via **Terraform IaC** and implementing Shift-Left security gates (**Checkov, Gitleaks, Bandit, Trivy**) in modern delivery pipelines.

**4. Skill Development Opportunities**  
The internship drove holistic professional growth: mastering automated CI/CD pipelines orchestrated by AWS CodePipeline, adopting a Shift-Left security mindset, authoring clean technical documentation, and managing project deadlines effectively.

**5. Community Culture & Team Spirit**  
The vibrant open-sharing culture within the **AWS Study Group** and **First Cloud Journey (FCAJ)** community was inspiring. Attending in-person events such as the **AWS Vietnam Community Meetup** at AWS Hanoi Office provided exposure to cutting-edge cloud and AI trends while expanding my professional network.

---

### Survey Responses

*   **What was your most satisfying accomplishment during the internship?**  
    Designing, provisioning, and operating an end-to-end automated DevSecOps ecosystem on AWS: from pushing code to GitHub, triggering multi-scanner automated vulnerability checks, generating change plans with Manual Approval gates, to automated Terraform Apply and verifying application health via automated smoke tests.
*   **What areas do you recommend improving for future cohorts?**  
    Introducing informal weekly tech-sharing sessions among small peer groups to discuss common Terraform, IAM, and pipeline debugging challenges.
*   **Would you recommend this program to your peers?**  
    Unquestionably. It is an exceptional hands-on program that bridges the gap between academic theory and enterprise cloud engineering practices.

---

### Suggestions & Future Outlook

*   **Suggestion**: Introduce advanced workshops exploring distributed cloud networking architectures (Transit Gateway, VPC Peering, Hybrid Cloud via AWS Outposts) and deeper observability tooling (AWS X-Ray, CloudWatch Container Insights).
*   **Expectation**: Continue engaging with the AWS Vietnam community, participating in future knowledge-sharing events, and supporting upcoming student cohorts.
