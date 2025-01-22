from abc import ABC
class Vehecule:
    def __init__(self, marque , modele, annee):
        self.marque = marque
        self.modele = modele
        self.annee = annee 
        
    def afficher_info(self):
        return f"Marque {self.marque}, Modele : {self.modele}, Annee de fabrication: {self.annee}"
    
    def __str__(self):
        return self.afficher_info()
    
class Moteur:
    def __init__(self, puissance, type_moteur):
        self.puissance = puissance
        self.type_moteur = type_moteur
        
    def afficher_moteur(self):
        return f"Puissance: {self.puissance}, type_moteur: {self.type_moteur}"
    def __str__(self):
        return self.afficher_info()
class Voiture(Vehecule,Moteur):
    def __init__(self,nombre_de_places, marque, modele, annee, puissance, type_moteur):
        Vehecule.__init__(self,marque, modele, annee)
        Moteur.__init__(self,puissance, type_moteur)
        self.nombre_de_places = nombre_de_places
        
    def afficher_info(self):
        return f"nombre de place est : {self.nombre_de_places} {Vehecule.afficher_info(self)}{Moteur.afficher_moteur(self)}"
    def __str__(self):
        return self.afficher_info()
class Moto(Vehecule,Moteur):
    def __init__(self,type_moto, marque, modele, annee, puissance, type_moteur):
        Vehecule.__init__(self,marque, modele, annee)
        Moteur.__init__(self,puissance, type_moteur)
        self.type_moto = type_moto
    def afficher_info(self):
        return f"type de moto est :{self.type_moto}{Vehecule.afficher_info(self)}Moteur:{Moteur.afficher_moteur(self)}"
    def __str__(self):
        return self.afficher_info()
#test
V = Voiture(4,"Mercedes benz","AMG", 2024,300,"ESSENCE")
print(V)
M = Moto("Sport","Mercedes benz","AMG", 2025,200,"ELECTRIQUE")
print(M)