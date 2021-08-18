# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:41:08 2021

@author: Mateus Henrique
"""

razao = int(input("Digite a razão: "))
ref = int(input("Digite o referente n: "))
k = int(input("Digite k: "))

for n in range(1, (ref + 1)):
    prog = k * razao**(n - k)
    print(str(prog))