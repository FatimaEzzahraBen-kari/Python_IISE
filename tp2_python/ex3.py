class CompteBancaire:
    
    def __init__(self,titulaire,solde):
        self.titulaire= titulaire
        self.solde=solde
    
    def deposer(self,montant):
        self.solde+=montant
    def retirer(self,montant):
        if self.solde>=montant:
            self.solde-=montant
        else:
            print("Montant insuffisant!!")
        return self.solde
    
    def afficher_solde(self):
        return "le solde actuel est: {}".format(self.solde)
        
#instanciation du premier objet
cb1 = CompteBancaire("alaoui ahmed", 9000)
print(cb1.retirer(2000))
print(cb1.afficher_solde())
#instanciation du deuxième objet
cb2 = CompteBancaire("amjad kawtar", 8000)
print(cb2.deposer(3000))
print(cb2.afficher_solde())