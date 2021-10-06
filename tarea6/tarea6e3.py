# Comparar un numero para saber si es par o impar infinitas veces,
# hasta que el usuario decida salir

num = int(input("Número: "))
while True:
    if (num % 2 == 0):
        print(f"{num} es par")
    else:
        print(f"{num} es impar")
    num = int(input("Número: "))