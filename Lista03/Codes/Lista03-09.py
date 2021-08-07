# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 18:14:52 2021

@author: Mateus Henrique
"""

total = 0
qtdNums = 0

while True:
    num = int(input("Digite o número: "))
    
    if num == -1:
        break
    
    if num >= 0:
        qtdNums += 1
        total += num
        

print("A média é " + str(total / qtdNums))