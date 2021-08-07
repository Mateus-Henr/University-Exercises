# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 01:02:27 2021

@author: Mateus Henrique
"""

resultado = y = 1


print(str(resultado), end="")
for x in range(1, 52):
    y += 2
    if (x % 2) == 0:
        resultado += (1 / (y ** 3))
        print(" + " + "1/" + str(y) + "^3", end="")
    else:
        resultado -= (1 / (y ** 3))
        print(" - " + "1/" + str(y) + "^3", end="")

print("\nResultado = " + str(resultado) +
      "\nResultado de π = " + str(((resultado * 32) ** 1 / 3)))
    