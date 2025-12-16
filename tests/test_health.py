def test_health_endpoint(api_client):
    """
    Validates that the API health endpoint responds successfully
    and returns the expected data structure.
    """
    response = api_client.get("/posts/1")

    assert response.status_code == 200

    body = response.json()
    assert "id" in body
    assert body["id"] == 1
