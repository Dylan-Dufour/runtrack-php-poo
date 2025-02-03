class Produit:
    def __init__(self, nom, prixHT, TVA):
        # Le constructeur initialise le nom, le prix HT et la TVA
        self.nom = nom
        self.prixHT = prixHT
        self.TVA = TVA

    def CalculerPrixTTC(self):
        # La méthode calcule le prix TTC en ajoutant la TVA au prix HT
        prixTTC = self.prixHT * (1 + self.TVA / 100)
        return prixTTC

    def afficher(self):
        # La méthode affiche toutes les informations du produit
        print(f"Nom : {self.nom}")
        print(f"Prix HT : {self.prixHT}€")
        print(f"TVA : {self.TVA}%")
        print(f"Prix TTC : {self.CalculerPrixTTC():.2f}€")

    def modifierNom(self, nouveau_nom):
        # Méthode pour modifier le nom du produit
        self.nom = nouveau_nom

    def modifierPrix(self, nouveau_prixHT):
        # Méthode pour modifier le prix HT du produit
        self.prixHT = nouveau_prixHT

    def modifierTVA(self, nouvelle_TVA):
        # Méthode pour modifier la TVA du produit
        self.TVA = nouvelle_TVA

    def obtenirNom(self):
        # Méthode pour obtenir le nom du produit
        return self.nom

    def obtenirPrixHT(self):
        # Méthode pour obtenir le prix HT du produit
        return self.prixHT

    def obtenirTVA(self):
        # Méthode pour obtenir la TVA du produit
        return self.TVA


# Création de plusieurs produits
produit1 = Produit("Ordinateur", 1000, 20)
produit2 = Produit("Téléphone", 500, 15)
produit3 = Produit("Casque", 150, 10)

# Affichage des informations des produits
print("Informations des produits :\n")
produit1.afficher()
produit2.afficher()
produit3.afficher()

# Modification des informations des produits
produit1.modifierNom("Ordinateur Portable")
produit1.modifierPrix(1200)
produit2.modifierNom("Smartphone")
produit2.modifierPrix(600)

# Affichage des informations après modification
print("\nInformations des produits après modification :\n")
produit1.afficher()
produit2.afficher()
