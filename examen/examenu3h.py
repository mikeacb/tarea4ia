# h) Intercambiar los valores de a y b,
# por ejemplo:
# a = 1
# b = 2
# Después del cambio:
# a = 2
# b = 1

a = int(input("Número para a: "))
b = int(input("Número para b: "))
print(f"Valores iniciales: \na = {a}\nb = {b}")
c = a
a = b
b = c
print(f"Valores ya intercambiados: \na = {a}\nb = {b}")