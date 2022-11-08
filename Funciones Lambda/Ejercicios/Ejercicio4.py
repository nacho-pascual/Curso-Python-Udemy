'''
Ejercicio 4
Dada una lista de números enteros, quédate con filter() con los que tengan más de 5 divisores. Necesitarás
una función que devuelva el número de divisores de un número dado.
'''

def divisores(x):
    divisores=0
    for i in range(1,x+1):
        if x % i == 0:
            divisores+=1
    if divisores>5:
        return x

numeros = [5,32,345,235,567,123987,2345,]

print(list(filter(divisores,numeros)))
