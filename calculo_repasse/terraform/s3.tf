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