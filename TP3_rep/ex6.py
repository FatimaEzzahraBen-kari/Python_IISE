class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom
        self.__prix = prix

    def getNom(self):
        return self.__nom

    def setNom(self, nom):
        self.__nom = nom

    def getPrix(self):
        return self.__prix

    def setPrix(self, prix):
        self.__prix = prix


class Commande(Produit):
    def __init__(self, nom, prix, quantite):
        super().__init__(nom, prix)
        self.quantite = quantite

    def calculer_total(self):
        return self.getPrix() * self.quantite


class Panier:
    def __init__(self):
        self.list_cmd = []

    def ajouter_cmd(self, cmd):
        self.list_cmd.append(cmd)

    def calculer(self):
        print("-- Total du panier --")
        total_panier = 0
        for cmd in self.list_cmd:
            total_cmd = cmd.calculer_total()
            print(
                f"Produit: {cmd.getNom()}, Prix Unitaire: {cmd.getPrix()} DH, Quantité: {cmd.quantite}, Total: {total_cmd} DH"
            )
            total_panier += total_cmd
        print(f"Total général: {total_panier} DH")


# Exemple d'utilisation
cmd1 = Commande("Téléphone", 1200, 15)
cmd2 = Commande("Casque", 100, 10)

# Créer un panier et ajouter les commandes
panier = Panier()
panier.ajouter_cmd(cmd1)
panier.ajouter_cmd(cmd2)

# Calculer le total
panier.calculer()
