class Voiture:

    def __init__(self,marque,modele,annee):
        self.marque= marque
        self.modele=modele
        self.annee=annee
    def afficher_info(self):
        return "Voiture: {} , medele: {} ,d'annee :{}".format(self.marque,self.modele,self.annee)

v1= Voiture("mercedess","G64",2020)
print(v1.afficher_info())
v2= Voiture("clio","C99",2023)
print(v2.afficher_info())