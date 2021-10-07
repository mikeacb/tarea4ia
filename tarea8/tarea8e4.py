# Realizar el problema de las operaciones aritméticas, con módulos

import operator
import math

def triangulo(base, altura):
    return operator.truediv(operator.mul(base, altura), 2)

def cuadrado(lado):
    return pow(lado, 2)

def rectangulo(base, altura):
    return operator.mul(base, altura)

def circulo(radio):
    return operator.mul(math.pi, math.pow(radio, 2))

while True:
    ans = int(input("Áreas de figuras:\n1) Triangulo \n2) Cuadrado \n3) Rectángulo \n4) Circulo \nOpción: "))
    if (ans == 1):
        print("\nTriángulo")
        num1 = int(input("Base: "))
        num2 = int(input("Altura: "))
        print(f"\nÁrea: {triangulo(num1, num2)}\n")
    elif (ans == 2):
        print("\nCuadrado")
        num1 = int(input("Lado: "))
        print(f"\nÁrea: {cuadrado(num1)}\n")
    elif (ans == 3):
        print("\nRectangulo")
        num1 = int(input("Base: "))
        num2 = int(input("Altura: "))
        print(f"\nÁrea: {rectangulo(num1, num2)}\n")
    elif (ans == 4):
        print("\nCirculo")
        num1 = float(input("Radio: "))
        print(f"\nÁrea: {circulo(num1)}\n")
    else:
        print("\nError\n")