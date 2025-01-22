with open("exemple.txt", "r") as fichier:
    content = fichier.readlines()
    
numero = 1
for ligne in content:
    print(numero, ligne)
    numero += 1
   ## while content:
       # print(conte
        
