# Hacer la suma de n números

num = int(input("Número: "))
res = 0

if (num != 0):
    for i in range(num + 1):
        res += i
    print(res)
else:
    print("Error")