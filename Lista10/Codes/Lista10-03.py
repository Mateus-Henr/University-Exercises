m, soma, dif = [float(input("Elem: ")) for _ in range(int(input("Tam: ")))], 0, []

for x in m: soma += x
for x in m: dif.append(abs((soma / len(m)) - x))

mini = [dif[0], 0]
for x in range(len(dif)):
    if dif[x] < mini[0]: mini = [dif[x], x]

print(m[mini[1]])