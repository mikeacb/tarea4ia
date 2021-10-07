# Hacer un menú infinito para cambio de moneda:
# 1) De pesos a dólares.
# 2) De dólares a pesos.
# 3) De pesos a euros.
# 4) De euros a pesos.

while True:
    ans = int(input("Cambio de moneda:\n1) De pesos a dólares \n2) De dólares a pesos \n3) De pesos a euros \n4) De euros a pesos \nOpción: "))
    if (ans == 1):
        moneda = int(input("¿Cuántos pesos a dolares? "))
        print(f"\nResultado: {moneda * 0.048}\n")
    elif (ans == 2):
        moneda = int(input("¿Cuántos dólares a pesos? "))
        print(f"\nResultado: {moneda * 20.66}\n")
    elif (ans == 3):
        moneda = int(input("¿Cuántos pesos a euros? "))
        print(f"\nResultado: {moneda * 0.042}\n")
    elif (ans == 4):
        moneda = int(input("¿Cuántos euros a pesos? "))
        print(f"\nResultado: {moneda * 23.83}\n")
    else:
        print("Error")