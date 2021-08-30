temps = []
menorTemp, maiorTemp = 40, 15
total = acimaMedia = media = 0

while len(temps) < 121:
    inp = float(input("Temp: "))
    
    if inp >= 15 and inp <= 40:
        temps.append(inp)
        if inp > maiorTemp:
            maiorTemp = inp
        if inp < menorTemp:
            menorTemp = inp
        total += inp
    else:
        print("Temperatura entre 15 e 40, inclusive.")
        print("Digite novamente.")

print("Menor temp: {}°".format(menorTemp))
print("Maior temp: {}°".format(maiorTemp))
media = total / len(temps)
print("Temp média: {:.2f}°".format(media))

for x in temps:
    if x > media:
        acimaMedia += 1

print("Qtd temp acima da média: {}".format(acimaMedia))