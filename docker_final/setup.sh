#!/bin/bash

# Pull the API image
docker image pull datascientest/fastapi:1.0.0

# Build the base image
docker build -f Dockerfile.base -t python310-requests . || {
  echo "Failed to build base image"
  exit 1
}

# Build test images
for test in auth_test authz_test content_test; do
  docker build -t ${test}:latest --build-arg TEST_FILE=${test}.py . || {
    echo "Failed to build ${test} image"
    exit 1
  }
done

# Run Docker Compose
docker-compose up --build || {
  echo "Docker Compose failed"
  exit 1
}

# Copy logs
if docker ps -a --format '{{.Names}}' | grep -q "^api$"; then
  docker cp api:/app/api_test.log ./log.txt || echo "Warning: Could not copy log file"
else
  echo "Warning: API container not found, no logs copied"
fi

# Clean up
docker-compose down