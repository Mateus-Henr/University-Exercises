vetorA = []

while len(vetorA) < 30:
    inp = int(input("Vetor A - Num: "))
    if inp in vetorA:
        print("Número {} já no vetor.".format(inp))
    else:
        vetorA.append(inp)

vetorB = [int(input("Vetor B - Num: ")) for _ in range(30)]
x = int(input("Valor de X: "))

if vetorA.count(x) == 1:
   print("Vetor A - Posição elemento igual a X: {}".format(vetorA.index(x)))
   print("Vetor B - Elem: {}".format(vetorB[vetorA.index(x)]))
else:
    print("X não existe no vetor.")
    

