m = [[int(input(f"{i}° l - {j}° c: ")) for j in range(10)] for i in range(10)]
temp = m[7]
m[7] = m[1]
m[1] = temp

temp = [m[j][9] for j in range(len(m))]
for i in range(len(m[9])): m[i][9] = m[i][3]
for i in range(len(m[3])): m[i][3] = temp[i]

temp = [m[(len(m)) - x - 1][x] for x in range((len(m) - 1), -1, -1)]
for x in range((len(m) - 1), -1, -1): m[len(m) - x - 1][x] = m[len(m) - x - 1][len(m) - x -1]
for x in range(len(m)): m[x][x] = temp[x]
print(m)