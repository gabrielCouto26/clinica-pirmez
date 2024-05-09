resource "aws_lambda_function" "calculo_repasse" {
  depends_on = [
    aws_s3_bucket.clinica_pirmez
  ]
  function_name = "${var.lambda_prefix}-lambda"
  role          = aws_iam_role.lambda.arn
  timeout       = 300
  image_uri     = "${aws_ecr_repository.repo.repository_url}:${var.lambda_image_tag}"
  package_type  = "Image"

  environment {
    variables = {
      LOAD_FOLDER = "s3://${aws_s3_bucket.clinica_pirmez.bucket}/repasses/"
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

output "lambda_image_uri" {
  value = aws_lambda_function.calculo_repasse.image_uri
}
