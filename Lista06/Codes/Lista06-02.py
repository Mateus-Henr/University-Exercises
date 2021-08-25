# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:12:29 2021

@author: Mateus Henrique
"""

vetor = [int(input("Num: ")) for _ in range(10)]
num = int(input("Num: "))
[print("Menor: {}".format(n) if n < num else "Igual: {}".format(n) if n == num else "Maior: {}".format(n)) for n in vetor]
    