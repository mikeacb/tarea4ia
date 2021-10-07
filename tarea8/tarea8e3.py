# Realizar el problema de las áreas, con módulos

import operator

def suma(num1, num2):
    return operator.add(num1, num2)

def resta(num1, num2):
    return operator.sub(num1, num2)

def multi(num1, num2):
    return operator.mul(num1, num2)

def division(num1, num2):
    return operator.truediv(num1, num2)

while True:
    ans = int(input("Operaciones aritméticas:\n1) Suma \n2) Resta \n3) multiplicación \n4) División \nOpción: "))
    if (ans == 1):
        print("\nSuma")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"\nResultado: {suma(num1, num2)}\n")
    elif (ans == 2):
        print("\nResta")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"\nResultado: {resta(num1, num2)}\n")
    elif (ans == 3):
        print("\nMultiplicación")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"\nResultado: {multi(num1, num2)}\n")
    elif (ans == 4):
        print("\nDivisión")
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        print(f"\nResultado: {division(num1, num2)}\n")
    else:
        print("\nError\n")