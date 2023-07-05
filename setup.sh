#!/bin/bash

# Construction des images

docker build -t authentication_test -f Dockerfile.authentication .
docker build -t authorization_test -f Dockerfile.authorization .
docker build -t content_test -f Dockerfile.content .

# Lancement de docker-compose
docker-compose up --abort-on-container-exit > log.txt