# Investigar algún modulo en internet y utilizarlo en un programa

from colorama import Fore, Style

# init(convert= True)

metros = float(input("Dame tu altura: "))
if (metros <= 1.50):
    print(Fore.RED + "Persona de baja estatura")
elif (metros > 1.50) and (metros <= 1.70):
    print(Fore.YELLOW + "Persona de media estatura")
else:
    print(Fore.GREEN + "Persona alta")
