v1 = [int(input("{}° num: ".format(x + 1))) for x in range(10)]
v2 = [v1[x] for x in range(len(v1) - 1, -1, -1)]
print(v2)