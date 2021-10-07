# Investigar algún módulo nativo en Python y
# realizar un programa referente al módulo investigado

import math
import operator

radio = int(input("Radio del círculo: "))
print(f"Área: {round(math.pi * operator.pow(radio, 2))}")