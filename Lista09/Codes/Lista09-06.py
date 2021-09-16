p = [[] for _ in range(50)]

for x in range(len(p)):
    print(f"\n{x + 1}° planta")
    p[x].append(input("Nome: "))
    p[x].append(int(input("Estoque ideal: ")))
    p[x].append(int(input("Estoque: ")))
    
for x in range(len(p)):
    if (p[x][1] > p[x][2]): print(f"Nome: {p[x][0]}\nPrecisa comprar: {p[x][1] - p[x][2]}")
        