FROM python:3.10-alpine
WORKDIR /app
ARG TEST_FILE
COPY ${TEST_FILE} test.py
CMD ["python", "test.py"]