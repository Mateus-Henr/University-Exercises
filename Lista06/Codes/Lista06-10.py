vetor = [[str(x) for x in input("Digite o nome e nota: (Ex: M 10)").split()] for i in range(3)]
maior = max([float(vetor[x][1]) for x in range(len(vetor))])
print("Maior valor: {}, {}".format(list(str(x[0]) for x in vetor if int(x[1]) == maior)[0], maior))