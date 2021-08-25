c = []
while True:
    y = str(input("Conta, saldo: "))
    if float(y.split()[0]) < 0: break
    else: c.append([z for z in y.split()])
[print("Conta: R${:.2f}, Saldo: R${:.2f}, {}".format(float(x[0]), (float(x[1]) - float(x[0])), ("+" if float(x[1]) > float(x[0]) else "-"))) for x in c]
print("Qtd Clien: {}, Negat(%): {:.2f}%".format(len(c), (sum([1 for x in c if float(x[1]) < float(x[0])]) / len(c) * 100)))
print("Agência: R${:.2f}, Negat: {}".format(sum(float(x[0]) for x in c), sum([1 for x in c if float(x[1]) < float(x[0])])))