m = [float(input("Elem: ")) for _ in range(int(input("Tam: ")))]
soma = 0
dif = []

for x in m: soma += x
for x in m: dif.append(abs((soma / len(m)) - x))

mini = dif[0]
ind = 0
for x in range(len(dif)):
    if dif[x] < mini:
        mini = dif[x]
        ind = x

print(m[ind])