import math

class Cercle:
    def __init__(self, rayon):
        # Le constructeur initialise le rayon du cercle
        self.rayon = rayon

    def changerRayon(self, nouveau_rayon):
        # La méthode permet de modifier le rayon du cercle
        self.rayon = nouveau_rayon

    def afficherInfos(self):
        # Affiche les informations du cercle : rayon, diamètre, circonférence et aire
        print(f"Rayon : {self.rayon}")
        print(f"Diamètre : {self.diametre()}")
        print(f"Circonférence : {self.circonference()}")
        print(f"Aire : {self.aire()}")

    def circonference(self):
        # La méthode calcule la circonférence du cercle
        return 2 * math.pi * self.rayon

    def aire(self):
        # La méthode calcule l'aire du cercle
        return math.pi * self.rayon ** 2

    def diametre(self):
        # La méthode calcule le diamètre du cercle
        return 2 * self.rayon


# Création de deux cercles
cercle1 = Cercle(4)
cercle2 = Cercle(7)

# Affichage des informations pour chaque cercle
print("Cercle 1 (rayon = 4) :")
cercle1.afficherInfos()

print("\nCercle 2 (rayon = 7) :")
cercle2.afficherInfos()

# Modification du rayon du premier cercle et affichage des nouvelles informations
cercle1.changerRayon(10)
print("\nCercle 1 après modification du rayon (rayon = 10) :")
cercle1.afficherInfos()
