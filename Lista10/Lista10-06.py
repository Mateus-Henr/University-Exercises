l = [[input("Nome: "), input("Num: ")] for _ in range(int(input("Tam: ")))]
l = sorted(l, key=lambda contato: contato[0].lower())
op = input("Opção (a ou b): ")

if op.lower() == "a":
    l.append([input("Nome: "), input("Num: ")])
    l = sorted(l, key=lambda contato: contato[0].lower())
if op.lower() == "b":
    n = input("Nome: ")
    if n in [x[0] for x in l]:
        for x in range(len(l)):
            if l[x][0].lower() == n.lower():
                print(f"Nome: {l[x][0]}\nNum: {l[x][1]}")
                break
    else: print("Pessoa não está na agenda.")

print(l)