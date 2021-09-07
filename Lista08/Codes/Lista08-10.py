a, b = [[[int(input(f"{'a' if x == 0 else 'b'}-{i}° lin | {j}° col - Num: ")) for j in range(4)] for i in range(3)] for x in range(2)]
s = 0
for x in [[(a[i][j] + b[i][j]) for j in range(len(a[i]))] for i in range(len(a))]: s += x[0] + x[1] + x[2] + x[3]
print(s)