# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:59:08 2021

@author: Mateus Henrique
"""

divisor = 0
resultado = 0

for x in reversed(range(2, 39)):
    divisor += 1
    
    resultado += ((x - 1) + (x)) / divisor
    print(((" + ") if (divisor != 1) else "") + str(x - 1) + "*" + str(x) + "/" + str(divisor), end="")
    
print("\nResultado = " + str(resultado))