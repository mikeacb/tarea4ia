# Imprimir números impares del 1 al 50

impar = 0
count = 1

while(count <= 50):
    impar = count % 2
    if (impar == 1):
        print(count)
    count += 1