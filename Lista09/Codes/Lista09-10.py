m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(3)] for i in range(3)]
print([[m[len(m) - i - 1][len(m[i]) - j - 1] for j in range(len(m[i]))] for i in range(len(m))])