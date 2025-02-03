class Operation:
    def __init__(self, nombre1=0, nombre2=0):
        # Le constructeur initialise les attributs nombre1 et nombre2 avec les valeurs par défaut
        self.nombre1 = nombre1
        self.nombre2 = nombre2

    def addition(self):
        # La méthode additionne nombre1 et nombre2 et affiche le résultat
        result = self.nombre1 + self.nombre2
        print(f"Le résultat de l'addition est : {result}")

# Instanciation de la classe
operation1 = Operation(3, 5)

# Appel de la méthode addition
operation1.addition()
