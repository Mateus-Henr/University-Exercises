qtd = int(input("Qtd funcionários: "))
p = [{"pes": 10, "maos": 15, "ambos": 30, "total:": 0} for _ in range(qtd)]

for x in range(qtd):
    print(f"{x + 1}° funcionário")
    p[x]["pes"] *= int(input("Pés: "))
    p[x]["maos"] *= int(input("Mãos: "))
    p[x]["ambos"] *= int(input("Pés e mãos: "))
    p[x]["total"] = (p[x]["pes"] + p[x]["maos"] + p[x]["ambos"]) / 2.0

[print(f"{x + 1}° funcionário: R${p[x]['total']}") for x in range(len(p))]