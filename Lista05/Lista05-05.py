# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:14:19 2021

@author: Mateus Henrique
"""

num = int(input("Digite o num: "))

for x in range(1, (num + 1)):
    if x % 3 == 0 and x % 5 == 0:
        print("{} é multiplo de 5 e 3.".format(x))