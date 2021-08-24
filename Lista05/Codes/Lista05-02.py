# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 11:56:45 2021

@author: Mateus Henrique
"""

salario = float(input("Salário: "))

final = salario + (salario * 0.02)

if final >= 0 and final <= 500:
    print("Nenhum crédito")
elif final >= 501 and final <= 1000:
    print("30% do valor do salário médio")
elif final >= 1001 and final <= 3000:
    print("40% do valor do salário médio")
elif final >= 3001:
    print("50% do valor do salário médio")

