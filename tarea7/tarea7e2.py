# Hacer un menú infinito para las 4 operaciones aritméticas básicas,
# cada operación se realizará en una función y
# se mandará como parámetro los valores necesarios
# 1) Suma.
# 2) Resta.
# 3) Multiplicación.
# 4) División.

def suma(num1, num2):
    return num1 + num2

def resta(num1, num2):
    return num1 - num2

def multi(num1, num2):
    return num1 * num2

def division(num1, num2):
    return num1 / num2

print("Operaciones aritméticas:")
print("1) Suma \n2) Resta \n3) multiplicación \n4) División")
while True:
    ans = int(input("Eliga una opción de arriba 1, 2, 3 o 4: "))
    if (ans == 1):
        print("Suma")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(suma(num1, num2))
    elif (ans == 2):
        print("Resta")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(resta(num1, num2))
    elif (ans == 3):
        print("Multiplicación")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(multi(num1, num2))
    elif (ans == 4):
        print("División")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(division(num1, num2))
    else:
        print("Error")