# Hacer un programa que realice una suma y
# le pregunte al usuario si quiere seguir sumando números,
# si la respuesta es no,
# imprimir el resultado de todos los números sumados

print("si para continuar, no para salir")
ans = input("¿Desea continuar? ... ")
temp = 0
while (ans == "si"):
    if (ans == "si"):
        num1 = int(input("Número 1: "))
        num2 = int(input("Número 2: "))
        suma = num1 + num2
        temp += suma
        print("si para continuar, no para salir")
        ans = input("¿Desea continuar? ... ")
print(f"\nSuma total: {temp}")