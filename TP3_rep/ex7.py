from abc import ABC,abstractmethod
class Vehicule(ABC):

    @abstractmethod
    def deplacer(self):
        raise NotImplementedError("On peut pas implementer une methode abstraite!")

class Voiture(Vehicule):

    def deplacer(self):
        print("La voiture se deplace avec le diesel")

class Bicyclette(Vehicule):

    def deplacer(self):
        print("La Bicyclette se deplace en pédalant avec les pieds")

v1= Voiture()
v1.deplacer()
b1= Bicyclette()
b1.deplacer()