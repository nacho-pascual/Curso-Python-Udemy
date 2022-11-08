'''
Ejercicio 8
Dada una lista de números enteros, calcula el número anterior con map().
'''

numeros = [5,32,345,235,567,123987,2345,]

print(list(map(lambda x: x-1 ,numeros)))