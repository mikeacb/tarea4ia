# b) Escriba un programa que lea la distancia entre
# dos ciudades en metros y visualice su equivalente
# en kilómetros y metros. Por ejemplo: 2300 metros
# equivalen a 2 kilómetros y 300 metros.

import operator

def metros(distancia):
    return operator.mod(distancia, 1000)

def kilometros(distancia, metros):
    return operator.truediv(operator.sub(distancia, metros), 1000)

distancia = float(input("Distancia: "))

mtrs = metros(distancia)

print(f"Kilometros: {kilometros(distancia, mtrs)}\nMetros: {mtrs}")