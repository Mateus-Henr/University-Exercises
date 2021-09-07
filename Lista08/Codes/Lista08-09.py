a = [[int(input(f"{i}° lin | {j}° col - Num: ")) for j in range(4)] for i in range(3)]
b = [[(a[i][j] * 3) for j in range(len(a[i]))] for i in range(len(a))]
print(b)