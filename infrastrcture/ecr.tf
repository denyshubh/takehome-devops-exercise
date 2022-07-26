resource "aws_ecr_repository" "container_image_registry" {
  name = "container-image-registry"
}

resource "aws_ecr_repository_policy" "repo-policy" {
  repository = aws_ecr_repository.container_image_registry.name
  policy     = <<EOF
  {
    "Version": "2008-10-17",
    "Statement": [
      {
        "Sid": "adds full ecr access to the demo repository",
        "Effect": "Allow",
        "Principal": "*",
        "Action": [
          "ecr:BatchCheckLayerAvailability",
          "ecr:BatchGetImage",
          "ecr:CompleteLayerUpload",
          "ecr:GetDownloadUrlForLayer",
          "ecr:GetLifecyclePolicy",
          "ecr:InitiateLayerUpload",
          "ecr:PutImage",
          "ecr:UploadLayerPart"
        ]
      }
    ]
  }
  EOF
}

resource "null_resource" "deploy_image" {

 provisioner "local-exec" {
    command = "/bin/bash deploy.sh ${var.account_id} ${var.region}"
  }
} 