vetor1, vetor2 = [[float(input(str(z + 1) + "° vetor - Num: ")) for _ in range(5)] for z in range(2)]
vetor3 = [vetor1[x] + vetor2[x] for x in range(5)]
print(vetor3)