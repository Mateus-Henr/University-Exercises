f, a, n, s = input("Frase: ").split(), input("Antiga: "), input("Nova: "), ""

if a in f:
    for x in f:
        space = " " if s != "" else ""
        if x == a: s += space + n
        else: s += space + x
    print(s)
else: print("Não encontrado.")