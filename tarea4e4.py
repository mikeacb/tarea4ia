# Hacer una suma,
# si el resultado está en un rango de 1 a 100 imprimir resultado,
# si no mandar un mensaje de error.

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))
res = num1 + num2
if (res > 0 and res <= 100):
    print(f"El resultado es {res}")
else:
    print("Error")