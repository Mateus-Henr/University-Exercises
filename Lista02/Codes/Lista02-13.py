# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:20:15 2021

@author: Mateus Henrique
"""

num = int(input("Digite um número: "))

if ((num % 3) == 0):
    print("O número " + str(num) + " é múltiplo de 3")
    
if ((num % 7) == 0):
    print("O número " + str(num) + " é múltiplo de 7")
    
if (((num % 3) != 0) and ((num % 7) != 0)):
    print("O número " + str(num) + " não é múltiplo de 7 ou 3")