class Student:
    def __init__(self, nom, prenom, numero_etudiant):
        self.__nom = nom  # Attribut privé
        self.__prenom = prenom  # Attribut privé
        self.__numero_etudiant = numero_etudiant  # Attribut privé
        self.__credits = 0  # Attribut privé, initialisé à 0
        self.__level = self.__studentEval()  # Attribut privé, calculé via studentEval()

    # Méthode pour ajouter des crédits
    def add_credits(self, credits):
        if credits > 0:  # Vérification que les crédits ajoutés sont positifs
            self.__credits += credits
            self.__level = self.__studentEval()  # Mise à jour du niveau après l'ajout des crédits
        else:
            print("Erreur : Le nombre de crédits doit être positif.")

    # Méthode privée pour évaluer le niveau de l'étudiant
    def __studentEval(self):
        if self.__credits >= 90:
            return "Excellent"
        elif self.__credits >= 80:
            return "Très bien"
        elif self.__credits >= 70:
            return "Bien"
        elif self.__credits >= 60:
            return "Passable"
        else:
            return "Insuffisant"

    # Méthode pour afficher les informations de l'étudiant
    def studentInfo(self):
        print(f"Nom : {self.__nom}")
        print(f"Prénom : {self.__prenom}")
        print(f"Numéro d'étudiant : {self.__numero_etudiant}")
        print(f"Crédits : {self.__credits}")
        print(f"Niveau : {self.__level}")

# Instanciation d'un étudiant John Doe avec le numéro d'étudiant 145
student = Student("Doe", "John", 145)

# Ajout de crédits
student.add_credits(30)  # Ajoute 30 crédits
student.add_credits(25)  # Ajoute 25 crédits
student.add_credits(40)  # Ajoute 40 crédits

# Affichage des informations de l'étudiant
student.studentInfo()

