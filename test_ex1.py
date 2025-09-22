import pytest
from ExDebug1 import environnement_optimal
#test unitaire pour la fonction environnement_optimal()
def test_environnement_optimal():
    #arrange : preparer les variables d'entrées et le résultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Tout est sous contrôle!"

    #act : appeler la fonction et la tester
    resultat_obtenu = environnement_optimal(temperature,poussiere,humidite)

    #assert :  vérifier le resultat
    assert resultat_attendu == resultat_obtenu

def test_environnement_optimal2():
    # arrange : preparer les variables d'entrées et le résultat attendu
    temperature = 30
    poussiere = "faible"
    humidite = 40
    resultat_attendu = "Environnement non optimal"

    # act : appeler la fonction et la tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # assert :  vérifier le resultat
    assert resultat_attendu == resultat_obtenu

def test_environnement_optimal3():
    # arrange : preparer les variables d'entrées et le résultat attendu
    temperature = 25
    poussiere = "faible"
    humidite = 20
    resultat_attendu = "Environnement non optimal"

    # act : appeler la fonction et la tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # assert :  vérifier le resultat
    assert resultat_attendu == resultat_obtenu

def test_environnement_optimal4():
    # arrange : preparer les variables d'entrées et le résultat attendu
    temperature = 30
    poussiere = "moyen"
    humidite = 25
    resultat_attendu = "Environnement non optimal"

    # act : appeler la fonction et la tester
    resultat_obtenu = environnement_optimal(temperature, poussiere, humidite)

    # assert :  vérifier le resultat
    assert resultat_attendu == resultat_obtenu