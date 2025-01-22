def convert_to_int(value):
    try:
        return int(value)
    except ValueError:
        print("\'value\' n'est pas convertible vers \'int\'")
def read_file(filename):
    f = None
    try:
        f = open(filename , 'r')
        return f.read()
    except FileNotFoundError:
        print("file n'exist pas.")
        return None
    finally:
        if f is not None:
            f.close() 
    
file = input("saisir chemin de ficher \n").strip()
n = input("saisir un entier \n")
try:
    print(convert_to_int(n))
    print(read_file(file))
except Exception as e:
   print(e)
    
        