# Sacar el promedio de n unidades

num = int(input("Número de datos: "))
suma = 0
count = 0

for i in range(num):
    dato = int(input("Número: "))
    suma += dato
    count += 1

print(f"Promedio: {suma/count}")