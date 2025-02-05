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

# Instancier la classe Rectangle
rectangle = Rectangle(10, 5)

# Afficher l'aire du rectangle
print(f"L'aire du rectangle est : {rectangle.aire()}")  # Affiche l'aire du rectangle


