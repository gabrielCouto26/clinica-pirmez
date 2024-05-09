#!bin/bash

aws --profile ClinicaPirmezTerraform \
    ecr get-login-password | \
    docker login --username AWS --password-stdin 415953478593.dkr.ecr.us-east-1.amazonaws.com

docker build -t calculo-repasse-lambda:latest . -f Dockerfile.lambda
docker tag calculo-repasse-lambda:latest 415953478593.dkr.ecr.us-east-1.amazonaws.com/calculo-repasse-lambda-container:latest
docker push 415953478593.dkr.ecr.us-east-1.amazonaws.com/calculo-repasse-lambda-container:latest

echo "Imagem Docker atualizada!"

aws --profile ClinicaPirmezTerraform \
    lambda update-function-code \
    --function-name calculo-repasse-lambda \
    --image-uri 415953478593.dkr.ecr.us-east-1.amazonaws.com/calculo-repasse-lambda-container:latest

echo "Função Lambda atualizada!"
