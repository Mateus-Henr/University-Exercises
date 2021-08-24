# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 20:08:52 2021

@author: Mateus Henrique
"""

vetor = [int(x) for x in input("Digite os elementos: ").split()]
print(sum(vetor[i] for i in range(len(vetor)) if i % 2 != 0))