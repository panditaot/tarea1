def n(m):
    x = m%2
    if x == 0:
        return True
    else:
        return False
m = int(input("Ingrese un número entero para comprobar si es divisible entre dos"))
print(n(m))
