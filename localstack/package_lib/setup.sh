#!/bin/bash
docker build -t lambda-layer:numpy ${NOCACHE} .
id=$(docker create lambda-layer:numpy bash)
docker cp $id:/root/lambda-layer.zip ./lambda-layer.zip
docker rm -v $id
