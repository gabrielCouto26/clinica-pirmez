data "aws_caller_identity" "current" {}

locals {
  prefix              = "calculo-repasse"
  account_id          = data.aws_caller_identity.current.account_id
  ecr_repository_name = "${local.prefix}-lambda-container"
  ecr_image_tag       = "latest"
}

######## ECR ########

resource "aws_ecr_repository" "repo" {
  name = local.ecr_repository_name

  provisioner "local-exec" {
    command = "bash ../ecr-update.sh"
  }
}

resource "null_resource" "ecr_image" {
  triggers = {
    python_file = md5(file("../src/main.py"))
    docker_file = md5(file("../Dockerfile"))
  }
}

######## S3 ########

resource "aws_s3_bucket" "clinica_pirmez" {
  bucket = "clinica-pirmez"

  tags = {
    Projeto = "Clinica Pirmez"
    Env     = "Dev"
  }
}

resource "aws_s3_object" "consultas_folder" {
  bucket = aws_s3_bucket.clinica_pirmez.id
  key    = "consultas/"
}

resource "aws_s3_object" "repasses_folder" {
  bucket = aws_s3_bucket.clinica_pirmez.id
  key    = "repasses/"
}

resource "aws_lambda_permission" "s3_invoke_lambda_permission" {
  statement_id  = "AllowS3InvokeLambda"
  action        = "lambda:InvokeFunction"
  function_name = aws_lambda_function.calculo_repasse.arn
  principal     = "s3.amazonaws.com"
  source_arn    = aws_s3_bucket.clinica_pirmez.arn
}

######## LAMBDA ########

resource "aws_iam_role" "lambda" {
  name               = "${local.prefix}-lambda-role"
  assume_role_policy = <<EOF
{
   "Version": "2012-10-17",
   "Statement": [
       {
           "Action": "sts:AssumeRole",
           "Principal": {
               "Service": "lambda.amazonaws.com"
           },
           "Effect": "Allow"
       }
   ]
}
 EOF
}

resource "aws_iam_role_policy_attachment" "lambda_ecr_policy_attachment" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonEC2ContainerRegistryReadOnly"
}

resource "aws_iam_role_policy_attachment" "lambda_cloudwatch_policy_attachment" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/service-role/AWSLambdaBasicExecutionRole"
}

resource "aws_iam_role_policy_attachment" "lambda_s3_access" {
  role       = aws_iam_role.lambda.name
  policy_arn = "arn:aws:iam::aws:policy/AmazonS3ReadOnlyAccess"
}

resource "aws_lambda_function" "calculo_repasse" {
  depends_on = [
    null_resource.ecr_image,
    aws_s3_bucket.clinica_pirmez
  ]
  function_name = "${local.prefix}-lambda"
  role          = aws_iam_role.lambda.arn
  timeout       = 300
  image_uri     = "${aws_ecr_repository.repo.repository_url}:${local.ecr_image_tag}"
  package_type  = "Image"

  environment {
    variables = {
      FILE_PATH = "s3://${aws_s3_bucket.clinica_pirmez.bucket}/consultas/$${s3:ObjectKey}"
      LOAD_PATH = "s3://${aws_s3_bucket.clinica_pirmez.bucket}/repasses/repasses.csv"
    }
  }
}

resource "aws_s3_bucket_notification" "bucket_notification" {
  depends_on = [
    aws_lambda_function.calculo_repasse
  ]
  bucket = aws_s3_bucket.clinica_pirmez.id

  lambda_function {
    lambda_function_arn = aws_lambda_function.calculo_repasse.arn
    events              = ["s3:ObjectCreated:*"]
    filter_prefix       = "consultas/"
    filter_suffix       = ".csv"
  }
}

output "lambda_name" {
  value = aws_lambda_function.calculo_repasse.id
}

output "lambda_image_uri" {
  value = aws_lambda_function.calculo_repasse.image_uri
}

######## CLOUD WATCH ########

resource "aws_cloudwatch_log_group" "lambda_log_group" {
  name = "/aws/lambda/${aws_lambda_function.calculo_repasse.function_name}"
}
