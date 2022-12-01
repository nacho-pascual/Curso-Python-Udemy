'''
Ejercicio
Vamos a configurar los siguientes métodos de clase:

.random() que se encarga de crear un objeto aleatorio de la clase RationalNumber.
.zero() que se encarga de crear el objeto de la clase RationalNumber que tiene por numerador 0 y denominador 1.
.one() que se encarga de crear el objeto de la clase RationalNumber que tiene por numerador 1 y denominador 1.
.fromRealNumber() que dado un número real se encarga de buscar su expresión en racional. 
Por ejemplo, dado 5.4, tendremos que crear el objeto RationalNumber con numerador 54 y denominador 10. 
Investiga el método math.modf() para este caso.'''

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
  r = 0
  max = bigger(abs(a), abs(b)) 
  min = lower(abs(a), abs(b))
  while(min > 0):
    r = min
    min = max % min 
    max = r
  return max

def helper(n, d):
  print("{} / {} = {}".format(n, d, n / d))


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


  @staticmethod
  def sum(p, q):
    num = p.numerator * q.denominator + q.numerator * p.denominator
    den = p.denominator * q.denominator
    helper(num, den)


  @staticmethod
  def subtract(p, q):
    num = p.numerator * q.denominator - q.numerator * p.denominator
    den = p.denominator * q.denominator
    helper(num, den)


  @staticmethod
  def product(p, q):
    num = p.numerator * q.numerator
    den = p.denominator * q.denominator
    helper(num, den)


  @staticmethod
  def division(p, q):
    num = p.numerator * q.denominator
    den = p.denominator * q.numerator
    helper(num, den)


  @classmethod
  def random(cls):
    import random
    num = random.randrange(-100, 100)
    den = random.randrange(-100, 100)
    while den == 0:
      den = random.randrange(-100, 100)
    return cls(num, den)

  
  @classmethod
  def zero(cls):
    return cls(0)


  @classmethod
  def one(cls):
    return cls(1)


  @classmethod
  def fromRealNumber(cls, f):
    import math
    num = f
    den = 1
    d, i = math.modf(num)
    while d != 0:
      num *= 10
      den *= 10
      d, i = math.modf(num)
    num = int(num)
    den = int(den)
    return cls(num, den)
