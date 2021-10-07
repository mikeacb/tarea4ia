# Comparar un numero para saber si es par o impar infinitas veces,
# hasta que el usuario decida salir

print("si para continuar, no para salir")
ans = input("¿Desea empezar? ... ")
while (ans == "si"):
    num = int(input("Ingresa un número: "))
    if(num % 2 == 0):
        print(f"{num} es par")
    else:
        print(f"{num} es impar")
    ans = input("¿Desea continuar? ... ")