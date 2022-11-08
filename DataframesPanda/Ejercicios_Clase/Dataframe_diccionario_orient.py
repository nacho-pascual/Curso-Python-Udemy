import pandas as pd

#Lo interesante de este método es que podemos crear un dataframe a partir de un diccionario
#donde cada clave represente una fila (observación) diferente, 
# gracias al parámetro orient. 

""" Si no ponemos el "Index" como orient va a dar error
"""
d = {"fila1": [1, 4, 7],
     "fila2": [2, 5, 8],
     "fila3": [3, 6, 9]}

df = pd.DataFrame.from_dict(d, orient = "index", columns = ["A", "B", "C"])
print(df)