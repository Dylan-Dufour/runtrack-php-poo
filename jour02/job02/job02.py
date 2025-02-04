class Livre:
    def __init__(self, titre, auteur, nombre_de_pages):
        self.__titre = titre  # Attribut privé
        self.__auteur = auteur  # Attribut privé
        self.__nombre_de_pages = nombre_de_pages  # Attribut privé

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

# Création d'un livre avec titre, auteur et nombre de pages
livre = Livre("1984", "George Orwell", 328)

# Affichage des informations du livre
livre.afficher()

# Changer le titre, l'auteur et le nombre de pages
livre.set_titre("Animal Farm")
livre.set_auteur("George Orwell")
livre.set_nombre_de_pages(112)

# Affichage des informations après modification
livre.afficher()

# Tentative de modification avec un nombre de pages incorrect
livre.set_nombre_de_pages(-10)  # Cela devrait afficher un message d'erreur

# Tentative de modification avec un nombre de pages non entier
livre.set_nombre_de_pages("not a number")  # Cela devrait également afficher un message d'erreur
