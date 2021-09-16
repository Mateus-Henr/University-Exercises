m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(10)] for i in range(10)]
print([[m[i][j] for j in range(len(m[i])) if j != i] for i in range(len(m))])