vetor = [int(input("Num: ")) for x in range(25)]
n = int(input("Posição: "))
print(vetor[n] if n < len(vetor) else "Posição inexistente.")