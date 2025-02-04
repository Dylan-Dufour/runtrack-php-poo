class Commande:
    def __init__(self, numero_commande):
        self.__numero_commande = numero_commande  # Attribut privé
        self.__plats_commandes = {}  # Dictionnaire des plats commandés
        self.__statut = "en cours"  # Statut initial de la commande

    # Assesseurs et mutateurs pour le numéro de la commande
    def get_numero_commande(self):
        return self.__numero_commande

    def set_numero_commande(self, numero):
        self.__numero_commande = numero

    # Assesseurs et mutateurs pour le statut de la commande
    def get_statut(self):
        return self.__statut

    def set_statut(self, statut):
        self.__statut = statut

    # Méthode pour ajouter un plat à la commande
    def ajouter_plat(self, nom_plat, prix):
        if nom_plat not in self.__plats_commandes:
            self.__plats_commandes[nom_plat] = {"prix": prix, "statut": "commandé"}
            print(f"Le plat '{nom_plat}' a été ajouté à la commande.")
        else:
            print(f"Le plat '{nom_plat}' est déjà dans la commande.")

    # Méthode pour annuler la commande
    def annuler_commande(self):
        self.__statut = "annulée"
        print("La commande a été annulée.")

    # Méthode privée pour calculer le total de la commande
    def __calculer_total(self):
        total = 0
        for plat, details in self.__plats_commandes.items():
            total += details["prix"]
        return total

    # Méthode publique pour calculer la TVA (exemple 20% de TVA)
    def calculer_tva(self):
        total = self.__calculer_total()
        tva = total * 0.20  # TVA à 20%
        return tva

    # Méthode pour afficher la commande et son total
    def afficher_commande(self):
        if self.__statut != "annulée":
            print(f"Commande numéro: {self.__numero_commande}")
            print(f"Statut: {self.__statut}")
            print("Plats commandés :")
            for plat, details in self.__plats_commandes.items():
                print(f"  - {plat}: {details['prix']} EUR")
            total = self.__calculer_total()
            print(f"Total à payer : {total} EUR")
            tva = self.calculer_tva()
            print(f"TVA (20%) : {tva} EUR")
            print(f"Total TTC : {total + tva} EUR")
        else:
            print(f"La commande numéro {self.__numero_commande} a été annulée et ne peut pas être affichée.")

# Création d'une commande
commande1 = Commande(1001)

# Ajout de plats à la commande
commande1.ajouter_plat("Pizza Margherita", 10)
commande1.ajouter_plat("Salade César", 7.5)
commande1.ajouter_plat("Spaghetti Bolognese", 12)

# Affichage de la commande avec le total et la TVA
commande1.afficher_commande()

# Annulation de la commande
commande1.annuler_commande()

# Tentative d'affichage après annulation
commande1.afficher_commande()

