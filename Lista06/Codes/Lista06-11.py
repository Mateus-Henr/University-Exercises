vetor = [[(int(x) ** 2) if int(x) > 0 else -1 for x in input("Num: ").split()] for _ in range(15)]
print(list(int(x[0]) for x in vetor))