import csv

# Nom du fichier CSV
nom_fichier = "contacts.csv"

# Fonction pour ajouter un contact
def ajouter_contact():
    nom = input("Nom : ")
    prenom = input("Prénom : ")
    telephone = input("Téléphone : ")

    with open(nom_fichier, mode='a') as fichier:
        writer = csv.writer(fichier)
        writer.writerow([nom, prenom, telephone])
    
    print("Contact ajouté avec succès !")

# Fonction pour afficher tous les contacts
def afficher_contacts():
    try:
        with open(nom_fichier, mode='r') as fichier:
            reader = csv.reader(fichier)
            print("\nTous les contacts :")
            for row in reader:
                print(f"Nom: {row[0]}, Prénom: {row[1]}, Téléphone: {row[2]}")
    except FileNotFoundError:
        print("Le fichier des contacts n'existe pas.")

# Fonction pour rechercher un contact par nom
def rechercher_contact():
    nom_recherche = input("Nom à rechercher : ")
    try:
        with open(nom_fichier, mode='r') as fichier:
            reader = csv.reader(fichier)
            trouve = False
            for row in reader:
                if row[0].lower() == nom_recherche.lower():
                    print(f"Contact trouvé - Nom: {row[0]}, Prénom: {row[1]}, Téléphone: {row[2]}")
                    trouve = True
                    break
            if not trouve:
                print(f"Aucun contact trouvé pour le nom '{nom_recherche}'.")
    except FileNotFoundError:
        print("Le fichier des contacts n'existe pas.")

# Fonction pour supprimer un contact par nom
def supprimer_contact():
    nom_recherche = input("Nom à supprimer : ")
    contacts_restants = []
    contact_supprime = False

    try:
        with open(nom_fichier, mode='r', encoding='utf-8') as fichier:
            reader = csv.reader(fichier)
            for row in reader:
                if row[0].lower() == nom_recherche.lower():
                    contact_supprime = True
                else:
                    contacts_restants.append(row)
        
        if contact_supprime:
            with open(nom_fichier, mode='w', newline='', encoding='utf-8') as fichier:
                writer = csv.writer(fichier)
                writer.writerows(contacts_restants)
            print(f"Le contact '{nom_recherche}' a été supprimé.")
        else:
            print(f"Aucun contact trouvé pour le nom '{nom_recherche}'.")
    except FileNotFoundError:
        print("Le fichier des contacts n'existe pas.")

# Menu principal de l'application
def menu():
    while True:
        print("\n--- Gestion des contacts ---")
        print("1. Ajouter un contact")
        print("2. Afficher tous les contacts")
        print("3. Rechercher un contact")
        print("4. Supprimer un contact")
        print("5. Quitter")
        
        choix = input("Choisissez une option (1-5) : ")
        
        if choix == "1":
            ajouter_contact()
        elif choix == "2":
            afficher_contacts()
        elif choix == "3":
            rechercher_contact()
        elif choix == "4":
            supprimer_contact()
        elif choix == "5":
            print("Merci d'avoir utilisé l'application. À bientôt !")
            break
        else:
            print("Option invalide, veuillez choisir un nombre entre 1 et 5.")
