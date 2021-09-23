f = [input("Matric: ") for _ in range(300)]
x = len(f)

while x >= 0:
    if input("S ou N: ").lower() == "n":
        f.pop(len(f) - x - 1)
    p = int(input("Guardando para quantas pess: "))
    if p < 4:
        x += p
    x += 1

print(f"Qtd pessoas na fila: {len(p)}")