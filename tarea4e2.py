# Teclear 3 números y detectar cual es el menor.

num1 = int(input("Número 1: "))
num2 = int(input("Número 2: "))
num3 = int(input("Número 3: "))

if (num1 > num2 and num1 > num3):
    print(f"El número {num1} es el mayor de los tres")
elif (num2 > num1 and num2 > num3):
    print(f"El número {num2} es el mayor de los tres")
elif (num1 == num2 and num1 == num3):
    print(f"Los tres números son iguales {num1}, {num2}, {num3}")
else:
    print(f"El número {num3} es el mayor de los tres")