---
title: "Target Workload Environment"
date: 2026-08-25
weight: 8
chapter: false
pre: " <b> 5.8. </b> "
---

# 5.8. Target Workload Environment

This chapter details the workload target infrastructure managed automatically by Terraform, encompassing **Amazon VPC**, **Security Groups**, **Amazon EC2**, and automated application bootstrapping.

---

### Workload Network Architecture & Access Controls

- **Amazon VPC & Subnets**: Provisions a dedicated VPC with isolated address space, an Internet Gateway, and a Route Table associated with the public subnet for routing internet traffic.
- **Security Group Ingress Controls**: Configures web server security groups permitting HTTP (port 80) traffic for accessibility and testing. Ingress port 22 (SSH) remains fully closed to eliminate brute-force attack vectors. Default security groups are stripped of all rules.

---

### EC2 Provisioning & Automated Application Bootstrap

1. **Amazon EC2 Instance Configuration**:
   Instances run Amazon Linux 2023 (`t3.micro`) equipped with an IAM Instance Profile granting secure management via AWS Systems Manager (SSM) Session Manager without exposed management ports.

2. **Automated User Data Bootstrapping (`user_data.sh.tftpl`)**:
   During instance launch, the user data script installs Python 3.11, configures the Flask web application, installs requirements, and registers a persistent `systemd` service:

```bash
#!/bin/bash
set -euo pipefail

# Update packages and install Python
dnf update -y
dnf install -y python3.11 python3.11-pip git

# Create dedicated application user
useradd -m -s /bin/bash appuser || true
mkdir -p /opt/app && chown appuser:appuser /opt/app

# Deploy application code
cat <<'EOF' > /opt/app/app.py
from flask import Flask, jsonify
app = Flask(__name__)

@app.route("/")
def index():
    return "FCAJ AWS DevSecOps Workshop - Demo Application Running"

@app.route("/health")
def health():
    return jsonify({"status": "healthy", "service": "demo-web-app"}), 200

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=80)
EOF

# Register systemd unit
cat <<'EOF' > /etc/systemd/system/demo-app.service
[Unit]
Description=FCAJ Demo Web Application
After=network.target

[Service]
User=root
WorkingDirectory=/opt/app
ExecStart=/usr/bin/python3.11 /opt/app/app.py
Restart=always
RestartSec=5

[Install]
WantedBy=multi-user.target
EOF

systemctl daemon-reload
systemctl enable --now demo-app
```

---

### Verifying Network Connectivity & Application Access

Verify public connectivity and endpoint health using the emitted workload outputs:

```bash
# Extract Public IP from workload output
EC2_IP=$(terraform -chdir=workload output -raw ec2_public_ip)
echo "Accessing EC2 Web Server at: http://${EC2_IP}/"

# Query HTTP health endpoint
curl -I "http://${EC2_IP}/"
curl -s "http://${EC2_IP}/health"
```

> [!TIP]
> A successful `200 OK` response from the `/health` route validates that both the infrastructure network layer and the demo application service are operating correctly.
