# Hacer un programa que lea un numero y diga si el numero es par o impar.

num = float(input("Número: "))

if (num % 2 == 0):
    print(f"{num} es par")
else:
    print(f"{num} es impar")