class Vehicule:

    def __init__(self,marque,modele,annee):
        self.marque=marque
        self.modele=modele
        self.annee=annee

    def afficher_info(self):
        print("Vehicule de la marque",self.marque,"modele:",self.modele,"fabriqué dans l annee",self.annee)

class Moteur:
    def __init__(self,puissance,type_moteur):
        self.puissance=puissance
        self.type_moteur=type_moteur

    def afficher_moteur(self):
        print("Moteur avec une puissance",self.puissance,"chevaux, de type:",self.type_moteur)

class Voiture(Vehicule,Moteur):

    def __init__(self,marque,modele,annee,puissance,type_moteur,nombre_de_places):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.nombre_de_places=nombre_de_places

    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print("le nombre de place :",self.nombre_de_places)

class Moto(Vehicule,Moteur):

    def __init__(self,marque,modele,annee,puissance,type_moteur,type_moto):
        Vehicule.__init__(self,marque,modele,annee)
        Moteur.__init__(self,puissance,type_moteur)
        self.type_moto=type_moto
    
    def afficher_info(self):
        Vehicule.afficher_info(self)
        Moteur.afficher_moteur(self)
        print("type de moto :",self.type_moto) 

#créer une instance de voiture
v1 = Voiture("Toyota","Corola",2022,140,"Essence",5)
v1.afficher_info()

#créer une instance de moto
m1 = Moto("Yamaha","MT-07",2021,74,"Essence","Sport")
m1.afficher_info()
