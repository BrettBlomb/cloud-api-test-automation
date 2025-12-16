from utils.api_client import APIClient

@pytest.mark.regression
def test_data_structure():
    client = APIClient()
    response = client.get("/posts/1")

    body = response.json()

    assert response.status_code == 200
    assert "userId" in body
    assert "id" in body
    assert "title" in body
    assert "body" in body
#test
