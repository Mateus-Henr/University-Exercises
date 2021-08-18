# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:07:50 2021

@author: Mateus Henrique
"""

x = int(input("Digite o valor de x: "))
x = x / 180
sen = x
y = 0

print(sen, end="")
for z in range(1, 16):
    fatorial = 1
        
    for n in range(1, (z + 3 + y)):
        fatorial *= n
        
    if z % 2 == 0:
        sen += (x** (z + 2 + y) / fatorial)
        print(" + {}^{}/{}".format(x ** (z + 2 + y) , (z + 2), fatorial), end="")
    else:
        sen -= (x** (z + 2 + y) / fatorial)
        print(" - {}^{}/{}".format(x ** (z + 2 + y), (z + 2), fatorial), end="")
    y += 1

print("\nSeno = " + str(sen))