notas = []
fAbs = {x:0 for x in range(11)}

while len(notas) < 80:
    nota = float(input("Nota: "))
    
    if nota >= 0 and nota <= 10:
        notas.append(nota)
        fAbs[nota] += 1
    else: print("Nota deve ser entre 0 e 10.")

[print("---", end="") for _ in range(30)]
print()
[print("|   {}  |".format(x), end="") for x in fAbs.keys()]
print()
[print("| {:.2f} |".format(x / len(notas)), end="") for x in fAbs.keys()]
print()
[print("| {:.2f} |".format(fAbs[x]), end="") for x in fAbs.keys()]
print()
[print("---", end="") for _ in range(30)]