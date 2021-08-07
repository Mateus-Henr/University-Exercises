# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:12:22 2021

@author: Mateus Henrique
"""

print("Múltiplos de 5 de 0 a 500")

for num in range(1, 505):
    if (num % 5) == 0:
        print(str(num), end=", ")