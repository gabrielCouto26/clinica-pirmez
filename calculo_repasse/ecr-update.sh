#!bin/bash

image_name='calculo-repasse-lambda'

aws --profile ClinicaPirmezTerraform \
    ecr get-login-password | \
    docker login --username AWS --password-stdin 415953478593.dkr.ecr.us-east-1.amazonaws.com

echo "-> Atualizando imagem: $image_name"

docker build -t $image_name:latest . -f Dockerfile.lambda
docker tag $image_name:latest 415953478593.dkr.ecr.us-east-1.amazonaws.com/$image_name:latest
docker push 415953478593.dkr.ecr.us-east-1.amazonaws.com/$image_name:latest

echo "-> Imagem Docker atualizada!"

aws --profile ClinicaPirmezTerraform \
    lambda update-function-code \
    --function-name $image_name \
    --image-uri 415953478593.dkr.ecr.us-east-1.amazonaws.com/$image_name:latest

echo "-> Função Lambda atualizada!"
