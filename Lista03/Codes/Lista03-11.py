# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:35:23 2021

@author: Mateus Henrique
"""

valores = input("Digite os 20 números: ")

for i in range(20):
    num = int(valores.split(" ")[i])
    
    print("------------")
    for j in range(num):
        print(str(num) + " x " + str(j + 1) + " = " + str(num * (j + 1)))
    print("------------")