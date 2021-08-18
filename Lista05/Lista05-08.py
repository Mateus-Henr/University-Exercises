# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:23:10 2021

@author: Mateus Henrique
"""

maior = menor = loop = 0

while True:
    num = float(input("Número: "))
    
    if num == -1:
        break
    if loop == 0:
        maior = num
        menor = num
    else:
        if num > maior:
            maior = num
        if num < menor:
            menor = num
    loop += 1

print("Maior " + str(maior) + "\nMenor " + str(menor))