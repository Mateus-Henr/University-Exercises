# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:29:48 2021

@author: Mateus Henrique
"""

num = int(input("Digite o número do mês: "))
meses = ["Janeiro", "Fevereiro", "Março", "Abril", "Maio", "Junho", "Julho", "Agosto", "Setembro", "Outubro", "Novembro", "Dezembro"]
index = num - 1

if (index in range(len(meses))):
    print(meses[index])
else:
    print("Mês inválido")