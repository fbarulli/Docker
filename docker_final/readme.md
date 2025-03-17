# Docker Setup Overview

This project implements a testing framework for a sentiment analysis API using Docker and Docker Compose. The setup is designed to run multiple test suites against a FastAPI application that analyzes sentiment in text.

## Architecture

1. **API Service**: A pre-built FastAPI container (`datascientest/fastapi:1.0.0`) that provides sentiment analysis endpoints.

2. **Test Containers**: Three separate test containers that validate different aspects of the API:
   - `auth-test`: Tests authentication functionality
   - `authz-test`: Tests authorization functionality
   - `content-test`: Tests sentiment analysis functionality

3. **Networking**: All containers communicate through a dedicated bridge network.

4. **Logging**: Test results are logged to a shared volume mounted across all test containers.

## Test Workflow

1. The API container starts first, exposing port 8000.
2. Test containers start afterward, running their respective test scripts.
3. Each test container connects to the API, performs its tests, and logs results.
4. If any test fails, the container exits with a non-zero status code.

## Security Features

The API implements authentication and authorization:
- Users must provide valid username/password combinations
- Different users have different permission levels (v1 and v2 endpoints)
- The API returns appropriate HTTP status codes based on authentication/authorization status

## File Structure

- `Dockerfile`: Generic template for building test containers
- `Dockerfile.base`: Base image with Python and requests library
- `docker-compose.yml`: Orchestrates the entire test environment
- `*_test.py`: Individual test scripts for different aspects of the API
- `requirements.txt`: Python dependencies for the test containers
- `setup.sh`: Helper script to build and run the environment