def n(m):
    x = m%3 or m%2
    if x == 0:
        return True
    else:
        return False
m = int(input("Ingrese un número entero para comprobar si es divisible entre dos y tres "))
print(n(m))
