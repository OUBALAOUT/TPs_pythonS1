class Personne:
    def __init__(self, nom , prenom , age):
        self.__nom = nom 
        self.__prenom = prenom
        self.__age = age
       
    def getnom(self):
        return self.__nom
    def getprenom(self):
        return self.__prenom
    def getage(self):
        return self.__age
  
            
    @property
    def nom(self):
     return self.__nom
    @property
    def prenom(self):
      return self.__prenom
    @property
    def age(self):
     return self.__age 
    @age.setter
    def age(self):
     if self.age<=0:
         self.__age = age
     else:
        False
P = Personne("Brahim" , "Oubalaout", 21)
print(P.nom , P.prenom ,P.age) # setters
