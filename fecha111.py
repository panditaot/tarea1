import datetime
def cumpleaños(cumple):
    actual = datetime.date.today()
    if((cumple.month, cumple.day)>(actual.month, actual.day)): 
        return print("Tu edad es de {} años". format(actual.year-cumple.year-1))
    return print("Tu edad es de {} años". format(actual.year-cumple.year))

cfecha= input("Ingresa tu fecha de nacimiento (fornato dd/mm/yyyy): ")
dfecha = datetime.datetime.strptime(cfecha, "%d/%m/%Y")
cumpleaños(dfecha)

          
    
