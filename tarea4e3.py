#Leer 2 números y hacer la resta del mayor menos el menor.
num1 = float(input("Número 1: "))
num2 = float(input("Número 2: "))

if (num1 > num2):
    print("Número 1 menos número 2, ", num1 - num2)
elif (num1 == num2):
    print("Los dos números son iguales")
else:
    print("Número 2 menos número 1, ", num2 - num1)