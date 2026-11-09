import pytest
from app.texte import nettoyer_texte


@pytest.mark.parametrize("entree, attendu", [
    ("  BONJOUR   monde  ", "bonjour monde"),
    (" déjà propre ", "déjà propre"),
    ("", ""),
    ("     ", ""),
    ("PYTHON", "python"),
])
def test_nettoyer_texte(entree, attendu):
    assert nettoyer_texte(entree) == attendu


@pytest.mark.parametrize("entree", [123, None])
def test_entree_non_textuelle_declenche_type_error(entree):
    with pytest.raises(TypeError):
        nettoyer_texte(entree)


def test_nettoyer_texte_deja_nettoye_ne_change_pas_resultat():
    texte = "bonjour monde"
    assert nettoyer_texte(nettoyer_texte(texte)) == texte
