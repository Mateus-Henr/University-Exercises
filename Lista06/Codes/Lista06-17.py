# -*- coding: utf-8 -*-
"""
Created on Tue Aug 24 00:00:57 2021

@author: Mateus Henrique
"""

prod = [input("Produto, valor($): ").split() for _ in range(int(input("Qtd: ")))]
[print("Nome: {}, Valor: ${:.2f}, Valor: R${:.2f}".format(x[0], float(x[1]), float(x[1]) * 5)) for x in prod]