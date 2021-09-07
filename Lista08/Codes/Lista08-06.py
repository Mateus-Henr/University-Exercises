m, s = [[int(input(f"{i}° lin | {j}° col - Num: ")) for j in range(10)] for i in range(10)], 0
for x in [m[x - 1][x] for x in range(1, len(m))]: s += x
print(s)