# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:17:38 2021

@author: Mateus Henrique
"""
soma = qtdNums = 0

while True:
    num = int(input("Número: "))
    
    if num < 0:
        break
    
    if num % 3 == 0:
        soma += num
        qtdNums += 1

print("Média mútiplos de 3 = " + str(soma / qtdNums))