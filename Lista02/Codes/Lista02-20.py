# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:32:05 2021

@author: Mateus Henrique
"""

caixa = float(input("Digite o valor em caixa: R$"))
num = int(input("Digite o número da bola sorteada: "))
valorBolas = [0.05, 0.25, 0.10, 0.07, 0.08, 0.05, 0.15, 0.12, 0.03, 0.10]

def alteraCaixa(numBola):
    global caixa, valorBolas
    valorBola = caixa * valorBolas[numBola]
    caixa = caixa - valorBola
    return str("%.2f" % valorBola)

print("Valor restante em caixa: R$" + str("%.2f" % caixa))

if (num in range(len(valorBolas))):
    print("Bola " + str(num) + " - Prêmio R$" + alteraCaixa(num))
    
else:
    print("Número inválido.")
