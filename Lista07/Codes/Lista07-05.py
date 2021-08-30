vetor = [int(input("{}° num: ".format(x + 1))) for x in range(15)]
primos = {}

for x in range(len(vetor)):
    naoPrimo = False
    for y in range(3, vetor[x]):
        if vetor[x] % y == 0:
            naoPrimo = True
    if not naoPrimo and vetor[x] >= 0:
        primos[x] = vetor[x]

[print("Num: {} - Posição: {}".format(primos[x], x)) for x in primos.keys()]