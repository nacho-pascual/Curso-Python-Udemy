'''
Dada una lista de palabras, calcula el número de vocales de cada una con map().
'''
def vocal_counter(x):
    contador=0
    for i in x:
        if i in ["a","e","i","o","u"]:
            contador+=1
    return contador



words = ["castaña", "astronomía", "masa", "bolígrafo", "mando", "tostada"]
print(list(map(lambda x: vocal_counter(x),words)))