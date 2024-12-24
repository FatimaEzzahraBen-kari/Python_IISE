class Personne:
    def __init__(self,nom,prenom,age):
        self.__nom = nom
        self.__prenom = prenom
        self.__age = age
    
    def getNom(self):
        return self.__nom
    def setNom(self,nom):
        self.__nom=nom
    def getPrenom(self):
        return self.__prenom
    def setPrenom(self,prenom):
        self.__prenom=prenom
    def getAge(self):
        return self.__age
    def setAge(self,age):
        self.__age=age

if __name__== '__main__':
    p1= Personne("alami","rania",20)
    print(p1.getNom(),"",p1.getPrenom()," a ",p1.getAge())
    p1.setAge(21)
    print(p1.getAge())