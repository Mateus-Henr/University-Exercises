m = [[] for _ in range(10)]

for x in range(len(m)):
    m[x].append(input("Matrícula (aascccnnn): "))
    sx = int(input("Sexo (0 - fem / 1 - masc): "))
    m[x].append("Feminino" if sx == 0 else "Masculino" if sx == 1 else "-")
    m[x].append(m[x][0][3:6])
    m[x].append(int(input("CR: ")))

maior = m[0]
for x in m:
    if x[3] > maior[3]: maior = x

print(f"Cód: {maior[2]}\nCR: {maior[3]}")