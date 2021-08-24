# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:36:18 2021

@author: Mateus Henrique
"""

a = b = c = d = e = maiorOtimo = menorRuim = totalIdade = maiorPess = 0

for _ in range(1):
    idade = int(input("Idade: "))
    nota = str(input("Nota: "))
    
    if nota == "A":
        a += 1
        if idade > maiorOtimo:
            maiorOtimo = idade
            
    elif nota == "B":
        b += 1
    elif nota == "C":
        c += 1
    elif nota == "D":
        d += 1
        totalIdade += idade
        if idade < menorRuim:
            menorRuim = idade
            
    elif nota == "E":
        e += 1
        if idade > maiorPess:
            maiorPess = idade
    else:
        print("Inválida.")

total = a + b + c + d + e

print("Qtd ótimo: {}".format(a) +
      "\nDiferença bom e regular em %: {}".format(((b / total) * 100) - ((d / total) * 100)) +
      "\nMédia ruim: {}%".format(totalIdade / d) + 
      "\nNotas pessimas em % e maior idade: {}%, {}".format((e / total) * 100, maiorPess) +
      "\nDiferença maior idade ótima e menor ruim: {}".format(maiorOtimo - menorRuim))
