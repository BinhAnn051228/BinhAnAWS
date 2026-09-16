import os
import sys
import shutil
from pathlib import Path

if hasattr(sys.stdout, "reconfigure"):
    sys.stdout.reconfigure(encoding="utf-8")

BASE_DIR = Path(r"c:\Users\ASUS\Desktop\Năm cuối\Prj thực tập\BinhAnAWS")
CONTENT_DIR = BASE_DIR / "content" / "5-Workshop"
STATIC_IMAGES_DIR = BASE_DIR / "static" / "images" / "5-Workshop"

def ensure_dir(d):
    os.makedirs(d, exist_ok=True)

def copy_if_missing(src, dst):
    if os.path.exists(src) and not os.path.exists(dst):
        ensure_dir(os.path.dirname(dst))
        shutil.copy2(src, dst)
        print(f"Copied image: {src} -> {dst}")

def setup_image_aliases():
    # Copy IAM images to create-role directories if helpful
    iam_roles_src = STATIC_IMAGES_DIR / "5.3-IAM-Secrets" / "5.3.1-pipeline-iam-roles"
    if iam_roles_src.exists():
        copy_if_missing(iam_roles_src / "5.3.1-codepipeline-role.png",
                        STATIC_IMAGES_DIR / "5.3-IAM-Secrets" / "5.3.1-create-codepipeline-role" / "5.3.1-codepipeline-role.png")
        copy_if_missing(iam_roles_src / "5.3.2-scan-build-role.png",
                        STATIC_IMAGES_DIR / "5.3-IAM-Secrets" / "5.3.2-create-scanbuild-role" / "5.3.2-scan-build-role.png")
        copy_if_missing(iam_roles_src / "5.3.3-terraform-plan-role.png",
                        STATIC_IMAGES_DIR / "5.3-IAM-Secrets" / "5.3.3-create-terraform-plan-role" / "5.3.3-terraform-plan-role.png")
        copy_if_missing(iam_roles_src / "5.3.4-terraform-deploy-role.png",
                        STATIC_IMAGES_DIR / "5.3-IAM-Secrets" / "5.3.4-create-terraform-deploy-role" / "5.3.4-terraform-deploy-role.png")

    ssm_src = STATIC_IMAGES_DIR / "5.3-IAM-Secrets" / "5.3.2-ssm-parameter-store"
    if ssm_src.exists():
        copy_if_missing(ssm_src / "check SSM.png",
                        STATIC_IMAGES_DIR / "5.3-IAM-Secrets" / "5.3.5-configure-ssm-parameter-store" / "check SSM.png")

def clean_orphans():
    orphans = [
        CONTENT_DIR / "5.3-IAM-Secrets" / "5.3.1-pipeline-iam-roles",
        CONTENT_DIR / "5.3-IAM-Secrets" / "5.3.2-ssm-parameter-store",
        CONTENT_DIR / "5.3-IAM-Secrets" / "5.3.3-save-secret-securestring",
        CONTENT_DIR / "5.3-IAM-Secrets" / "5.3.4-verify-least-privilege",
        CONTENT_DIR / "5.4-GitHub-CodePipeline" / "5.4.2-create-aws-codeconnections",
        CONTENT_DIR / "5.4-GitHub-CodePipeline" / "5.4.4-create-s3-artifact-bucket",
        CONTENT_DIR / "5.4-GitHub-CodePipeline" / "5.4.5-init-aws-codepipeline",
        CONTENT_DIR / "5.6-Terraform-Plan-Approval" / "5.6.4-save-tfplan-artifact",
        CONTENT_DIR / "5.6-Terraform-Plan-Approval" / "5.6.5-manual-approval-stage",
        CONTENT_DIR / "5.7-Terraform-Apply" / "5.7.2-assume-terraform-deploy-role",
        CONTENT_DIR / "5.7-Terraform-Apply" / "5.7.3-apply-approved-plan",
        CONTENT_DIR / "5.8-Target-Environment" / "5.8.1-create-amazon-vpc",
        CONTENT_DIR / "5.8-Target-Environment" / "5.8.3-public-subnet-route-table",
        CONTENT_DIR / "5.8-Target-Environment" / "5.8.5-create-amazon-ec2",
        CONTENT_DIR / "5.8-Target-Environment" / "5.8.6-deploy-web-application"
    ]
    for o in orphans:
        if o.exists():
            shutil.rmtree(o)
            print(f"Removed orphan directory: {o}")

if __name__ == "__main__":
    setup_image_aliases()
    clean_orphans()
