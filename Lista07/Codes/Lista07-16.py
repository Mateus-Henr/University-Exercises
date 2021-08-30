from random import randint

valores, somatorio = [randint(1, 100) for _ in range(100)], 0

print("S = ", end=" ")
for x in range(len(valores) // 2):
    somatorio += (valores[x] - valores[(len(valores) - 1 - x)]) ** 3
    if x != 0:
        print(" + ", end="")
    print("({} - {})³".format(valores[x], valores[(len(valores) - 1 - x)]), end="")

print("\nS = {}".format(somatorio))