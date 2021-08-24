# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:30:41 2021

@author: Mateus Henrique
"""

v3 = []
v1, v2 = [[int(input(str(z + 1) + "° vetor - Num: ")) for _ in range(3)] for z in range(2)]
for x in range(3): 
    v3.append(v1[x])
    v3.append(v2[x])
print(v3)