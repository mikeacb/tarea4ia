# Hacer un menú infinito para cambio de moneda:
# 1) De pesos a dólares.
# 2) De dólares a pesos.
# 3) De pesos a euros.
# 4) De euros a pesos.

print("Cambio de moneda:")
print("1) De pesos a dólares \n2) De dólares a pesos \n3) De pesos a euros \n4) De euros a pesos")
while True:
    ans = int(input("Eliga una opción de arriba 1, 2, 3 o 4: "))
    if (ans == 1):
        moneda = int(input("¿Cuántos pesos a dolares? "))
        moneda *= 0.048
        print(moneda)
    elif (ans == 2):
        moneda = int(input("¿Cuántos dólares a pesos? "))
        moneda *= 20.66
        print(moneda)
    elif (ans == 3):
        moneda = int(input("¿Cuántos pesos a euros? "))
        moneda *= 0.042
        print(moneda)
    elif (ans == 4):
        moneda = int(input("¿Cuántos euros a pesos? "))
        moneda *= 23.83
        print(moneda)
    else:
        print("Error")