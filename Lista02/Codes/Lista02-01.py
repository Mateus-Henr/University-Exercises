# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:18:43 2021

@author: Mateus Henrique
"""

num = float(input("Digite o número: "))

if (num > 20):
    print("Número: " + (str("%.0f" % num) if (num).is_integer() else str(num)))