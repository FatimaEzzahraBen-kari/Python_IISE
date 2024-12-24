class Produit:
    def __init__(self, nom, prix):
        self.__nom = nom  
        self.__prix = prix 

    # Méthodes getter et setter pour le nom
    def get_nom(self):
        return self.__nom

    def set_nom(self, nom):
        self.__nom = nom

    # Méthodes getter et setter pour le prix
    def get_prix(self):
        return self.__prix

    def set_prix(self, prix):
        if prix > 0:  # Vérification que le prix est positif
            self.__prix = prix
        else:
            raise ValueError("Le prix doit être supérieur à 0.")

    # Méthode pour calculer le prix avec remise
    def calculer_prix_remise(self, remise, seuil):
        if self.__prix > seuil:
            prix_avec_remise = self.__prix * (1 - remise / 100)
            return round(prix_avec_remise, 2)  # Retourne un prix arrondi à 2 décimales
        return self.__prix

if __name__ == "__main__":
    produit = Produit("Ordinateur", 1500)
    print(f"Nom du produit : {produit.get_nom()}")
    print(f"Prix initial : {produit.get_prix()} DH")
    
    remise = 10  # Remise de 10%
    seuil = 1000  # Appliquer la remise si le prix est supérieur à 1000
    prix_apres_remise = produit.calculer_prix_remise(remise, seuil)
    print(f"Prix après remise de {remise}% : {prix_apres_remise} DH")
