# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:03:53 2021

@author: Mateus Henrique
"""

vetor = []
a = float(input("A: "))

for _ in range(30):
    x = float(input("Num: "))
    vetor.append(x)
    a *= x

print("O produto é " + str(a))
if a % 2 == 0:
    print("O produto é par.")
else:
    print("O produto é ímpar.")