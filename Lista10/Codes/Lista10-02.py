l1, l2 = [[int(input("Elem: ")) for _ in range(int(input(f"{x + 1}° Tam: ")))] for x in range(2)]
li = []

for x in range(len(l1) if len(l1) > len(l2) else len(l2)):
    if x < len(l1): li.append(l1[x])
    if x < len(l2): li.append(l2[x])

print(li)