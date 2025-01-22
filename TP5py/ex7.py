import os
import shutil#copy et archiver les fichiers

# Étape 1 : Créer un fichier texte nommé "journal.txt" et ajouter des lignes
with open("journal.txt", "w") as fichier:
    fichier.write("Aujourd'hui, il fait beau.\n")
    fichier.write("J'ai appris beaucoup de choses en programmation.\n")
    fichier.write("Python est un langage puissant et polyvalent.\n")
print("Fichier 'journal.txt' créé avec succès.")

# Copier le fichier "journal.txt" vers "journal_copie.txt"
shutil.copy("journal.txt", "journal_copie.txt")
print("Fichier 'journal.txt' copié en 'journal_copie.txt'.")

# Déplacer "journal_copie.txt" dans un dossier nommé "archives"
# Créer le dossier "archives" s'il n'existe pas
if not os.path.exists("archives"):
    os.mkdir("archives")

# Déplacer le fichier
shutil.move("journal_copie.txt", os.path.join("archives", "journal_copie.txt"))
print("Fichier 'journal_copie.txt' déplacé dans le dossier 'archives'.")
