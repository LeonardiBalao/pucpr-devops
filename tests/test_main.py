from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health_status_code():
    response = client.get("/health")
    assert response.status_code == 200


def test_health_body():
    response = client.get("/health")
    assert response.json() == {"status": "ok"}


def test_releases_status_code():
    response = client.get("/releases")
    assert response.status_code == 200


def test_releases_payload():
    body = client.get("/releases").json()
    assert body["app"] == "pucpr-devops"
    assert body["versao"] == "1.0.0"
    assert body["ambiente"] == "producao"


def test_unknown_route_404():
    response = client.get("/rota-inexistente")
    assert response.status_code == 404
