print("saisir trois phrases :\n")
content=[]
for i in range(1, 4):
    ligne = input("Phrase  : ")
    content.append(ligne)
add = input("d'autre phrases ?")
if add=="oui":
    ligne = input("Phrase  : ")
    content.append(ligne)
elif add=="non":
    print("see you")
     

with open("phrases.txt", "w") as fichier:
    for ligne in content:
        fichier.write(ligne + "\n")
    
    