# Imprimir números impares del 1 al 100

impar = 0
for i in range(0, 101):
    impar = i % 2
    if (impar == 1):
        print(i)