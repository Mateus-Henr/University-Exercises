m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(2)] for i in range(2)]
mi = [[m[len(m) - j - 1][len(m) - i - 1] if i == j else -m[len(m) - j - 1][len(m) - i - 1] for j in range(len(m[i]))] for i in range(len(m))]
print("m e mt são simétricas" if m == mi else "m e mi não são siméticas")