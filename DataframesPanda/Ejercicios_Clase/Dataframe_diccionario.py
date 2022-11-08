import pandas as pd

data = {"x": [1, 2, 3, 4, 5], "y": [2, 4, 6, 8, 10]}
df1 = pd.DataFrame(data = data)
print(df1)

#Ejemplo modificando el nombre de las filas

df3 = pd.DataFrame(data = data, index = ["obs1", "obs2", "obs3", "obs4", "obs5"])
print(df3)