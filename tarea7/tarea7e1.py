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

print("Cambio de moneda:")
print("1) De pesos a dólares \n2) De dólares a pesos \n3) De pesos a euros \n4) De euros a pesos")
while True:
    ans = int(input("Eliga una opción de arriba 1, 2, 3 o 4: "))
    if (ans == 1):
        moneda = int(input("¿Cuántos pesos a dolares? "))
        print(pesosADolares(moneda))
    elif (ans == 2):
        moneda = int(input("¿Cuántos dólares a pesos? "))
        print(dolaresAPesos(moneda))
    elif (ans == 3):
        moneda = int(input("¿Cuántos pesos a euros? "))
        print(pesosAEuros(moneda))
    elif (ans == 4):
        moneda = int(input("¿Cuántos euros a pesos? "))
        print(eurosAPesos(moneda))
    else:
        print("Error")