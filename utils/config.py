import os

BASE_URL = os.getenv(
    "BASE_URL",
    "https://jsonplaceholder.typicode.com"
)

AUTH_TOKEN = os.getenv("AUTH_TOKEN")
AWS_S3_BUCKET = os.getenv("AWS_S3_BUCKET", "qa-test-reports")
