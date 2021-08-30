while True:
    qtd = int(input("Qtd: "))
    if qtd > 20:
        print("Qtd deve menor que 20.")
        continue
    break

vetor = [int(input("{}° Num: ".format(x + 1))) for x in range(qtd)]
cres = [x for x in vetor]

loop = True
while loop:
    loop = False
    for x in range(len(cres) - 1):
        if cres[x] > cres[x + 1]:
            temp = cres[x]
            cres[x] = cres[x + 1]
            cres[x + 1] = temp
            loop = True

decres = [cres[x] for x in range(len(cres) - 1, -1, -1)]
print("Vetor: {}".format(vetor))
print("Vetor crescente: {}".format(cres))
print("Vetor decrescente: {}".format(decres))