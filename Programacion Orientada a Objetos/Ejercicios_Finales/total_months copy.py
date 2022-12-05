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

def total_month_days(month,year):
    año_bisiesto= not year % 4 and (year % 100 or not year % 400)
    if año_bisiesto ==True and month==2:
        return 29
    if año_bisiesto ==False and month==2:
        return 28
    if month==1 or  month==3 or  month==5 or  month==7 or  month==8 or  month==10 or  month==12:
        return 31
    else:
        return 30

class date():
    def __init__(self, day=1, month=1, year=1):
        self.day:int = day
        self.month:int = month
        self.year:int = year
        
        
    def __str__(self):
        return f"{rellenar_dia_mes(self.day)} / {rellenar_dia_mes(self.month)} / {rellenar_año(self.year)} "

    def isLeap(self):
        if es_bisiesto(self.year) ==True:
            return print(f"El año {self.year} es bisiesto")
        else:
            return print(f"El año {self.year} no bisiesto")
    def totalMonthDay(self):
        return(f"El mes {self.month} tiene {total_month_days(self.month,self.year)} dias")


    @property
    def monthName(self):
        months = ["January", "February", "March", "April", "May", "June",
    "July", "August", "September", "October", "November", "December"]
        return months[self.month - 1]