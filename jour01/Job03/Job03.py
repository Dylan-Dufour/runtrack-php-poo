class Personne:
    def __init__(self, nom, prenom):
        # Le constructeur initialise les attributs nom et prenom
        self.nom = nom
        self.prenom = prenom

    def SePresenter(self):
        # La méthode retourne une présentation de la personne
        return f"Bonjour, je m'appelle {self.prenom} {self.nom}."

# Instanciation de plusieurs personnes
personne1 = Personne("Dupont", "Pierre")
personne2 = Personne("Lemoine", "Sophie")
personne3 = Personne("Martin", "Julien")

# Appel de la méthode SePresenter() pour chaque personne
print(personne1.SePresenter())
print(personne2.SePresenter())
print(personne3.SePresenter())

