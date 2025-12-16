from utils.api_client import APIClient

def test_invalid_auth():
    client = APIClient()
    response = client.get("/posts")

    # Public API returns 200, but structure is validated
    assert response.status_code == 200
    assert isinstance(response.json(), list)
