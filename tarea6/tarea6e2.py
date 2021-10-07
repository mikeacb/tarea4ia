# Imprimir las tablas de multiplicar en un rango del 1 al 10

count1 = 1
while (count1 <= 10):
    count2 = 1
    while(count2 <= 10):
        print(f"{count1} * {count2} = {count1 * count2}\n")
        count2 += 1
    count1 += 1