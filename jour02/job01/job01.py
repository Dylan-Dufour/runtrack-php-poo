class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé
        self.__largeur = largeur    # Attribut privé
    
    # Assesseur pour la longueur
    def get_longueur(self):
        return self.__longueur
    
    # Mutateur pour la longueur
    def set_longueur(self, longueur):
        self.__longueur = longueur
    
    # Assesseur pour la largeur
    def get_largeur(self):
        return self.__largeur
    
    # Mutateur pour la largeur
    def set_largeur(self, largeur):
        self.__largeur = largeur
    
    # Méthode pour afficher les dimensions du rectangle
    def afficher(self):
        print(f"Longueur : {self.__longueur}, Largeur : {self.__largeur}")

# Création d'un rectangle avec longueur = 10 et largeur = 5
rect = Rectangle(10, 5)

# Affichage des dimensions du rectangle
rect.afficher()

# Changement de la longueur et de la largeur
rect.set_longueur(15)
rect.set_largeur(8)

# Vérification des modifications
rect.afficher()
