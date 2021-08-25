# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:03:53 2021

@author: Mateus Henrique
"""

a, vetor = float(input("A: ")), []

for _ in range(30):
    exec('x = float(input("Num: "))\nvetor.append(x)\na *= x')

print("Prod: {}, {}".format(a, ("par" if a % 2 == 0 else "ímpar")))
