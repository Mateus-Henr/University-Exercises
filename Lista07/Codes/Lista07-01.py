valores, total = [float(input("{}� valor: ".format(x + 1))) for x in range(10)], 0
for valor in valores: total += valor
print("Vetor: {}\nM�dia: {}".format(valores, (total / len(valores))))