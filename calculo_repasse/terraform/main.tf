terraform {
  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 4.16"
    }
  }

  required_version = ">= 1.2.0"
}

provider "aws" {
  profile = "ClinicaPirmezTerraform"
  region  = "us-east-1"
}

variable "lambda_prefix" {
  default     = "calculo-repasse"
  description = "Lambda's name prefix"
}

variable "lambda_image_tag" {
  type        = string
  default     = "latest"
  description = "Lambda's image tag"
}
