class Personnage:
    def __init__(self, x, y):
        # Le constructeur initialise la position (x, y) du personnage
        self.x = x
        self.y = y

    def gauche(self):
        # Déplace le personnage à gauche (diminue l'index x)
        self.x -= 1

    def droite(self):
        # Déplace le personnage à droite (augmente l'index x)
        self.x += 1

    def bas(self):
        # Déplace le personnage en bas (augmente l'index y)
        self.y += 1

    def haut(self):
        # Déplace le personnage en haut (diminue l'index y)
        self.y -= 1

    def position(self):
        # Renvoie la position actuelle du personnage (x, y)
        return (self.x, self.y)

# Instanciation du personnage à une position donnée (par exemple x=2, y=3)
personnage1 = Personnage(2, 3)

# Affichage de la position initiale
print(f"Position initiale : {personnage1.position()}")

# Déplacements du personnage
personnage1.gauche()
personnage1.bas()
personnage1.droite()
personnage1.haut()

# Affichage de la position après déplacements
print(f"Position après déplacements : {personnage1.position()}")


