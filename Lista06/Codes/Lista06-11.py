# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 21:57:36 2021

@author: Mateus Henrique
"""

vetor = [[(int(x) ** 2) if int(x) > 0 else -1 for x in input("Num: ").split()] for _ in range(15)]
print(list(int(x[0]) for x in vetor))