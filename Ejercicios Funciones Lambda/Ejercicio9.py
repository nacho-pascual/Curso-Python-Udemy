'''
Ejercicio 9
Dada una lista de números reales, ordénalos con sorted() por valor absoluto de menor a mayor.
'''


numeros = [5,32,-3345,235,-6567,123987,2345,]

x=(list(map(lambda x: abs(x) ,numeros)))
print(sorted(x,reverse=True))

