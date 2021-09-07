m = [[int(input(f"{i}° lin | {j}° col - Num: ")) for j in range(5)] for i in range(5)]
print([[m[i][j] for j in range(len(m[i])) if (i + 1) != j] for i in range(len(m))])