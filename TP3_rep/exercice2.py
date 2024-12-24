class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    @property
    def nom(self):
        return self.__nom
    @property
    def prenom(self):
        return self.__prenom
    @property
    def age(self):
        return self.__age
    @nom.setter
    def nom(self,nom):
        self.__nom=nom
    @prenom.setter
    def prenom(self,prenom):
        self.__prenom=prenom
    @age.setter
    def age(self,age):
        self.__age=age

if __name__== '__main__':
    p1= Personne("mellali","hiba",19)
    print(p1.nom,"",p1.prenom," a ",p1.age)
    p1.age = 20
    print(p1.age)