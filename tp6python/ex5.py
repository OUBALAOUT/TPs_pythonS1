def process_input(val):
    try:
        
      return int(val)/10
    except ValueError:
        print("saisir un entier !!\n")
    except ZeroDivisionError:
        print("division impossible")

cl = input("saisir une valeur: \n")
print(process_input(cl))