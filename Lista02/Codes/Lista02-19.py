# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:12:16 2021

@author: Mateus Henrique
"""

def qtdGotas(valorEmMg):
    return str(valorEmMg * 0.04)

idade = int(input("Digite a idade: "))
peso = float(input("Digite o peso: "))

if (idade >= 12):
    if (peso >= 60):
        (print("Receita: \n1000 mg, " + qtdGotas(1000) + " gotas."))
    else:
        print("Receita: \n875 mg, " + qtdGotas(875) + " gotas.")
else:
    if (peso >= 5 and peso < 9):
        print("Receita: \n125 mg, " + qtdGotas(125) + " gotas.")
    elif (peso >= 9 and peso < 16):
        print("Receita: \n250 mg, " + qtdGotas(250) + " gotas.")
    elif (peso >= 16 and peso < 24):
        print("Receita: \n275 mg, " + qtdGotas(275) + " gotas.")
    elif (peso >= 24 and peso < 30):
        print("Receita: \n500 mg, " + qtdGotas(500) + " gotas.")
    elif (peso >= 30):
        print("Receita: \n750 mg, " + qtdGotas(750) + " gotas.")

