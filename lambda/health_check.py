import requests
import os

API_BASE_URL = os.getenv(
    "BASE_URL",
    "https://jsonplaceholder.typicode.com"
)

ENDPOINTS = [
    {
        "path": "/posts/1",
        "required_fields": ["userId", "id", "title", "body"]
    },
    {
        "path": "/posts/2",
        "required_fields": ["userId", "id", "title", "body"]
    }
]


def lambda_handler(event, context):
    results = []

    for endpoint in ENDPOINTS:
        try:
            response = requests.get(
                f"{API_BASE_URL}{endpoint['path']}",
                timeout=5
            )

            body = response.json()
            missing_fields = [
                f for f in endpoint["required_fields"]
                if f not in body
            ]

            results.append({
                "endpoint": endpoint["path"],
                "statusCode": response.status_code,
                "missingFields": missing_fields
            })

        except Exception as e:
            return {
                "status": "ERROR",
                "message": str(e)
            }

    failures = [
        r for r in results
        if r["statusCode"] != 200 or r["missingFields"]
    ]

    if failures:
        return {
            "status": "FAIL",
            "failures": failures
        }

    return {
        "status": "PASS",
        "checkedEndpoints": len(results)
    }
