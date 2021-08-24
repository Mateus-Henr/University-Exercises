# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 09:08:12 2021

@author: Mateus Henrique
"""

chico = 1.50
juca = 1.10
anos = 0

while juca <= chico:
    chico += 0.02
    juca += 0.03
    anos += 1

print("Demorará " + str(anos) + " anos.")