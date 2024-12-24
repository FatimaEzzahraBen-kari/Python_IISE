class Employee:

    def __init__(self,nom,prenom,salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

class Manager(Employee):

    def __init__(self,nom,prenom,salaire,list_empl):
        super().__init__(nom,prenom,salaire)
        self.list_empl = list_empl

    def ajouter_employee(self,emp):
        if emp not in self.list_empl:
            self.list_empl.append(emp)
    
    def afficher_employee(self):
        print("--Liste des employees--")
        for emp in self.list_empl:
            print("L''employee: ",emp.nom,"",emp.prenom,"a un salaire de",emp.salaire)
            
emp1= Employee("amar","amine",5000)
emp2= Employee("sadik","aya",4000)
mg1= Manager("alaoui","khalid",6000,[emp1,emp2])
mg1.ajouter_employee(emp1)
mg1.ajouter_employee(emp2)
mg1.afficher_employee()