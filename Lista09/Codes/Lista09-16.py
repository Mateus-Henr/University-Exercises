m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(int(input("C: ")))] for i in range(int(input("L: ")))]
mi = [[]]
if len(m) == len(m[0]):
    mi = [[m[len(m) - j - 1][len(m) - i - 1] if i == j else -m[len(m) - j - 1][len(m) - i - 1] for j in range(len(m[i]))] for i in range(len(m))]
print("m e mi são simétricas" if m == mi else "m e mi não são siméticas")