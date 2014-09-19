def promedio(n1, n2, n3, n4, n5, n6, n7, n8, n9, n10):
    x = (n1 +n2+n3+n4+n5+n6+n7+n8+n9+n10)/10
    return x
n1 = float(input("Teclea el primer número de 10 números que teclearás"))
n2=float(input("Teclea el segundo"))
n3=float(input("Teclea el tercero"))
n4=float(input("Teclea el cuarto"))
n5=float(input("Teclea el quinto"))
n6=float(input("Teclea sexto"))
n7=float(input("Teclea el séptimo"))
n8=float(input("Teclea el octavo"))
n9=float(input("Teclea el noveno"))
n10=float(input("Teclea el décimo"))
x = promedio(n1, n2,n3,n4,n5,n6,n7,n8,n9,n10)
print("El promedio es {}". format(x))
