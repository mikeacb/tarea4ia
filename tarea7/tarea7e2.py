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

while True:
    ans = int(input("Operaciones aritméticas:\n1) Suma \n2) Resta \n3) multiplicación \n4) División \nOpción: "))
    if (ans == 1):
        print("Suma")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"Resultado: {suma(num1, num2)}\n")
    elif (ans == 2):
        print("Resta")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"Resultado: {resta(num1, num2)}\n")
    elif (ans == 3):
        print("Multiplicación")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"Resultado: {multi(num1, num2)}\n")
    elif (ans == 4):
        print("División")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"Resultado: {division(num1, num2)}\n")
    else:
        print("Error")