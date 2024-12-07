class Livre:
    def __init__(self, titre, auteur, annee_publication):
        self.titre = titre
        self.auteur = auteur
        self.annee_publication = annee_publication

    def __str__(self):
        return f"Le livre :{self.titre}, ecrite par {self.auteur}, publié en {self.annee_publication}"


class Bibliotheque:
    def __init__(self):
        self.list_livre = []

    def ajouter_livre(self, livre):
        if livre not in self.list_livre:
            self.list_livre.append(livre)

    def afficher_livre(self):
        for livre in self.list_livre:
            print(livre)


# Création des livres
l1 = Livre("Candide", "Voltaire", 1759)
l2 = Livre("La boîte à merveilles", "Ahmed Sefrioui", 1954)

# Création de la bibliothèque
b1 = Bibliotheque()

# Ajout des livres à la bibliothèque
b1.ajouter_livre(l1)
b1.ajouter_livre(l2)

# Affichage des livres dans la bibliothèque
b1.afficher_livre()
