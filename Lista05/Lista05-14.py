# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 10:16:28 2021

@author: Mateus Henrique
"""

n1 = int(input("Primeiro termo: "))
n2 = int(input("Segundo termo: "))

n = int(input("Loop: "))

for x in range(n):
    if x % 2 == 0:
        gerado = n1 + n2
    else:
        gerado = n1 - n2
            
    print("Número gerado: " + str(gerado))
    
    n1 = n2
    n2 = gerado