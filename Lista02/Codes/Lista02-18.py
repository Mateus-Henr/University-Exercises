# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:02:03 2021

@author: Mateus Henrique
"""

pesos = [0.37, 0.88, 0.38, 2.64, 1.15, 1.17]
planetas = ["Mercúrio", "Vênus", "Marte", "Júpiter", "Saturno", "Urano"]

peso = float(input("Digite o peso: "))
num = int(input("1 - Mercúrio" +
                "\n2 - Vênus" +
                "\n3 - Marte" +
                "\n4 - Júpiter" +
                "\n5 - Saturno" +
                "\n6 - Urano" +
                "\nDigite o número do planeta: "))

index = num - 1

if (index in range(len(pesos))):
    print("O peso terreste ('" + str(peso) + "') em " + planetas[index] + " é " + str(peso * pesos[index]))