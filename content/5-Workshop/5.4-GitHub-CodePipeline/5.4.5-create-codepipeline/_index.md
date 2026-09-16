---
title: "Initialize AWS CodePipeline"
date: 2026-08-25
weight: 5
chapter: false
pre: " <b> 5.4.5. </b> "
---

# 5.4.5. Initialize AWS CodePipeline

The pipeline uses V1 type, `SUPERSEDED` execution mode, and the S3 artifact bucket as artifact store. Stages are declared sequentially: `Source`, `ValidateTest`, `SecurityScan`, `TerraformPlan`, `ManualApproval`, `TerraformApply`, and `PostDeployVerification`.

### CodePipeline Definition

```hcl
resource "aws_codepipeline" "main" {
  name          = "${local.name}-pipeline"
  role_arn      = aws_iam_role.codepipeline.arn
  pipeline_type = "V1"
  execution_mode = "SUPERSEDED"

  artifact_store {
    location = var.pipeline_artifact_bucket
    type     = "S3"
  }

  stage {
    name = "Source"
    action {
      name             = "GitHubSource"
      category         = "Source"
      owner            = "AWS"
      provider         = "CodeStarSourceConnection"
      version          = "1"
      output_artifacts = ["SourceOutput"]
      configuration = {
        ConnectionArn    = aws_codeconnections_connection.github.arn
        FullRepositoryId = local.repo_full_name
        BranchName       = var.github_branch
        DetectChanges    = "true"
      }
    }
  }

  stage {
    name = "ValidateTest"
    action {
      name            = "ValidateAndUnitTest"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.validate_security.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "validate", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "SecurityScan"
    action {
      name            = "ShiftLeftSecurity"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.validate_security.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "security", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "TerraformPlan"
    action {
      name             = "CreatePlan"
      category         = "Build"
      owner            = "AWS"
      provider         = "CodeBuild"
      version          = "1"
      input_artifacts  = ["SourceOutput"]
      output_artifacts = ["PlanOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.terraform_plan.name
      }
    }
  }

  stage {
    name = "ManualApproval"
    action {
      name     = "ReviewTerraformPlan"
      category = "Approval"
      owner    = "AWS"
      provider = "Manual"
      version  = "1"
      configuration = {
        NotificationArn = aws_sns_topic.pipeline.arn
        CustomData      = "Review PlanOutput/plan.txt. Approve only if the planned infrastructure change is expected and safe."
      }
    }
  }

  stage {
    name = "TerraformApply"
    action {
      name            = "ApplyApprovedPlan"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput", "PlanOutput"]
      configuration = {
        ProjectName   = aws_codebuild_project.terraform_apply_smoke.name
        PrimarySource = "SourceOutput"
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "apply", type = "PLAINTEXT" }
        ])
      }
    }
  }

  stage {
    name = "PostDeployVerification"
    action {
      name            = "SmokeTest"
      category        = "Build"
      owner           = "AWS"
      provider        = "CodeBuild"
      version         = "1"
      input_artifacts = ["SourceOutput"]
      configuration = {
        ProjectName = aws_codebuild_project.terraform_apply_smoke.name
        EnvironmentVariables = jsonencode([
          { name = "RUN_MODE", value = "smoke", type = "PLAINTEXT" }
        ])
      }
    }
  }

  depends_on = [aws_iam_role_policy.codepipeline]
}
```

---

![AWS CodePipeline Console - End-to-end 7-stage CI/CD pipeline execution overview](/images/5-Workshop/5.4-GitHub-CodePipeline/5.4.5-create-codepipeline/%E1%BA%A2nh%20ch%E1%BB%A5p%20m%C3%A0n%20h%C3%ACnh%202026-09-16%20024115.png)

*AWS CodePipeline Console - End-to-end 7-stage CI/CD pipeline execution overview*

