# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:30:15 2021

@author: Mateus Henrique
"""

for x in range(10):
    num = int(input(str(x + 1) + "° Número: "))
    
    if num < 0:
        print("Negativo não aceito.")
        x -= 1
        continue
    else:
        print("Raiz quadrada de {} é {}".format(num, num ** (1/2)))