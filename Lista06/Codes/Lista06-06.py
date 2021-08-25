vetor = [int(input("Num: ")) for x in range(int(input("Qtd: ")))]
print(sum([i for i in vetor if i % 2 == 0]))