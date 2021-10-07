# Imprimir la tabla de multiplicar en un rango de 1 a 10,
# si el usuario da un numero fuera de ese rango mandar mensaje de error.

tabla = int(input("Que tabla del 1-10 deseas hacer: "))

if (tabla > 0 and tabla <= 10):
    for i in range(1, 11):
        print(f"{tabla} * {i} = {tabla * i}")
else:
    print("Error")