qtd = int(input("Qtd funcion�rios: "))
p = [{"pes": 10, "maos": 15, "ambos": 30, "total:": 0} for _ in range(qtd)]

for x in range(qtd):
    print(f"{x + 1}� funcion�rio")
    p[x]["pes"] *= int(input("P�s: "))
    p[x]["maos"] *= int(input("M�os: "))
    p[x]["ambos"] *= int(input("P�s e m�os: "))
    p[x]["total"] = (p[x]["pes"] + p[x]["maos"] + p[x]["ambos"]) / 2.0

[print(f"{x + 1}� funcion�rio: R${p[x]['total']}") for x in range(len(p))]