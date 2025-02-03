class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        # Le constructeur initialise les attributs nombre1 et nombre2 avec des valeurs par défaut
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        # La méthode additionne nombre1 et nombre2 et affiche le résultat
        result = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est : {result}")

# Instanciation de l'objet Operation avec des valeurs spécifiques
operation1 = Operation(5, 7)

# Appel de la méthode addition() pour afficher le résultat
operation1.addition()
