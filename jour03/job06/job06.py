# Classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque  # Marque du véhicule
        self.modele = modele  # Modèle du véhicule
        self.annee = annee    # Année de fabrication du véhicule
        self.prix = prix      # Prix du véhicule

    # Méthode pour afficher les informations du véhicule
    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix} €")

# Classe Voiture héritant de Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)  # Initialisation de la classe parent
        self.portes = portes  # Attribut spécifique à la classe Voiture
# Classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque  # Marque du véhicule
        self.modele = modele  # Modèle du véhicule
        self.annee = annee    # Année de fabrication du véhicule
        self.prix = prix      # Prix du véhicule

    # Méthode pour afficher les informations du véhicule
    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix} €")

# Classe Voiture héritant de Vehicule
class Voiture(Vehicule):
    def __init__(self, marque, modele, annee, prix, portes=4):
        super().__init__(marque, modele, annee, prix)  # Initialisation de la classe parent
        self.portes = portes  # Attribut spécifique à la classe Voiture

    # Surcharge de la méthode informationsVehicule() pour afficher les informations spécifiques à la voiture
    def informationsVehicule(self):
        super().informationsVehicule()  # Appel à la méthode de la classe parent
        print(f"Nombre de portes : {self.portes}")  # Affiche le nombre de portes de la voiture

# Instancier la classe Vehicule
vehicule = Vehicule("Toyota", "Corolla", 2022, 20000)

# Instancier la classe Voiture
voiture = Voiture("Peugeot", "208", 2023, 15000)

# Afficher les informations du véhicule
print("Informations du véhicule :")
vehicule.informationsVehicule()

# Afficher les informations de la voiture
print("\nInformations de la voiture :")
voiture.informationsVehicule()

# Classe Vehicule
class Vehicule:
    def __init__(self, marque, modele, annee, prix):
        self.marque = marque  # Marque du véhicule
        self.modele = modele  # Modèle du véhicule
        self.annee = annee    # Année de fabrication du véhicule
        self.prix = prix      # Prix du véhicule

    # Méthode pour afficher les informations du véhicule
    def informationsVehicule(self):
        print(f"Marque : {self.marque}")
        print(f"Modèle : {self.modele}")
        print(f"Année : {self.annee}")
        print(f"Prix : {self.prix} €")

# Classe Moto héritant de Vehicule
class Moto(Vehicule):
    def __init__(self, marque, modele, annee, prix, roue=2):
        super().__init__(marque, modele, annee, prix)  # Initialisation de la classe parent
        self.roue = roue  # Attribut spécifique à la classe Moto

    # Surcharge de la méthode informationsVehicule() pour afficher les informations spécifiques à la moto
    def informationsVehicule(self):
        super().informationsVehicule()  # Appel à la méthode de la classe parent
        print(f"Nombre de roues : {self.roue}")  # Affiche le nombre de roues de la moto

# Instancier un objet Moto avec les informations nécessaires
moto = Moto("Kawasaki", "Ninja 650", 2023, 7500)

# Appeler la méthode informationsVehicule() sur l'objet Moto
print("Informations de la moto :")
moto.informationsVehicule()


