# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:24:13 2021

@author: Mateus Henrique
"""

print("Números ímpares de 100 a 200")

for num in range(100, 201):
    if (num % 2) == 1:
        print(str(num), end=", ")