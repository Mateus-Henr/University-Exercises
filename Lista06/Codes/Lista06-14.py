# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:13:29 2021

@author: Mateus Henrique
"""

vetor = []
while True: 
    x = str(input("ID e Valor ex(23 4,00): "))
    [vetor.append(x) if int(x.split()[0]) >= 0 else print("Valor total: R${}".format(sum(float(x.split()[1]) for x in vetor)))]
    if int(x.split()[0]) < 0: break