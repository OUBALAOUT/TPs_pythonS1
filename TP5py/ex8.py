try:
    # Tenter d'ouvrir le fichier inexistant.txt
    with open("inexistant.txt", "r", encoding="utf-8") as fichier:
        contenu = fichier.read()
        print("Contenu du fichier :")
        print(contenu)
except FileNotFoundError:
    # Gérer le cas où le fichier n'existe pas
    print("Erreur : Le fichier 'inexistant.txt' n'existe pas.")
