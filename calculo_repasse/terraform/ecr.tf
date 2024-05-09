resource "aws_ecr_repository" "repo" {
  name = "${var.lambda_prefix}-lambda"

  provisioner "local-exec" {
    command = "bash ../ecr-update.sh"
  }
}
