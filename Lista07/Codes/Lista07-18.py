tempos = [int(input("{}° Corredor - Tempo: ".format(x + 1))) for x in range(10)]
clas = [x for x in tempos]

loop = True
while loop:
    loop = False
    for x in range(len(clas) - 1):
        if clas[x] > clas[x + 1]:
            temp = clas[x]
            clas[x] = clas[x + 1]
            clas[x + 1] = temp
            loop = True

[print("{}° Num: {} - Tempo: {}s".format((x + 1), tempos.index(clas[x]), clas[x])) for x in range(len(clas))]