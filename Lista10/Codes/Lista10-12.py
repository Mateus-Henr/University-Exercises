f, nf = input(), ""

for x in range(len(f)):
    if f[x] == " ": nf += "#"
    else: nf += f[x]
        
print(nf)