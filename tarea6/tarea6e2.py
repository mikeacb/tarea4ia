# Imprimir las tablas de multiplicar en un rango del 1 al 10

tabla = int(input("Que tabla del 1-10 deseas hacer: "))
count = 1

if (tabla > 0 and tabla <= 10):
    while (count <= 10):
        res = tabla * count
        count += 1
        print(res)
else:
    print("Error")
