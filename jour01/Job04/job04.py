class Point:
    def __init__(self, x, y):
        # Le constructeur initialise les coordonnées x et y du point
        self.x = x
        self.y = y

    def afficherLesPoints(self):
        # Affiche les coordonnées du point
        print(f"Les coordonnées du point sont : ({self.x}, {self.y})")

    def afficherX(self):
        # Affiche la coordonnée x
        print(f"Coordonnée x : {self.x}")

    def afficherY(self):
        # Affiche la coordonnée y
        print(f"Coordonnée y : {self.y}")

    def changerX(self, nouvelle_valeur):
        # Change la valeur de x
        self.x = nouvelle_valeur
        print(f"Nouvelle coordonnée x : {self.x}")

    def changerY(self, nouvelle_valeur):
        # Change la valeur de y
        self.y = nouvelle_valeur
        print(f"Nouvelle coordonnée y : {self.y}")

# Instanciation d'un point avec des coordonnées spécifiques
point1 = Point(3, 4)

# Affichage des coordonnées du point
point1.afficherLesPoints()

# Affichage des coordonnées séparées
point1.afficherX()
point1.afficherY()

# Modification des coordonnées
point1.changerX(10)
point1.changerY(20)

# Nouveau affichage des coordonnées après modification
point1.afficherLesPoints()
