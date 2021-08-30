n = int(input("Qtd pessoas: "))
rendas = [float(input("Renda {}° pessoa: R$".format(x + 1))) for x in range(n)]
totalRendas = 0

for x in rendas: totalRendas += x

print("Média das rendas: R${}".format(totalRendas / len(rendas)))

    