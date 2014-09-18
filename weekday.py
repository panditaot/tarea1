import datetime
def Viernes(x):
    x = datetime.date.weekday(x)
    if (x ==4):
        return True
    return False
    
cfecha = input("Escribe una fecha formato dd/mm/yyyy")
dfecha = datetime.datetime.strptime(cfecha, "%d/%m/%Y")
print(Viernes(dfecha))
