# a) Realice un programa que calcule e imprima el
# resultado del Trinomio cuadrado perfecto de:
# (a2 + b)2, Donde la fórmula es: a2 + 2ab + b2 y
# los valores son: a = 3, b = 4

import operator

def trinomio(a, b):
    return operator.pow(operator.pow(a, 2), 2) + operator.mul(operator.pow(a, 2), b) + operator.mul(operator.pow(a, 2), b) + operator.pow(b, 2)

a = 3
b = 4

print("a)\nTrinomio -> (a^2 + b)^2\nValores -> a=3, b=4\nFórmula -> a^2 + 2ab + b^2\n")
print(f"Resultado: {trinomio(a, b)}")