resource "aws_ecr_repository" "calculo_repasse" {
  name = "calculo-repasse"
}

output "ecr_repository_url" {
  value = aws_ecr_repository.calculo_repasse.repository_url
}
