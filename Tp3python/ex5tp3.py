class Employe:
    def __init__(self, nom, prenom, salaire):
        self.nom = nom
        self.prenom = prenom
        self.salaire = salaire

class Manager(Employe):
    def __init__(self, nom, prenom, salaire):
        super().__init__(nom, prenom, salaire)
        self.employes_supervises = []

    def ajouter_employe(self, employe):
        self.employes_supervises.append(employe)

    def afficher_employes(self):
        print(f"Employés supervisés par {self.prenom}:")
        for employe in self.employes_supervises:
            print(f"- {employe.prenom} {employe.nom}")

# Exemple d'utilisation
manager = Manager("OUBALAOUT", "BRAHIM", 15000)
employe1 = Employe("SAKI", "Mohamed", 5000)
employe2 = Employe("ALAOUI", "KHALID", 5000)
manager.ajouter_employe(employe1)
manager.ajouter_employe(employe2)
manager.afficher_employes()