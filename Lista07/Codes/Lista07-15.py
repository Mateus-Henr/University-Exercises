while True:
    qtd = int(input("Qtd: "))
    if qtd > 1000:
        print("Qtd deve ser menor que 1000.")
        continue
    break

vetor = [int(input("Num: ")) for x in range(qtd)]
v = []

loop = True
while loop:
    loop = False
    for x in range(len(vetor) - 1):
        if vetor[x] > vetor[x + 1]:
            temp = vetor[x]
            vetor[x] = vetor[x + 1]
            vetor[x + 1] = temp
            loop = True

for x in vetor:
    if vetor.count(x) > 1 and not x in v:
        print("Elemento {} aparece {} veze(s)".format(x, vetor.count(x)))
        v.append(x)

print("Vetor: {}".format(vetor))