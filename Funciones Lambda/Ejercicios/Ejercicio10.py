'''
Ejercicio 10
Dada una lista de palabras, ordénalos con sorted() por número de consonates de mayor a menor.
'''

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

print(sorted(words,key=consonant_counter,reverse=True))