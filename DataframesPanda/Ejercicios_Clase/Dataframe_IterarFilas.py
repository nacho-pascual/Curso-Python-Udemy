'''
Ejercicio
Vamos a mostrar las filas del dataframe words con el siguiente formato: 
"La palabra {identificadorFila} {sí/no} es un palíndromo de {longitud} letras"..'''

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

for row in words.itertuples():
  print("La palabra {}{} es un palíndromo de {} letras".
        format(row[0], "" if row[4] else " no", row[1]))
