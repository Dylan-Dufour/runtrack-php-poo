# Classe Rectangle
class Rectangle:
    def __init__(self, longueur, largeur):
        self.__longueur = longueur  # Attribut privé longueur
        self.__largeur = largeur  # Attribut privé largeur

    # Méthode pour calculer le périmètre
    def perimetre(self):
        return 2 * (self.__longueur + self.__largeur)

    # Méthode pour calculer la surface
    def surface(self):
        return self.__longueur * self.__largeur

    # Assesseurs (getters) et mutateurs (setters)
    def get_longueur(self):
        return self.__longueur

    def set_longueur(self, longueur):
        self.__longueur = longueur

    def get_largeur(self):
        return self.__largeur

    def set_largeur(self, largeur):
        self.__largeur = largeur

# Classe Parallelepipede héritant de Rectangle
class Parallelepipede(Rectangle):
    def __init__(self, longueur, largeur, hauteur):
        super().__init__(longueur, largeur)  # Initialisation de Rectangle
        self.__hauteur = hauteur  # Attribut privé hauteur

    # Méthode pour calculer le volume
    def volume(self):
        return self.surface() * self.__hauteur

    # Assesseur et mutateur pour la hauteur
    def get_hauteur(self):
        return self.__hauteur

    def set_hauteur(self, hauteur):
        self.__hauteur = hauteur

# Instancier la classe Rectangle
rectangle = Rectangle(10, 5)

# Afficher le périmètre et la surface du rectangle
print(f"Périmètre du rectangle : {rectangle.perimetre()}")  # Affiche le périmètre
print(f"Surface du rectangle : {rectangle.surface()}")  # Affiche la surface

# Utilisation des assesseurs et mutateurs
rectangle.set_longueur(12)  # Modifier la longueur du rectangle
rectangle.set_largeur(6)  # Modifier la largeur du rectangle

# Afficher les nouvelles valeurs
print(f"Nouvelle longueur : {rectangle.get_longueur()}")
print(f"Nouvelle largeur : {rectangle.get_largeur()}")
print(f"Nouveau périmètre : {rectangle.perimetre()}")  # Affiche le nouveau périmètre
print(f"Nouvelle surface : {rectangle.surface()}")  # Affiche la nouvelle surface

# Instancier la classe Parallelepipede
parallelepipede = Parallelepipede(12, 6, 8)

# Afficher le volume du parallélépipède
print(f"Volume du parallélépipède : {parallelepipede.volume()}")  # Affiche le volume


