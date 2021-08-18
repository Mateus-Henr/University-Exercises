# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:24:53 2021

@author: Mateus Henrique
"""

valor = float(input("Digite o valor do produto: "))
desconto = valor * 9/100

print("Desconto: R$" + str("%.2f" % desconto) + 
      "\nProduto com desconto: R$" + str("%.2f" % (valor - desconto)))