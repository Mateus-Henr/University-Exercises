while True:
    c, d = [int(x) for x in input("C e D: ").split()]
    e, f = [int(x) for x in input("E e F: ").split()]
    if c > 6 or d > 6 or e > 6 or f > 6: print("Inválido")
    else: break

a = [[int(input(f"{i}° l - {j}° c: ")) for j in range(d)] for i in range(c)]
b = [[int(input(f"{i}° l - {j}° c: ")) for j in range(f)] for i in range(e)]

if d == e:
    g = [[0 for _ in range(f)] for _ in range(c)]
    for i in range(c):
        for j in range(f):
            for x in range(d):
                g[i][j] += a[i][x] * b[x][j]
    print(g)
else: print("O produto matricial não é possível")