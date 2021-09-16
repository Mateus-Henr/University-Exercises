n, mt = [], []

while True:
    n = [int(input(f"{x + 1}° {'L' if x == 0 else 'C'}: ")) for x in range(2)]
    if n[0] <= 10 and n[1] <= 10: break
    print("Num <= 10")

m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(n[1])] for i in range(n[0])]

if n[0] == n[1]:
    mt = [[m[j][i] for j in range(len(m[i]))] for i in range(len(m))]
print("m e mt são simétricas" if m == mt else "m e mt não são siméticas")