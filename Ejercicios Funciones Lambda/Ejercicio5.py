''' 
Dada una lista de palabras, quédate con reduce() con la palabra más larga. Necesitarás una función que
compare dos palabras y devuelva la que tenga mayor longitud.
'''
from functools import reduce

def longitud(x,y):
    if len(x) >= len(y):
        return x
    else:
        return y

words = ["castaña", "astronomía", "masa", "bolígrafo", "mando", "tostada"]
print(reduce(longitud,words))