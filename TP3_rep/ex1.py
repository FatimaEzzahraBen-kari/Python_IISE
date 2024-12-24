from abc import ABC, abstractmethod
import math
class Forme(ABC):

    @abstractmethod
    def calculer_surface():
        raise NotImplementedError("method not implemented!")
    
class Cercle(Forme):
    def __init__(self,r):
        self.r=r

    def calculer_surface(self):
        return f"La surface du cercle est :{math.pi*self.r**2}"

class Rectangle(Forme):
    def __init__(self,long,larg):
        self.long=long
        self.larg=larg
    def calculer_surface(self):
        return f"La surface du Rectangle est :{(self.long + self.larg)*2}"
    
C1= Cercle(3)
print(C1.calculer_surface())
r1=Rectangle(5,2)
print(r1.calculer_surface())
