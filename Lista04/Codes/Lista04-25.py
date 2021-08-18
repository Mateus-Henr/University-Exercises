# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:17:54 2021

@author: Mateus Henrique
"""

x = int(input("Digite o valor de x: "))

if x != 4:
    print("O valor de f(x) é " + str(((5 * x) + 3) / (((x**2) - 16)**1/2)))
else:
    print("Divisão por 0.")