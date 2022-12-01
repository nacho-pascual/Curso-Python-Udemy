'''
Ejercicio
Vamos a implementar los siguientes métodos estáticos:

.sum() dode  𝑝1𝑞1+𝑝2𝑞2=𝑝1𝑞2+𝑝2𝑞1𝑞1⋅𝑞2 
.subract() dode  𝑝1𝑞1−𝑝2𝑞2=𝑝1𝑞2−𝑝2𝑞1𝑞1⋅𝑞2 
.product() dode  𝑝1𝑞1⋅𝑝2𝑞2=𝑝1⋅𝑝2𝑞1⋅𝑞2 
.division() dode  𝑝1𝑞1÷𝑝2𝑞2=𝑝1⋅𝑞2𝑝2⋅𝑞1
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
  