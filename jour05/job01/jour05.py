<?php
// Classe Case
class CaseJeu {
    private $valeur;

    public function __construct() {
        $this->valeur = ' ';  // Initialement vide
    }

    public function getValeur() {
        return $this->valeur;
    }

    public function setValeur($symbole) {
        $this->valeur = $symbole;
    }

    public function estVide() {
        return $this->valeur == ' ';
    }
}

// Classe Plateau
class Plateau {
    private $grille;

    public function __construct() {
        $this->grille = array_fill(0, 3, array_fill(0, 3, new CaseJeu()));
    }

    public function afficher() {
        for ($i = 0; $i < 3; $i++) {
            $ligne = "";
            for ($j = 0; $j < 3; $j++) {
                $ligne .= $this->grille[$i][$j]->getValeur();
                if ($j < 2) $ligne .= "|";
            }
            echo $ligne . "<br>";
            if ($i < 2) echo "-----<br>";
        }
    }

    public function mettreAJour($ligne, $colonne, $symbole) {
        if ($this->grille[$ligne][$colonne]->estVide()) {
            $this->grille[$ligne][$colonne]->setValeur($symbole);
            return true;
        }
        return false;
    }

    public function verifieVictoire($symbole) {
        // Vérifier les lignes, les colonnes et les diagonales
        for ($i = 0; $i < 3; $i++) {
            if ($this->grille[$i][0]->getValeur() == $symbole && $this->grille[$i][1]->getValeur() == $symbole && $this->grille[$i][2]->getValeur() == $symbole) {
                return true;
            }
            if ($this->grille[0][$i]->getValeur() == $symbole && $this->grille[1][$i]->getValeur() == $symbole && $this->grille[2][$i]->getValeur() == $symbole) {
                return true;
            }
        }
        if ($this->grille[0][0]->getValeur() == $symbole && $this->grille[1][1]->getValeur() == $symbole && $this->grille[2][2]->getValeur() == $symbole) {
            return true;
        }
        if ($this->grille[0][2]->getValeur() == $symbole && $this->grille[1][1]->getValeur() == $symbole && $this->grille[2][0]->getValeur() == $symbole) {
            return true;
        }
        return false;
    }

    public function estComplet() {
        foreach ($this->grille as $ligne) {
            foreach ($ligne as $case) {
                if ($case->estVide()) {
                    return false;
                }
            }
        }
        return true;
    }
}

// Classe Joueur
class Joueur {
    private $nom;
    private $symbole;

    public function __construct($nom, $symbole) {
        $this->nom = $nom;
        $this->symbole = $symbole;
    }

    public function getNom() {
        return $this->nom;
    }

    public function getSymbole() {
        return $this->symbole;
    }
}

// Classe Jeu
class Jeu {
    private $plateau;
    private $joueur1;
    private $joueur2;
    private $tour;
    private $gagnant;

    public function __construct($joueur1, $joueur2) {
        $this->plateau = new Plateau();
        $this->joueur1 = $joueur1;
        $this->joueur2 = $joueur2;
        $this->tour = 1; // Joueur 1 commence
        $this->gagnant = null;
    }

    public function jouer($ligne, $colonne) {
        if ($this->tour % 2 != 0) {
            $joueurActuel = $this->joueur1;
        } else {
            $joueurActuel = $this->joueur2;
        }

        if ($this->plateau->mettreAJour($ligne, $colonne, $joueurActuel->getSymbole())) {
            $this->plateau->afficher();
            if ($this->plateau->verifieVictoire($joueurActuel->getSymbole())) {
                $this->gagnant = $joueurActuel;
                echo "<br>" . $joueurActuel->getNom() . " a gagné!<br>";
                return;
            }

            if ($this->plateau->estComplet()) {
                echo "<br>Match nul!<br>";
                return;
            }

            $this->tour++;
        } else {
            echo "Case déjà occupée, essayez à nouveau.<br>";
        }
    }

    public function getGagnant() {
        return $this->gagnant;
    }
}

// Initialisation des joueurs
$joueur1 = new Joueur("Alice", "X");
$joueur2 = new Joueur("Bob", "O");

// Initialisation du jeu
$jeu = new Jeu($joueur1, $joueur2);

// Traitement du formulaire
if (isset($_POST['ligne']) && isset($_POST['colonne'])) {
    $ligne = $_POST['ligne'];
    $colonne = $_POST['colonne'];
    $jeu->jouer($ligne, $colonne);
}
?>