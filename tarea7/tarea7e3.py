import math
# Hacer un menú infinito para calcular el área
# de un triángulo, cuadrado, rectángulo y circulo,
# cada operación se realizará en una función
# y se mandará como parámetro los valores necesarios
# 1) Triangulo.
# 2) Cuadrado.
# 3) Rectángulo.
# 4) Circulo.

def triangulo(base, altura):
    return (base * altura) / 2

def cuadrado(lado):
    return pow(lado, 2)

def rectangulo(base, altura):
    return base * altura

def circulo(radio):
    return math.pi * math.pow(radio, 2)

while True:
    ans = int(input("Áreas de figuras:\n1) Triangulo \n2) Cuadrado \n3) Rectángulo \n4) Circulo \nOpción: "))
    if (ans == 1):
        print("Triángulo")
        num1 = int(input("Base: "))
        num2 = int(input("Altura: "))
        print(f"Área: {triangulo(num1, num2)}\n")
    elif (ans == 2):
        print("Cuadrado")
        num1 = int(input("Lado: "))
        print(f"Área: {cuadrado(num1)}\n")
    elif (ans == 3):
        print("Rectangulo")
        num1 = int(input("Base: "))
        num2 = int(input("Altura: "))
        print(f"Área: {rectangulo(num1, num2)}\n")
    elif (ans == 4):
        print("Circulo")
        num1 = float(input("Radio: "))
        print(f"Área: {circulo(num1)}\n")
    else:
        print("Error")

