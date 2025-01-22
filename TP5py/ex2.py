#t = input("saisir trois phrases :\n")
content=[]
for i in range(1, 4):
    ligne = input("Phrase  : ")
    content.append(ligne)


with open("phrases.txt", "w") as fichier:
    for ligne in content:
        fichier.write(ligne + "\n")
    
    