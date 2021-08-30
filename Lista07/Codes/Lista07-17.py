qtd = int(input("Quantidade de mercadorias: "))
precos = {x:0 for x in range(1, 101)}
qtds = {x:0 for x in range(1, 101)}
total = 0

for _ in range(qtd):
    while True:
        num = int(input("ID: "))
        if num >= 1 and num <= 100:
            precos[num] = float(input("Preço: "))
            qtds[num] = int(input("Quantidade: "))
            total += precos[num] * qtds[num]
            break
        else:
            print("Mercadoria deve ser entre 1 e 100.")

print("\nIDs\n")
[print("| " + str(x).zfill(3) + " |"+ ("\n" if x % 10 == 0 else ""), end="") for x in precos.keys()]
print("\nQuantidade\n")
[print("| {:03d}".format(qtds[x]) + " |" + ("\n" if x % 10 == 0 else ""), end="") for x in qtds.keys()]
print("\nPreços\n")
[print("| {:06.2f}".format(precos[x]) + " |" + ("\n" if x % 10 == 0 else ""), end="") for x in precos.keys()]
print("\nFaturamento mensal: R${:.2f}".format(total))