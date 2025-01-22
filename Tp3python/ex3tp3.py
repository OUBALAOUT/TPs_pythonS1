from ex1tp3 import Cercle,Rectangle
def afficher_surface(formes):
     for forme in formes:
        print(f"Surface: {forme.calculer_surface():.2f}")
    
C1 = Cercle(7)
R1 = Rectangle(7 , 8)
#Liste d'objets Forme
formes = [C1, R1]
#test
print(afficher_surface(formes))
