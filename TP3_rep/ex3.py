from abc import ABC, abstractmethod

# Classe abstraite Forme
class Forme(ABC):
    @abstractmethod
    def calculer_surface(self):
        pass

# Classe Rectangle
class Rectangle(Forme):
    def __init__(self, largeur, hauteur):
        self.largeur = largeur
        self.hauteur = hauteur

    def calculer_surface(self):
        return self.largeur * self.hauteur

# Classe Cercle
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon

    def calculer_surface(self):
        import math
        return round(math.pi * (self.rayon ** 2), 2)

# Fonction affichant les surfaces
def afficher_surface(formes):
    for forme in formes:
        print(f"Surface de {type(forme).__name__} : {forme.calculer_surface()}")

# Exemple d'utilisation
if __name__ == "__main__":
    rectangle = Rectangle(3, 6)  # Rectangle de largeur 5 et hauteur 10
    cercle = Cercle(4)           # Cercle de rayon 7

    formes = [rectangle, cercle]
    afficher_surface(formes)
