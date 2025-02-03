class Animal:
    def __init__(self):
        # Le constructeur initialise les attributs age à 0 et prenom à une chaîne vide
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        # La méthode vieillir ajoute 1 à l'âge de l'animal
        self.age += 1

# Instanciation de l'objet Animal
animal1 = Animal()

# Affichage de l'âge de l'animal
print(f"Âge de l'animal : {animal1.age}")

# Faire vieillir l'animal
animal1.vieillir()

# Affichage de l'âge après avoir vieilli l'animal
print(f"Âge de l'animal après avoir vieilli : {animal1.age}")

class Animal:
    def __init__(self):
        # Le constructeur initialise l'âge à 0 et le prénom à une chaîne vide
        self.age = 0
        self.prenom = ""

    def vieillir(self):
        # La méthode vieillir ajoute 1 à l'âge de l'animal
        self.age += 1

    def nommer(self, nom):
        # La méthode nommer prend un nom et l'assigne à l'attribut prenom
        self.prenom = nom

    def afficherNom(self):
        # Affiche le nom de l'animal
        print(f"Le nom de l'animal est : {self.prenom}")

# Instanciation de l'objet Animal
animal1 = Animal()

# Nommer l'animal
animal1.nommer("Rex")

# Afficher le nom de l'animal
animal1.afficherNom()

# Affichage de l'âge de l'animal
print(f"Âge de l'animal : {animal1.age}")

# Faire vieillir l'animal
animal1.vieillir()

# Affichage de l'âge après avoir vieilli l'animal
print(f"Âge de l'animal après avoir vieilli : {animal1.age}")


