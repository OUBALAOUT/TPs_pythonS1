def get_positive_integer():
    while 1:
     try:
        num = int(input("saisir un val\n"))
        if num>0:
            print("valide",num)
            break
     except ValueError:
         print("saisir un entier")
get_positive_integer()