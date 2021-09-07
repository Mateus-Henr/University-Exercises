m = [[int(input(f"{i}° lin | {j}° col - Num: ")) for j in range(7)] for i in range(7)]
linha, coluna = [int(x) for x in input("Digite lin | col: ").split()]

if linha < len(m[0]) and coluna < len(m): print("Elemento: {}".format(m[linha][coluna]))
else: print("Não exite a posição informada.")