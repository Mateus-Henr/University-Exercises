vetor = [float(input("{}° num: ".format(x + 1))) for x in range(20)]

for x in range(len(vetor)):
    if x == 0:
        menor = vetor[x]
        maior = vetor[x]
    else:
        if vetor[x] > maior:
            maior = vetor[x]
        if vetor[x] < menor:
            menor = vetor[x]

print("Vetor: {}\nMenor valor: {}\nMaior valor: {}".format(vetor, menor, maior))