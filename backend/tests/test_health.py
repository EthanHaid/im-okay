def test_health_check_route(client):
    res = client.get("/health")

    assert res.status_code == 200
    assert res.text == "200"
