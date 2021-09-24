n, m, nn = input(), {"A": "T", "T": "A", "G": "C", "C": "G", "A": "T"}, ""
for x in n: nn += m[x]
print(nn)