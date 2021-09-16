m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(4)] for i in range(4)]
print([[m[i][len(m) - j - 1] for j in range(len(m[i])) if i < j] for i in range(len(m))])