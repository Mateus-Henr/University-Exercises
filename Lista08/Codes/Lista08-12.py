m, s = [[int(input(f"{i}° lin | {j}° col - Num: ")) for j in range(5)] for i in range(4)], 0
for x in [x for y in m for x in y]: s += x
print(s)