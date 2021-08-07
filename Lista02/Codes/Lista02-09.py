# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:47:48 2021

@author: Mateus Henrique
"""

def formataNum(num):
    return str("%.0f" % num) if (num).is_integer() else str(num)

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o segundo número: "))
        
if (num1 % num2) == 0:
     print("O 1° número '" + formataNum(num1) + "' é divisível pelo 2° número '" + formataNum(num2) + "'.")
if (num2 % num1) == 0:
     print("O 2° número '" + formataNum(num2) + "' é divisível pelo 1° número '" + formataNum(num1) + "'.")
if (((num2 % num1) != 0) and ((num2 % num1) != 0)):
     print("Os números digitados '" + formataNum(num1) + "' e '" + formataNum(num2) + "' não são divisíveis um pelo outro.")
