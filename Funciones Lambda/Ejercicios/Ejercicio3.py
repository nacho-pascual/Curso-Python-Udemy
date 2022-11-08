''' 
Ejercicio 3
Dada una lista de palabras, quédate con filter() con las que tengan más vocales que consonantes. 
Necesitarás una función que devuelva si una palabra tiene más vocales que consonantes.'''

def contador_letras(x):
    vocal=0
    consonante=0
    for i in x:
        if i=="a"or i=="e" or i=="i" or i=="o"or i=="u":
            vocal+=1
        else:
            consonante+=1
    if vocal>consonante:
        return x

words = ["castañaaaa", "astronomía", "masa", "bolígrafo", "mando", "tostada"]
print(list(filter(contador_letras, words)))
