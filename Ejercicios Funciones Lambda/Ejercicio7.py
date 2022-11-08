'''
Ejercicio 7
Dada una lista de palabras, quédate con reduce() y map() con la palabra con más consonantes. Necesitarás
una función que cuente el número de consonantes de una palabra y otra que dados dos números, devuelva el
mayor.'''
from functools import reduce

def consonant_counter(x):
    contador=0
    for i in x:
        if i not in ["a","e","i","o","u"]:
            contador+=1
    return contador

def mayor(x,y):
    if x>=y:
        return x
    else:
        return y


words = ["castaña", "astronomía", "masa", "bolígrafo", "mando", "tostada"]
x=list(map(lambda x: consonant_counter(x),words))
print(reduce(mayor,x))