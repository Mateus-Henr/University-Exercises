m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(2)] for i in range(2)]
d = [(m[x - 1][x - 1] * m[x][x]) - (m[x - 1][len(m) - x - 2] * m[x][len(m) - x - 1]) for x in range(1, len(m))]
print(d[0])