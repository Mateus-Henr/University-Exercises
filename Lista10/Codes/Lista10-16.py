n, curr = input(), ""

for x in range(len(n)):
    curr += n[x]
    for _ in range(x - (x * 2)): curr += n[x]

    print(curr)