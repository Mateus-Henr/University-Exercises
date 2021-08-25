# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 20:08:52 2021

@author: Mateus Henrique
"""

vetor = [int(input("Num: ")) for x in range(int(input("Qtd: ")))]
print(sum([i for i in vetor if i % 2 == 0]))