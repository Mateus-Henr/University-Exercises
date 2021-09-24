m = [[input("Car: "), float(input("Cons: "))] for _ in range(int(input("Qtd: ")))]
menor = m[0]

for x in range(len(m)):
    if m[x][1] < menor[1]: menor = m[x]

print(f"Carro: {menor[0]}\nViagem: R${((1000 / menor[1]) * 3.50):.2f}")