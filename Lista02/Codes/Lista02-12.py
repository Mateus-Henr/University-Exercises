# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:13:29 2021

@author: Mateus Henrique
"""

from math import sqrt

num = int(input("Digite o número: "))

if (num >= 0):
    print("A raiz quadrada de " + str(num) + " é " + str(sqrt(num)))
else:
    print("O quadrado de " + str(num) + " é " + str(num ** 2))