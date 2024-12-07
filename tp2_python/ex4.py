class Personne:

    def __init__(self,nom,prenom,age):
        self.nom=nom
        self.prenom=prenom
        self.age=age

    def se_presenter(self):
        return "Nom:{} ,Prenom:{} ,Age:{}".format(self.nom,self.prenom,self.age)

p1= Personne("alali","aya",20)
print(p1.se_presenter())

class Etudiant(Personne):
    def __init__(self,nom,prenom,age,matricule):
        super().__init__(nom,prenom,age)
        self.matricule=matricule

    def etudier(self):
        return "la personne est un etudiant"
    
e1= Etudiant("raji","ahmed",19,"cp1")
print(e1.etudier())