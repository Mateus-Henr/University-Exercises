# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:46:01 2021

@author: Mateus Henrique
"""

a = float(input("Valor real: "))
b = int(input("Valor inteiro: "))
temp = 0

while (a * b) != temp:
    temp += a
    print(temp)