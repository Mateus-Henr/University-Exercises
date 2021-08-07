# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:24:33 2021

@author: Mateus Henrique
"""

num = int(input("Digite o número: "))

if num > 0:
    fatorial = num
    for x in range(1, num):
        fatorial = fatorial * x
        
print("O fatorial de " + str(num) + " é " + str(fatorial))