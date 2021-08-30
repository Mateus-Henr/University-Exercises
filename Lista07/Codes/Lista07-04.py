vetor = [float(input("{}° num: ".format(x + 1))) for x in range(30)]
for x in range(len(vetor)):
    if x % 2 == 0:
        vetor[x] = 0
print(vetor)