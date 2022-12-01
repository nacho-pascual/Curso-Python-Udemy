'''
Ejercicio
Implementa el método de instancia .quotient() que devuelva el cociente
Implementa el método de instancia .isInfinite() que devuelva si el denominador es 0 o no
Implementa el método de instancia .simplify() que simplifique la fracción a la fracción irreducible

'''
def bigger(a, b): 
  """
  Devuelve el mayor número de 2 números reales dados.
  Args:
    a: Número real
    b: Número real
  Returns:
    Número real
  """
  if a >= b: 
    return a
  return b

def lower(a, b): 
  """
  Devuelve el menor número de 2 números reales dados.
  Args:
    a: Número real
    b: Número real
  Returns:
    Número real
  """
  if a <= b: 
    return a
  return b

def mcd(a, b): 
  """
  Devuelve el MCD de dos números enteros.
  Args:
    a: Número entero
    b: Número entero
  Returns:
    max: Número entero
  """
  r=0
  max = bigger(a, b) 
  min = lower(a, b)
  while(min > 0):
    r = min
    min = max % min 
    max = r
  return max


class RationalNumber():

  def __init__(self, n, d = 1):
    if type(n) is int and type(d) is int:
      self.numerator = n
      self.denominator = d
    else:
      print("El numerador y el denominador deben ser números enteros")

    
  def __str__(self):
    return "{} / {}".format(self.numerator, self.denominator)

  
  def mathFormat(self):
    from IPython.display import display, Latex
    display(Latex(f"${self.numerator}\\over{self.denominator}$"))


  def quotient(self):
    return self.numerator / self.denominator

  
  def isInfinite(self):
    if self.denominator == 0:
      return True
    return False


  def simplify(self):
    div = mcd(self.numerator, self.denominator)
    self.numerator = int(self.numerator / div)
    self.denominator = int(self.denominator / div)