'''Crear una función que dado un número entero y el número de cifras que debe tener, 
rellene con ceros a la izquierda hasta completar el número de cifras indicado.
'''
def rellenar_dia_mes(a):
    if a<=10:
        return f"{a:02d}"


def rellenar_año(a):
    if a<=10:
        return f"{a:04d}"
    elif a<=100:
        return f"{a:04d}"
    elif a<=1000:
        return f"{a:04d}"
    else:
        return f"{a}"

def es_bisiesto(year):
	return not year % 4 and (year % 100 or not year % 400)



class date():
    def __init__(self, day=1, month=1, year=1):
        self.day = day
        self.month = month
        self.year = year
    def __str__(self) -> str:
        return f"{rellenar_dia_mes(self.day)} / {rellenar_dia_mes(self.month)} / {rellenar_año(self.year)} "

    def isLeap(self):
        if es_bisiesto(self.year) ==True:
            return print(f"El año {self.year} es bisiesto")
        else:
            return print(f"El año {self.year} no bisiesto")

prueba=date(1,2,1999)
print(prueba.isLeap())