'''
Ejercicio
Del dataframe words, vamos a mostrar las 5 primeras filas, 
las 5 últimas filas y después, vamos a guardar una copia en la variable words_copy.
 Finalmente, vamos a modificar los nombres de las columnas de 
 words_copy a "Longitud", "Principio", "Fin", "Palindromo".'''

def is_palindrome(word): 
  """
  Devuelve si la palabra word es palíndroma.
  Args:
    word: Palabra en formato string
  Returns:
    isPalindrome: Booleano
  """
  word = word.lower()
  l = []
  isPalindrome = True
  for c in word: 
    l.append(c) 
  n = len(l)
  for i in range(int(n / 2)):
    if l[i] != l[n - (i + 1)]: 
      isPalindrome = False
  return isPalindrome

words = ["sol", "ala", "cama", "duro", "bueno", "kayak", "marea", "rotor", "misterio", "acurruca"]
data = {"word": words,
        "length": map(len, words),
        "start": map(lambda w: w[0], words),
        "end": map(lambda w: w[-1], words),
        "isPalindrome": map(is_palindrome, words)}

import pandas as pd
words = pd.DataFrame(data)
words = words.set_index("word")
words.index.names = [None]

#Mostrar 5 ultimas filas
print(words.tail(5))
#Mostrar 5 primeras filas
print(words.head(5))

words_copy = words.copy()
words_copy = words_copy.rename(columns = {"length": "Longitud",
                             "start": "Principio",
                             "end": "Fin",
                             "isPalindrome": "Palindromo"})
print(words_copy)