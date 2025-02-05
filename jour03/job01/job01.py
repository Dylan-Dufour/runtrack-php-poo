# Classe Personne
class Personne:
    def __init__(self, age=14):
        self.age = age  # Attribut age initialisé à 14 par défaut

    def afficherAge(self):
        print(f"J'ai {self.age} ans")  # Affiche l'âge de la personne

    def bonjour(self):
        print("Hello")  # Affiche "Hello"

    def modifierAge(self, age):
        self.age = age  # Modifie l'âge de la personne

# Classe Eleve héritant de Personne
class Eleve(Personne):
    def allerEnCours(self):
        print("Je vais en cours")  # Affiche "Je vais en cours"

    def afficherAge(self):
        print(f"J'ai {self.age} ans")  # Affiche l'âge de l'élève

# Classe Professeur
class Professeur:
    def __init__(self, matiereEnseignee):
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé

    def enseigner(self):
        print("Le cours va commencer")  # Affiche "Le cours va commencer"

# Instancier la classe Personne
personne = Personne()
personne.afficherAge()  # Affiche l'âge par défaut

# Instancier la classe Eleve
eleve = Eleve()
eleve.afficherAge()  # Affiche l'âge par défaut de l'élève


