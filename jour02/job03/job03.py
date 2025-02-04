class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre  # Attribut privé
        self.__auteur = auteur  # Attribut privé
        self.__nombre_de_pages = nombre_de_pages  # Attribut privé
        self.__disponible = True  # Attribut privé, initialisé à True

    # Assesseur pour le titre
    def get_titre(self):
        return self.__titre

    # Mutateur pour le titre
    def set_titre(self, titre):
        self.__titre = titre

    # Assesseur pour l'auteur
    def get_auteur(self):
        return self.__auteur

    # Mutateur pour l'auteur
    def set_auteur(self, auteur):
        self.__auteur = auteur

    # Assesseur pour le nombre de pages
    def get_nombre_de_pages(self):
        return self.__nombre_de_pages

    # Mutateur pour le nombre de pages
    def set_nombre_de_pages(self, nombre_de_pages):
        if isinstance(nombre_de_pages, int) and nombre_de_pages > 0:
            self.__nombre_de_pages = nombre_de_pages
        else:
            print("Erreur : Le nombre de pages doit être un entier positif.")

    # Méthode pour afficher les informations du livre
    def afficher(self):
        print(f"Titre : {self.__titre}, Auteur : {self.__auteur}, Nombre de pages : {self.__nombre_de_pages}")

    # Méthode pour vérifier si le livre est disponible
    def verification(self):
        return self.__disponible

    # Méthode pour emprunter le livre
    def emprunter(self):
        if self.verification():  # Vérifie si le livre est disponible sans utiliser l'attribut 'disponible'
            self.__disponible = False
            print(f"Le livre '{self.__titre}' a été emprunté.")
        else:
            print(f"Le livre '{self.__titre}' n'est pas disponible pour l'emprunt.")

    # Méthode pour rendre le livre
    def rendre(self):
        if not self.verification():  # Vérifie si le livre est emprunté
            self.__disponible = True
            print(f"Le livre '{self.__titre}' a été rendu et est maintenant disponible.")
        else:
            print(f"Le livre '{self.__titre}' n'a pas été emprunté, il est déjà disponible.")

# Exemple d'utilisation

# Création d'un livre
livre = Livre("1984", "George Orwell", 328)

# Affichage des informations du livre
livre.afficher()

# Vérification de la disponibilité
print("Disponible ?", livre.verification())  # Devrait afficher True

# Emprunter le livre
livre.emprunter()  # Le livre devient indisponible

# Vérification après emprunt
print("Disponible ?", livre.verification())  # Devrait afficher False

# Tenter de réemprunter un livre déjà emprunté
livre.emprunter()  # Devrait afficher un message d'indisponibilité

# Rendre le livre
livre.rendre()  # Le livre devient disponible à nouveau

# Vérification après rendu
print("Disponible ?", livre.verification())  # Devrait afficher True

# Tenter de rendre un livre qui n'a pas été emprunté
livre.rendre()  # Devrait afficher un message indiquant que le livre est déjà disponible

