from fastapi.testclient import TestClient

from app.main import app

client = TestClient(app)


def test_health():
    response = client.get("/health")
    assert response.status_code == 200
    assert response.json() == {"status": "ok"}


def test_releases():
    response = client.get("/releases")
    body = response.json()
    assert response.status_code == 200
    assert body["app"] == "pucpr-devops"
    assert body["versao"] == "1.0.0"
    assert body["ambiente"] == "producao"
