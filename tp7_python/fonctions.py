import math
import os
from datetime import datetime
def racine_carre(n):
    return math.sqrt(n)

def afficherdatenow():
    return datetime.now()
def repertoire_courant():
    return os.getcwd()