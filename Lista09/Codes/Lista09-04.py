m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(4)] for i in range(4)]
print([m[len(m) - x - 1][x] for x in range((len(m) - 1), -1, -1)])