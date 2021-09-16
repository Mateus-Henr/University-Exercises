m, p = [[int(input(f"{i}° l - {j}° c: ")) for j in range(4)] for i in range(4)], 1
for x in [y for x in [[m[i][j] for j in range(len(m[i])) if i > j] for i in range(len(m))] for y in  x]: p *= x
print(p)