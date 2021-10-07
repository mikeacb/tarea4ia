# Declarar una lista tamaño 10 y
# sumar solo los números que sean diferentes a 0

numeros = list(range(1, 11))
suma = 0

for i in numeros:
    num = int(input("Número: "))
    numeros[i] = num
    if (numeros[i] != 0):
        suma += numeros[i]

print(f"Suma: {suma}")