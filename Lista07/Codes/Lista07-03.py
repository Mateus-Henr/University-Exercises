vetor = [float(input("{}° num: ".format(x + 1))) for x in range(15)]
maiores, menores = [], []

for x in range(len(vetor)):
    if x == 0:
        menor = vetor[x]
        maior = vetor[x]
    else:
        if vetor[x] > maior:
            maior = vetor[x]
        if vetor[x] < menor:
            menor = vetor[x]

for x in range(len(vetor)):
    if vetor[x] == menor:
       menores.append(x)
    if vetor[x] == maior:
       maiores.append(x)

print("Vetor: {}".format(vetor))

print("Maior: {}".format(maior), end=" ")
if len(maiores) > 1: print("Posições: {}".format(maiores))
else: print("Posição: {}".format(vetor.index(maior)))

print("Menor: {}".format(menor), end=" ")
if len(menores) > 1: print("Posições: {}".format(menores))
else: print("Posição: {}".format(vetor.index(menor)))