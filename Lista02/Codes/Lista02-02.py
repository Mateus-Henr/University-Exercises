# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:22:07 2021

@author: Mateus Henrique
"""

num1 = float(input("Digite o 1° número: "))
num2 = float(input("Digite o 2° número: "))
soma = num1 + num2

if (soma > 10):
    print("Soma: " + (str("%.0f" % soma) if (soma).is_integer() else str(soma)))