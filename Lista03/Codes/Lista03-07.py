# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:04:17 2021

@author: Mateus Henrique
"""

pares = 0
impares = 0

for x in range(10):
    num = int(input("Digite o " + str(x + 1) + "° número: "))
    
    if (num % 2) == 0:
        pares += 1
    else:
        impares += 1
        
print("Quantidade números pares: " + str(pares) +
      "\nQuantidade números impares: " + str(impares))