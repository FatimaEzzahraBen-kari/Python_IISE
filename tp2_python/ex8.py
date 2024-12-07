class Personne:
    def __init__(self, nom, prenom, age):
        self.nom = nom
        self.prenom = prenom
        self.age = age
        self.amis = []  # Liste pour stocker les amis

    def se_presenter(self):
        return "Nom:{} ,Prenom:{} ,Age:{}".format(self.nom,self.prenom,self.age)

    def ajouter_ami(self, ami):
        #Ajoute un ami à la liste d'amis si ce n'est pas déjà le cas.
        if ami not in self.amis:
            self.amis.append(ami)
            print(f"{ami.prenom} a été ajouté comme ami.")
        else:
            print(f"{ami.prenom} est déjà dans la liste des amis.")

    def afficher_amis(self):
        #Affiche la liste des amis.
        if not self.amis:
            return "Cette personne n'a pas encore d'amis."
        else:
            amis_str = ", ".join([f"{ami.prenom} {ami.nom}" for ami in self.amis])
            return f"Amis de {self.prenom} : {amis_str}"


# Exemple d'utilisation

# Création de personnes
p1 = Personne("Alali", "Aya", 20)
p2 = Personne("Raji", "Ahmed", 19)
p3 = Personne("El Mahi", "Sara", 21)

# Présentation
print(p1.se_presenter())  # "Nom: Alali, Prénom: Aya, Âge: 20"

# Ajout d'amis
p1.ajouter_ami(p2)  # "Ahmed a été ajouté comme ami."
p1.ajouter_ami(p3)  # "Sara a été ajouté comme ami."
p1.ajouter_ami(p2)  # "Ahmed est déjà dans la liste des amis."

# Affichage des amis
print(p1.afficher_amis())  # "Amis de Aya : Ahmed Raji, Sara El Mahi"
print(p2.afficher_amis())  # "Cette personne n'a pas encore d'amis."
