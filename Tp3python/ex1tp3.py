from abc import abstractmethod
import math
class Forme:
    def __init__(abc):
        pass
    @abstractmethod
    def calculer_surface(self):
        pass
class Cercle(Forme):
    def __init__(self, rayon):
        self.rayon = rayon
    def calculer_surface(self): 
        return self.rayon**2 * math.pi
    
class Rectangle(Forme):
    def __init__(self , larg, h):
        self.larg  = larg
        self.h = h
    def calculer_surface(self): 
        return self.larg * self.h
    
def afficher_surface(formes):
     for forme in formes:
        print(f"Surface de {forme} : {forme.calculer_surface():.2f}")
    
C1 = Cercle(7)
R1 = Rectangle(7 , 8)
#Liste d'objets Forme
formes = [C1, R1]
#test
print(afficher_surface(formes))
        