import math

# Classe Forme
class Forme:
    def aire(self):
        return 0  # La méthode aire() renvoie 0 par défaut

# Classe Rectangle héritant de Forme
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur  # Attribut largeur
        self.hauteur = hauteur  # Attribut hauteur

    # Surcharge de la méthode aire() pour renvoyer l'aire du rectangle
    def aire(self):
        return self.largeur * self.hauteur  # Calcul de l'aire

# Classe Cercle héritant de Forme
class Cercle(Forme):
    def __init__(self, radius):
        self.radius = radius  # Attribut radius (rayon)

    # Surcharge de la méthode aire() pour renvoyer l'aire du cercle
    def aire(self):
        return math.pi * self.radius ** 2  # Aire du cercle : π * r^2

# Instancier la classe Rectangle
rectangle = Rectangle(10, 5)

# Instancier la classe Cercle
cercle = Cercle(7)

# Afficher les résultats des méthodes aire()
print(f"L'aire du rectangle est : {rectangle.aire()}")  # Affiche l'aire du rectangle
print(f"L'aire du cercle est : {cercle.aire()}")  # Affiche l'aire du cercle


