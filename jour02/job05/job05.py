class Voiture:
    def __init__(self, marque, modele, annee, kilometrage):
        self.__marque = marque  # Attribut privé
        self.__modele = modele  # Attribut privé
        self.__annee = annee    # Attribut privé
        self.__kilometrage = kilometrage  # Attribut privé
        self.__en_marche = False  # Attribut privé, initialisé à False
        self.__reservoir = 50  # Attribut privé, initialisé à 50

    # Assesseur et mutateur pour la marque
    def get_marque(self):
        return self.__marque

    def set_marque(self, marque):
        self.__marque = marque

    # Assesseur et mutateur pour le modèle
    def get_modele(self):
        return self.__modele

    def set_modele(self, modele):
        self.__modele = modele

    # Assesseur et mutateur pour l'année
    def get_annee(self):
        return self.__annee

    def set_annee(self, annee):
        self.__annee = annee

    # Assesseur et mutateur pour le kilométrage
    def get_kilometrage(self):
        return self.__kilometrage

    def set_kilometrage(self, kilometrage):
        self.__kilometrage = kilometrage

    # Assesseur et mutateur pour l'état de la voiture (en marche ou pas)
    def get_en_marche(self):
        return self.__en_marche

    def set_en_marche(self, en_marche):
        self.__en_marche = en_marche

    # Assesseur et mutateur pour le réservoir
    def get_reservoir(self):
        return self.__reservoir

    def set_reservoir(self, reservoir):
        self.__reservoir = reservoir

    # Méthode privée pour vérifier si le réservoir est suffisant
    def __verifier_plein(self):
        return self.__reservoir

    # Méthode pour démarrer la voiture
    def demarrer(self):
        if self.__verifier_plein() > 5:  # Si le réservoir contient plus de 5 litres, la voiture peut démarrer
            self.__en_marche = True
            print(f"La voiture {self.__marque} {self.__modele} a démarré.")
        else:
            print(f"Impossible de démarrer. Le réservoir de la {self.__marque} {self.__modele} est insuffisant.")

    # Méthode pour arrêter la voiture
    def arreter(self):
        self.__en_marche = False
        print(f"La voiture {self.__marque} {self.__modele} est arrêtée.")

# Création d'une voiture
ma_voiture = Voiture("Toyota", "Corolla", 2020, 25000)

# Vérification de l'état initial
print(f"Voiture en marche ? {ma_voiture.get_en_marche()}")  # Devrait être False

# Tentative de démarrer avec un réservoir suffisant
ma_voiture.demarrer()

# Vérification après démarrage
print(f"Voiture en marche ? {ma_voiture.get_en_marche()}")  # Devrait être True

# Réduire le réservoir à moins de 5 litres
ma_voiture.set_reservoir(3)

# Tentative de démarrer avec un réservoir insuffisant
ma_voiture.demarrer()  # La voiture ne devrait pas démarrer

# Arrêter la voiture
ma_voiture.arreter()

# Vérification après arrêt
print(f"Voiture en marche ? {ma_voiture.get_en_marche()}")  # Devrait être False

