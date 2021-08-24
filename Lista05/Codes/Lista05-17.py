# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:11:24 2021

@author: Mateus Henrique
"""
total = 0

while True:
    num = int(input("Número pedido: "))
    
    if num == 0:
        break
        
    input("Data pedido: ")
    preco = float(input("Preço unitário: "))
    qtd = int(input("Quantidade: "))
    total += qtd * preco

print("Valor total: R${:.2f}".format(total))
    