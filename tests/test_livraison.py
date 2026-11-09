import pytest
from app.livraison import frais_livraison


def test_livraison_panier_ordinaire():
    # Arrange
    montant = 120
    # Act
    resultat = frais_livraison(montant)
    # Assert
    assert resultat == 25


@pytest.mark.parametrize("montant, attendu", [
    (299, 25),
    (300, 0),
    (301, 0),
    (0, 25),
])
def test_frais_livraison_selon_montant(montant, attendu):
    assert frais_livraison(montant) == attendu


def test_montant_negatif_declenche_value_error():
    with pytest.raises(ValueError):
        frais_livraison(-1)
