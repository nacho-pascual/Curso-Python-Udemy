'''
Ejercicio 1
Crea una función lambda que dado un número entero multiplique por su anterior y su siguiente. Por ejemplo,
si proporcionamos n = 3, nos tendrá que devolver 2 · 3 · 4 = 24.
'''
plus_ant_post=(lambda x:(x-1)*(x)*(x+1))
print(plus_ant_post(5))