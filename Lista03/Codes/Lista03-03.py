# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:27:43 2021

@author: Mateus Henrique
"""

maxNum = - float("inf")
minNum = float('inf')

for I in range(0, 10):
    x = int(input("Digite o número: "))
    if x > maxNum:
        maxNum = x
    elif x < minNum:
        minNum = x
print(minNum)
print(maxNum)

print("Maior Número: " + str(maxNum) + 
      "\nMenor número: " + str (minNum))