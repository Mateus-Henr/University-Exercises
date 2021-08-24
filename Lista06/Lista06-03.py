# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:33:29 2021

@author: Mateus Henrique
"""

vetor = [int(input("Num: ")) for _ in range(4)]
revertido = list(reversed(vetor))
print("{}\n{}".format(vetor, revertido))