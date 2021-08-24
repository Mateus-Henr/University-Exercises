# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 00:19:23 2021

@author: Mateus Henrique
"""

c = []
while True: 
    y = input("Conta, saldo: ")
    [c.append(y) if x[0] >= 0 else print("Conta: {}, Saldo: {}, {}".format(x[0], x[1], ("+" if float(x[1]) > float(x[0]) else "-"))) for x in c]
    if y.split()[0] < 0: break
print("Qtd Clien: {}, Negat: {}".format(len(c), ) (for x in c))