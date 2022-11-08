import pandas as pd

#En este caso es importante especificar el nombre de las columnas
x = [1, 2, 3, 4, 5]
y = [2, 4, 6, 8, 10]

data = list(zip(x, y))
print(data)
df5 = pd.DataFrame(data, columns = ["x", "y"])
print(df5)