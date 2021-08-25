# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 22:07:07 2021

@author: Mateus Henrique
"""

alturas = [float(input("Altura: ")) for _ in range(10)]
print(list(float(x) for x in alturas if x > (sum(alturas) / 10)))