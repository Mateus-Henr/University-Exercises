# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:13:14 2021

@author: Mateus Henrique
"""
milhos = 1

for x in range(64):
    milhos += 2 ** x

print("Milhos " + str(milhos))