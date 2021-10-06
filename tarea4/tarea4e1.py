# (1) Escriba un programa que pida la estatura de una persona,
# si la altura es menor o igual a 1.50 mts envié el mensaje 
# “Persona baja de estatura”, si la altura está entre 
# 1.51 y 1.70 mts escriba el mensaje “Persona de estatura media” 
# y si la altura es mayor a 1.71 escriba “Persona alta”.

metros = float(input("Dame tu altura: "))
if (metros <= 1.50):
    print("Persona de baja estatura")
elif (metros > 1.50) and (metros < 1.70):
    print("Persona de media estatura")
else:
    print("Persona alta")


