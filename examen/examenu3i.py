# i) Declarar una lista de tamaño n con símbolos,
# pedir al usuario algún símbolo a buscar,
# contar cuantas veces aparece en la lista dicho
# símbolo e imprimir el resultado.

simbolos = ["!", "·", "#", "$", "%", "&", "/", "(", ")", "=", "+", "-", "*", "^", "?", "¿", ")", "$", ";", "¬", "~", "|", "@", "#", ";", "]", "[", "*", "`", ">", "€", "{", "!", "}", "$", "_", ".", ":", "¡", "·", "ç", "Ç", "´", "_", "<"]

simbolo = str(input("Símbolo: "))
count = 0
for i in simbolos:
    if(i == simbolo):
        count += 1
if(count != 0):
    print(f"El símbolo {simbolo} se encontró {count} veces")
else:
    print(f"El símbolo {simbolo} no se encontró")