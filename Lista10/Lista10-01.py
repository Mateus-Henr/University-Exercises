from random import randint

m = [randint(1, 10) for x in range(10)]
v = []

for x in range(len(m)):
    if m[x] not in [v[y][0] for y in range(len(v))]:
        v.append([m[x], 1])
        print(m[x])
    else:
        pos = 0
        for y in range(len(v)):
            if v[y][0] == m[x]:
                pos = y
        v[pos][1] += 1

print(m)
print(v)