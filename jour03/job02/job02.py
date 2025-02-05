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
    def __init__(self, matiereEnseignee, age):
        self.__matiereEnseignee = matiereEnseignee  # Attribut privé
        self.age = age  # Attribut âge

    def enseigner(self):
        print("Le cours va commencer")  # Affiche "Le cours va commencer"

    def bonjour(self):
        print("Bonjour !")  # Affiche "Bonjour !"

# Instancier la classe Eleve
eleve = Eleve()
eleve.bonjour()  # L'élève dit bonjour
eleve.allerEnCours()  # L'élève va en cours
eleve.modifierAge(15)  # Modifie l'âge de l'élève à 15 ans
eleve.afficherAge()  # Affiche l'âge modifié de l'élève

# Instancier la classe Professeur
professeur = Professeur(matiereEnseignee="Mathématiques", age=40)
professeur.bonjour()  # Le professeur dit bonjour
professeur.enseigner()  # Le professeur commence le cours


