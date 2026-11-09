import pytest
from unittest.mock import Mock
from app.moderation import decider


def test_spam_est_bloque_et_predict_est_appele():
    modele = Mock()
    modele.predict.return_value = "spam"
    resultat = decider(modele, "Offre miracle")
    assert resultat == "bloquer"
    modele.predict.assert_called_once_with("Offre miracle")


def test_message_normal_est_autorise():
    modele = Mock()
    modele.predict.return_value = "normal"
    assert decider(modele, "Bonjour") == "autoriser"


def test_erreur_du_modele_est_propagee():
    modele = Mock()
    modele.predict.side_effect = RuntimeError("Modele indisponible")
    with pytest.raises(RuntimeError, match="Modele indisponible"):
        decider(modele, "Bonjour")
