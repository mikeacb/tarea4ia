# Hacer un menú infinito para cambio de moneda,
# cada operación se realizará en una función
# y se mandará como parámetro el valor de pesos, dólares o euros.
# 1) De pesos a dólares.
# 2) De dólares a pesos.
# 3) De pesos a euros.
# 4) De euros a pesos.

def pesosADolares(moneda):
    return moneda * 0.048

def dolaresAPesos(moneda):
    return moneda * 20.66

def pesosAEuros(moneda):
    return moneda * 0.042

def eurosAPesos(moneda):
    return moneda * 23.83

while True:
    ans = int(input("Cambio de moneda:\n1) De pesos a dólares \n2) De dólares a pesos \n3) De pesos a euros \n4) De euros a pesos \nOpción: "))
    if (ans == 1):
        moneda = int(input("¿Cuántos pesos a dolares? "))
        print(f"Resultado: {pesosADolares(moneda)}\n")
    elif (ans == 2):
        moneda = int(input("¿Cuántos dólares a pesos? "))
        print(f"Resultado: {dolaresAPesos(moneda)}\n")
    elif (ans == 3):
        moneda = int(input("¿Cuántos pesos a euros? "))
        print(f"Resultado: {pesosAEuros(moneda)}\n")
    elif (ans == 4):
        moneda = int(input("¿Cuántos euros a pesos? "))
        print(f"Resultado: {eurosAPesos(moneda)}\n")
    else:
        print("Error")