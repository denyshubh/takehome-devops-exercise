#!/bin/bash

region=$1
account_id=$2

# authenticate to ecr
aws ecr get-login-password --region ${region} | docker login --username AWS --password-stdin ${account_id}.dkr.ecr.${region}.amazonaws.com

# docker build image
docker build --build-arg=APP_JWT_SECRET=$APP_JWT_SECRET -t ${account_id}.dkr.ecr.${region}.amazonaws.com/container-image-registry:latest 

# docker push image

docker push ${account_id}.dkr.ecr.${region}.amazonaws.com/container-image-registry:latest