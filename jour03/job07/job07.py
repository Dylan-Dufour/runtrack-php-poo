import random

# Classe Carte
class Carte:
    def __init__(self, valeur, couleur):
        self.valeur = valeur  # La valeur de la carte (numérique ou figure)
        self.couleur = couleur  # La couleur de la carte (coeur, carreau, trèfle, pique)

    def __str__(self):
        return f"{self.valeur} de {self.couleur}"

    def valeur_numerique(self):
        """Retourne la valeur numérique de la carte pour le jeu"""
        if self.valeur in ['Valet', 'Dame', 'Roi']:
            return 10
        elif self.valeur == 'As':
            return 11
        else:
            return self.valeur


# Classe Jeu
class Jeu:
    def __init__(self):
        self.paquet = self.creer_paquet()
        self.melanger_paquet()

    def creer_paquet(self):
        """Crée un paquet de 52 cartes (4 couleurs, 13 valeurs)"""
        couleurs = ['Coeur', 'Carreau', 'Trèfle', 'Pique']
        valeurs = ['2', '3', '4', '5', '6', '7', '8', '9', '10', 'Valet', 'Dame', 'Roi', 'As']
        paquet = []
        for couleur in couleurs:
            for valeur in valeurs:
                paquet.append(Carte(valeur, couleur))
        return paquet

    def melanger_paquet(self):
        """Mélange le paquet de cartes"""
        random.shuffle(self.paquet)

    def distribuer_carte(self):
        """Distribue une carte du paquet"""
        if len(self.paquet) > 0:
            return self.paquet.pop()
        return None

    def calculer_points(self, mains):
        """Calcul les points d'une main"""
        total_points = 0
        as_count = 0
        for carte in mains:
            total_points += carte.valeur_numerique()
            if carte.valeur == 'As':
                as_count += 1

        # Ajuste les As (si un As vaut 11 et dépasse 21, il devient 1)
        while total_points > 21 and as_count > 0:
            total_points -= 10
            as_count -= 1
        return total_points

    def afficher_main(self, mains):
        """Affiche les cartes d'une main"""
        return [str(carte) for carte in mains]

    def jeu_complet(self):
        """Jouer une partie complète de Blackjack"""
        joueur_mains = [self.distribuer_carte(), self.distribuer_carte()]
        croupier_mains = [self.distribuer_carte(), self.distribuer_carte()]

        print("Carte du croupier:", str(croupier_mains[0]))  # Croupier montre une seule carte

        # Joueur joue
        while True:
            print("\nMain du joueur:", self.afficher_main(joueur_mains))
            points_joueur = self.calculer_points(joueur_mains)
            print(f"Total des points du joueur: {points_joueur}")
            if points_joueur > 21:
                print("Le joueur a dépassé 21 points. Vous avez perdu!")
                return "Croupier gagne"
            action = input("Voulez-vous 'prendre' une carte ou 'passer' ? ").lower()
            if action == 'prendre':
                joueur_mains.append(self.distribuer_carte())
            elif action == 'passer':
                break
            else:
                print("Choix invalide. Entrez 'prendre' ou 'passer'.")

        # Croupier joue
        while self.calculer_points(croupier_mains) < 17:
            croupier_mains.append(self.distribuer_carte())

        print("Main du croupier:", self.afficher_main(croupier_mains))
        points_croupier = self.calculer_points(croupier_mains)
        print(f"Total des points du croupier: {points_croupier}")

        # Déterminer le gagnant
        if points_croupier > 21:
            return "Joueur gagne"
        elif points_joueur > points_croupier:
            return "Joueur gagne"
        elif points_joueur < points_croupier:
            return "Croupier gagne"
        else:
            return "Égalité"


# Partie principale pour démarrer le jeu
def jouer_blackjack():
    jeu = Jeu()
    print("Bienvenue dans le jeu de Blackjack!")
    resultat = jeu.jeu_complet()
    print(f"\nRésultat de la partie: {resultat}")


# Démarrer le jeu
if __name__ == "__main__":
    jouer_blackjack();


