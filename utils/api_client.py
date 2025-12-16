import requests
from utils.config import BASE_URL, AUTH_TOKEN


class APIClient:
    def __init__(self, timeout=5):
        """
        API client for interacting with REST services.

        :param timeout: Request timeout in seconds
        """
        self.base_url = BASE_URL
        self.timeout = timeout
        self.headers = {
            "Content-Type": "application/json"
        }

        if AUTH_TOKEN:
            self.headers["Authorization"] = f"Bearer {AUTH_TOKEN}"

    def get(self, endpoint, params=None):
        return requests.get(
            f"{self.base_url}{endpoint}",
            headers=self.headers,
            params=params,
            timeout=self.timeout
        )

    def post(self, endpoint, payload):
        return requests.post(
            f"{self.base_url}{endpoint}",
            json=payload,
            headers=self.headers,
            timeout=self.timeout
        )
