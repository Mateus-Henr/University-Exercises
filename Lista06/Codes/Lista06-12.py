alturas = [float(input("Altura: ")) for _ in range(10)]
print(list(float(x) for x in alturas if x > (sum(alturas) / 10)))