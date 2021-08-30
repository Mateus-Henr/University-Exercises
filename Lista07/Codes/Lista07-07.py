nums = [int(input("{}° Num: ".format(x + 1))) for x in range(10)]
totais, maiorEMenor = [0, 0], [0, 0]

for x in nums:
    if x % 2 == 0: maiorEMenor[0] = x
    else: maiorEMenor[1] = x

if maiorEMenor[1] % 2 == 0:
    print("Nenhum valor Ã­mpar informado.")
elif maiorEMenor[0] % 2 != 0 or maiorEMenor[0] == 0:
    print("Nenhum valor par informado.")
else:
    for x in nums:
        if x % 2 == 0:
            totais[0] += x
            if x > maiorEMenor[0]:
                maiorEMenor[0] = x
        else:
            totais[1] += x
            if x < maiorEMenor[1]:
                maiorEMenor[1] = x
    
    medias = [(totais[0] / len(nums)), (totais[1] / len(nums))]
    print("Médias\nPares: {}\nÍŒmpares: {}".format(medias[0], medias[1]))
    print("Maior par: {}\nMenor íŒmpar: {}".format(maiorEMenor[0], maiorEMenor[1]))
    print("Pares > média: {}".format([x for x in nums if x > medias[0] and x % 2 == 0]))
    print("\nÍŒmpares < média: {}".format([x for x in nums if x < medias[1] and x % 2 != 0]))