while True:
    qtd = int(input("Qtd: "))
    if qtd > 20:
        print("Qtd deve ser menor que 20.")
        continue
    break

vetor = [int(input("{}° Num: ".format(x + 1))) for x in range(qtd)]

loop = True
while loop:
    loop = False
    for x in range(len(vetor) - 1):
        if vetor[x] > vetor[x + 1]:
            temp = vetor[x]
            vetor[x] = vetor[x + 1]
            vetor[x + 1] = temp
            loop = True

k = int(input())

if k < len(vetor):
    print("K-ésimo elemento: {}".format(vetor[k]))
else:
    print("O vetor não possui o k-ésimo elemento.")