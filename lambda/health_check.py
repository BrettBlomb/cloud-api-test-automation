import json
import requests
import os

API_BASE_URL = os.getenv(
    "BASE_URL",
    "https://jsonplaceholder.typicode.com"
)

def lambda_handler(event, context):
    try:
        response = requests.get(
            f"{API_BASE_URL}/posts/1",
            timeout=5
        )

        body = response.json()

        required_fields = ["userId", "id", "title", "body"]
        missing_fields = [f for f in required_fields if f not in body]

        if response.status_code != 200 or missing_fields:
            return {
                "status": "FAIL",
                "statusCode": response.status_code,
                "missingFields": missing_fields
            }

        return {
            "status": "PASS",
            "statusCode": response.status_code
        }

    except Exception as e:
        return {
            "status": "ERROR",
            "message": str(e)
        }
