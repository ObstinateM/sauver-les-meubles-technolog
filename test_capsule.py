from unittest.mock import patch
from capsule import Capsule


def test_fonctionnel():
    capsule = Capsule(nom="Arpeggio", taille=40, couleur="noir")
    assert capsule.is_valid_for_nespresso()  # Vérifie si l'expression est vraie


def test_erreur():
    capsule = Capsule(nom="Arpeggio", taille=50, couleur="noir")
    assert not capsule.is_valid_for_nespresso()  # Vérifie si l'expression est fausse


# Ici, on "patch" la méthode is_valid_for_nespresso de la classe Capsule pour qu'elle retourne False
# Elle retournera donc, TOUJOURS False dans ce test
# C'est pratique si on doit utiliser cette méthode mais que ce n'est pas la méthode que l'on veut tester
@patch("capsule.Capsule.is_valid_for_nespresso", return_value=False)
def test_avec_patch(mock_is_valid):
    capsule = Capsule(nom="Arpeggio", taille=40, couleur="noir")
    assert not capsule.is_valid_for_nespresso()
