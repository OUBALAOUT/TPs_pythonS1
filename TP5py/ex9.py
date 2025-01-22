# Script pour calculer les statistiques d'un fichier texte
def calculer_statistiques(nom_fichier):
    try:
        # Ouvrir le fichier en mode lecture
        with open(nom_fichier, "r", encoding="utf-8") as fichier:
            contenu = fichier.readlines()
        
        # Calculer le nombre total de lignes
        nombre_lignes = len(contenu)
        
        # Calculer le nombre total de mots et de caractères
        nombre_mots = 0
        nombre_caracteres = 0
        for ligne in contenu:
            nombre_mots += len(ligne.split())
            nombre_caracteres += len(ligne)
        
        # Afficher les résultats
        print(f"Statistiques pour le fichier '{nom_fichier}':")
        print(f"- Nombre total de lignes : {nombre_lignes}")
        print(f"- Nombre total de mots : {nombre_mots}")
        print(f"- Nombre total de caractères : {nombre_caracteres}")
    
    except FileNotFoundError:
        print(f"Erreur : Le fichier '{nom_fichier}' n'existe pas.")
    except Exception as e:
        print(f"Une erreur s'est produite : {e}")

# Nom du fichier à analyser
nom_fichier = "fichier.txt"  # Remplacez par le nom de votre fichier
calculer_statistiques(nom_fichier)
