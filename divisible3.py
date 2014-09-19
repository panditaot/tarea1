def n(m):
    x = m%3
    if x == 0:
        return True
    else:
        return False
m = int(input("Ingrese un número entero para comprobar si es divisible entre tres "))
print(n(m))
