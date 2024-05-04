#!bin/bash

aws --profile ClinicaPirmezTerraform ecr get-login-password --region us-east-1 | \
    docker login --username AWS --password-stdin 415953478593.dkr.ecr.us-east-1.amazonaws.com

docker build -t calculo-repasse-lambda:latest . -f Dockerfile.lambda
docker tag calculo-repasse-lambda:latest 415953478593.dkr.ecr.us-east-1.amazonaws.com/calculo-repasse-lambda-container:latest
docker push 415953478593.dkr.ecr.us-east-1.amazonaws.com/calculo-repasse-lambda-container:latest

echo "Imagem Docker atualizada!"