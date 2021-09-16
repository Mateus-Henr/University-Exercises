m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(3)] for i in range(3)]
print([[m[len(m) - j - 1][i] for j in range(len(m[i]))] for i in range(len(m))])