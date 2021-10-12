# Hacer la sumatoria de n números

cantidad = int(input("¿Cuántas sumatorias desea hacer?: "))

for i in range(cantidad):
    numero = int(input("Número: "))
    res = 0
    for x in range(numero + 1):
        res += x
    print(f"La sumatoria del número {numero} es: {res}")