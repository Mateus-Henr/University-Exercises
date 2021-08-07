# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:58:58 2021

@author: Mateus Henrique
"""

a = float(input("Digite o valor de a: "))
b = float(input("Digite o valor de b: "))
c = float(input("Digite o valor de c: "))

valores = [a, b, c]
valores.sort(reverse=True)

print("Números em ordem decrescente: ")
for valor in valores:
    print(str(("%.0f" % valor) if (valor).is_integer() else valor), end = ", ")
    