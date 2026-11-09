import pytest
from app.web import create_app


@pytest.fixture
def client():
    app = create_app()
    app.config["TESTING"] = True
    return app.test_client()


def test_message_normal_est_autorise(client):
    response = client.post("/moderate", json={"message": "bonjour"})
    assert response.status_code == 200
    assert response.get_json() == {"decision": "autoriser"}


def test_message_spam_est_bloque_sans_tenir_compte_de_la_casse(client):
    response = client.post("/moderate", json={"message": "ceci est du SPAM"})
    assert response.status_code == 200
    assert response.get_json() == {"decision": "bloquer"}


def test_message_absent_retourne_erreur_400(client):
    response = client.post("/moderate", json={})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


def test_message_non_textuel_retourne_erreur_400(client):
    response = client.post("/moderate", json={"message": 42})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


def test_message_vide_retourne_erreur_400(client):
    response = client.post("/moderate", json={"message": "   "})
    assert response.status_code == 400
    assert response.get_json() == {"error": "Invalid message"}


def test_corps_json_liste_retourne_erreur_400(client):
    response = client.post("/moderate", json=["bonjour"])
    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}


def test_corps_non_json_retourne_erreur_400(client):
    response = client.post("/moderate", data="pas du json",
                           content_type="text/plain")
    assert response.status_code == 400
    assert response.get_json() == {"error": "JSON object required"}
