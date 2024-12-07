class Rectangle:

    def __init__(self,largeur,hauteur):
        self.largeur=largeur
        self.hauteur=hauteur

    def calculer_surface(self):
        s=self.largeur*self.hauteur
        return s

    def calculer_perimetre(self):
        p=(self.largeur+self.hauteur)*2
        return p

r1= Rectangle(4,9.5)
print(r1.calculer_surface())
print(r1.calculer_perimetre())