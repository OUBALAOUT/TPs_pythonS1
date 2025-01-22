import json

# Créer un dictionnaire contenant les infos de trois étudiants
etudiants = {
    "etudiant1": {"nom": "Alice", "âge": 20, "note": 85},
    "etudiant2": {"nom": "Bob", "âge": 22, "note": 90},
    "etudiant3": {"nom": "Charlie", "âge": 21, "note": 78},
}

# Enregistrer ce dictionnaire dans un fichier JSON
with open("etudiants.json", "w") as fichier:
    json.dump(etudiants, fichier)

print("Données enregistrées dans 'etudiants.json'.")

# Lire le fichier JSON et afficher les informations
with open("etudiants.json", "r", encoding="utf-8") as fichier:
    etudiants_lus = json.load(fichier)

# Afficher les informations des étudiants
for key, infos in etudiants_lus.items():
    print(f"{key.capitalize()} :")
    print(f"  Nom : {infos['nom']}")
    print(f"  Âge : {infos['âge']}")
    print(f"  Note : {infos['note']}")
    print()
