# -*- coding: utf-8 -*-
"""
Created on Sun Aug  8 22:07:02 2021

@author: Mateus Henrique
"""

razao = int(input("Digite a razão: "))
prim = int(input("Digite o primeiro termo: "))
ref = int(input("Digite o referente n: "))

for n in range(1, (ref + 1)):
    prog = prim + (n - 1) * razao
    print(prog)