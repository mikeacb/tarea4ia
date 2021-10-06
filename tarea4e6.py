# Leer dos números y decir si son de signos iguales o diferentes,
# también hay que mencionar si son positivos o negativos

num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

if (num1 >= 0 and num2 >= 0):
    print(f"El primer número {num1} y el segundo número {num2} son positivos, asi que, sus signos son iguales")
elif (num1 < 0 and num2 >= 0):
    print(f"El primer número {num1} es negativo, el segundo número {num2} es positivo, asi que, sus signos son diferentes")
elif (num1 >= 0 and num2 < 0):
    print(f"El primer número {num1} es positivo, el segundo número {num2} es negativo, asi que, sus signos son diferentes")
else:
    print(f"El primer número {num1} y el segundo número {num2} son negativos, asi que, sus signos son iguales")