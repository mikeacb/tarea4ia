# Comparar un numero para saber si es par o impar infinitas veces,
# hasta que el usuario decida salir

num = int(input("Número o 0 (cero) para salir: "))
while (num != 0):
    if (num % 2 == 0):
        print(f"{num} es par")
    else:
        print(f"{num} es impar")
    num = int(input("Número o 0 (cero) para salir: "))