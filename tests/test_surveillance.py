import pytest
from unittest.mock import patch
from app.surveillance import surveiller
from app.notifications import envoyer_notification


def test_taux_superieur_au_seuil_declenche_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.15) == "alerte"
        notifier.assert_called_once_with("Taux eleve")


def test_taux_inferieur_au_seuil_ne_declenche_pas_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.05) == "ok"
        notifier.assert_not_called()


def test_taux_exactement_egal_au_seuil_ne_declenche_pas_alerte():
    with patch("app.surveillance.envoyer_notification") as notifier:
        assert surveiller(0.10) == "ok"
        notifier.assert_not_called()


def test_erreur_notification_est_propagee():
    with patch("app.surveillance.envoyer_notification") as notifier:
        notifier.side_effect = RuntimeError("Notification indisponible")
        with pytest.raises(RuntimeError, match="Notification indisponible"):
            surveiller(0.15)

def test_notification_non_configuree_declenche_erreur():
    with pytest.raises(RuntimeError, match="Service non configure"):
        envoyer_notification("Taux eleve")