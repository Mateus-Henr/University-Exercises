# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 20:36:32 2021

@author: Mateus Henrique
"""

soma = 0
produto = 1

while True:
    num = int(input("Digite o número: "))
    
    if num <= 0:
        break
    
    if (num % 2):
        soma += num
    else:
        produto *= num
        
print("Soma dos pares = " + str(soma) + 
      "\nProduto dos ímpares = " + str(produto))