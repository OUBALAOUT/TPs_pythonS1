import os

# Nom du fichier à renommer
ancien_nom = "phrases.txt"
nouveau_nom = "anciennes_phrases.txt"

# Étape 1 : Renommer le fichier
os.rename(ancien_nom, nouveau_nom)
print(f"Le fichier '{ancien_nom}' a été renommé en '{nouveau_nom}'.")

# Étape 2 : Supprimer le fichier renommé
os.remove(nouveau_nom)
print(f"Le fichier '{nouveau_nom}' a été supprimé.")
