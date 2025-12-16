from utils.api_client import APIClient

def test_health_endpoint():
    client = APIClient("https://jsonplaceholder.typicode.com")
    response = client.get("/posts/1")

    assert response.status_code == 200
    body = response.json()
    assert "id" in body
#test
