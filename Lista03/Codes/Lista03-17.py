# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:37:30 2021

@author: Mateus Henrique
"""

resultado = 1
y = 0

for x in range(1, 51):
    
    if x == 1:
        y += 1
        print(str(y), end="")
    else:
        y += 2
        resultado += (y / x)
        print(" + " + str(y) + "/" + str(x), end="")

print("\nResultado = " + str(resultado))

