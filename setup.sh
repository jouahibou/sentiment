#!/bin/bash

# Nom du conteneur pour le service API
api_container_name="my-api-container"

# Construction de l'image pour le service API
docker build -t authentication_test -f Dockerfile.authentication .
docker build -t authorization_test -f Dockerfile.authorization .
docker build -t content_test -f Dockerfile.content .

# Lancement des conteneurs avec docker-compose
docker-compose up --abort-on-container-exit > log.txt &

# Attente de la disponibilité du service API
echo "Waiting for API service to become available..."
while ! curl -sSf "http://localhost:8000/health" > /dev/null; do
    sleep 1
done

# Lancement des tests d'authentification
docker run --rm --network container:${api_container_name} -e LOG=1 authentication_test

# Lancement des tests d'autorisation
docker run --rm --network container:${api_container_name} -e LOG=1 authorization_test

# Lancement des tests de contenu
docker run --rm --network container:${api_container_name} -e LOG=1 content_test