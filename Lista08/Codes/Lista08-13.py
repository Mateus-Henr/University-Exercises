m = [[int(input(f"{i + 1}° lin | {j + 1}° col - Num: ")) for j in range(5)] for i in range(3)]
vetorSL = [[] for _ in range(len(m))]

for i in range(len(m)):
    vetorSL[i].append(m[i][0])
    for j in range(len(m[i])):
        vetorSL[i][0] += m[i][j]

[print(f"{x + 1}° lin - Soma: {vetorSL[x][0]}") for x in range(len(vetorSL))]
print(f"Vetor: {vetorSL}")