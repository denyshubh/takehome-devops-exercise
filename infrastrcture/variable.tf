variable "region" {
  type = string
  default = "us-east-1"
}

variable "account_id" {
  type = string
  default = "123456789"
}

variable "aws_ecr_repo" {
  type = string
  default = "container-image-registry"
}