# Realizar el problema de cambio de moneda, con módulos

import operator

def pesosADolares(moneda):
    return operator.mul(moneda, 0.048)

def dolaresAPesos(moneda):
    return operator.mul(moneda, 20.66)

def pesosAEuros(moneda):
    return operator.mul(moneda, 0.042)

def eurosAPesos(moneda):
    return operator.mul(moneda, 23.83)

while True:
    ans = int(input("Cambio de moneda:\n1) De pesos a dólares \n2) De dólares a pesos \n3) De pesos a euros \n4) De euros a pesos \nOpción: "))
    if (ans == 1):
        moneda = int(input("\n¿Cuántos pesos a dolares? "))
        print(f"\nResultado: {pesosADolares(moneda)}\n")
    elif (ans == 2):
        moneda = int(input("\n¿Cuántos dólares a pesos? "))
        print(f"\nResultado: {dolaresAPesos(moneda)}\n")
    elif (ans == 3):
        moneda = int(input("\n¿Cuántos pesos a euros? "))
        print(f"\nResultado: {pesosAEuros(moneda)}\n")
    elif (ans == 4):
        moneda = int(input("\n¿Cuántos euros a pesos? "))
        print(f"\nResultado: {eurosAPesos(moneda)}\n")
    else:
        print("\nError\n")