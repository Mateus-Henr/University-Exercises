while True:
    qtd = int(input("Qtd: "))
    if qtd > 1000:
        print("Qtd deve ser menor que 1000.")
        continue
    break

vetor, repet = [int(input("Num: ")) for _ in range(qtd)], []

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
    if vetor.count(x) > 1 and not x in repet:
        print("Elemento {} aparece {} veze(s)".format(x, vetor.count(x)))
        for _ in range(vetor.count(x) - 1): repet.append(x)

vetor = [vetor[x] for x in range(len(vetor)) if x == (len(vetor) - 1) or vetor[x] != vetor[x + 1]]

print("Vetor sem repetição: {}".format(vetor))
print("Repetições: {}".format(repet))