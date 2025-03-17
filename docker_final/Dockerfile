FROM python:3.10-alpine
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt --progress-bar off
WORKDIR /app
ARG TEST_FILE
COPY ${TEST_FILE} test.py
CMD ["python", "test.py"]