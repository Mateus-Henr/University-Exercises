# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 21:10:34 2021

@author: Mateus Henrique
"""

qtdNum = 0

for _ in range(15):
    if int(input("Num: ")) > 30:
        qtdNum += 1

print("Quantidade nums maiores que 30 = " + str(qtdNum))