# Comparar un numero para saber si es par o impar infinitas veces,
# hasta que el usuario decida salir


while True:
    num = int(input("Número: "))
    if (num % 2 == 0):
        print(f"{num} es par")
    else:
        print(f"{num} es impar")