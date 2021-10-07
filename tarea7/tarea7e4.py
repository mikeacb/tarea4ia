# Calcular en una función el cambio de moneda de pesos a dólares,
# ese valor mandarlo al código llamador y
# hacer la conversión de dólares a euros,
# Imprimir los pesos, dólares y euros.

def pesosADolares(moneda):
    return moneda * 0.048

cambio = float(input("¿Cuántos pesos desea convertir? "))
llamada = pesosADolares(cambio)
euros = llamada * 0.87
print(f"\nPesos: {cambio}\n")
print(f"Dólares: {llamada}\n")
print(f"Euros: {euros}\n")