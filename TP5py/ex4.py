import csv
# Création du fichier CSV
with open("contacts.csv", "w") as fichier_csv:
    content = csv.writer(fichier_csv)
    
    content.writerow(["Nom", "Âge", "Ville"])
    content.writerow(["Alice", "30", "Paris"])
    content.writerow(["Bob", "25", "Lyon"])
    content.writerow(["Claire", "28", "Marseille"])

print("done.")


with open("contacts.csv", "r") as fichier_csv:
    content = csv.reader(fichier_csv)
    next(content)
    for ligne in content:
        print(f"nom: {ligne[1]}")
        #print(f"Nom : {ligne[0]}, Âge : {ligne[1]}, Ville : {ligne[2]}")
    fichier_csv.close()

