# Hacer la suma de n números

cantidad = int(input("¿Cuántos números desea sumar?: "))
suma = 0

for i in range(cantidad):
    numero = int(input("Número: "))
    suma += numero
print(suma)
    