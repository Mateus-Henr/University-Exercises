# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 00:55:14 2021

@author: Mateus Henrique
"""

salario = 500.00

nome = str(input("Digite o nome do vendedor: "))
carrosVend = int(input("Quantidade de carros vendidos: "))
valorTotal = float(input("Valor total das vendas: R$"))

salarioTotal = salario + (carrosVend * 50.00) + (valorTotal * (5 / 100))

print("Salário total de " + nome + " é R$" + str("%.2f" % salarioTotal))