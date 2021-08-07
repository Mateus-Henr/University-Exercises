# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:37:42 2021

@author: Mateus Henrique
"""

num = int(input("Digite o valor: "))

if (num is None):
    print("O número é nulo.")

else:
    if (num > 0):
        print("O número " + str(num) + " é positivo.")
    elif (num < 0):
        print("O número " + str(num) + " é negativo.")
    else:
        print("O número " + str(num) + " é zero.")