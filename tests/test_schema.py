def test_post_schema(api_client):
    response = api_client.get("/posts/1")
    body = response.json()

    expected_fields = {
        "userId": int,
        "id": int,
        "title": str,
        "body": str
    }

    for field, field_type in expected_fields.items():
        assert field in body
        assert isinstance(body[field], field_type)
