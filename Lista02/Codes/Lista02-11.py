# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:06:39 2021

@author: Mateus Henrique
"""

def formataNum(num):
    return str("%.0f" % num) if (num).is_integer() else str(num)

a = float(input("Digite o valor de A: "))
b = float(input("Digite o valor de B: "))

if (a > b):
    print("A ('" + formataNum(a) + "') é maior que B ('" + formataNum(b) + "').")
elif (a < b):
    print("A ('" + formataNum(a) + "') é menor que B ('" + formataNum(b) + "').")
else:
    print("A ('" + formataNum(a) + "') é igual a B ('" + formataNum(b) + "').")