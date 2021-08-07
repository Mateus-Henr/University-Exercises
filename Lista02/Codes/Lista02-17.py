# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:32:40 2021

@author: Mateus Henrique
"""

salario = float(input("Digite o salário: "))
prestacao = float(input("Digite a prestação: "))

if ((salario > 0) and (prestacao > 0)):
    if (prestacao <= (salario * 0.30)):
        print("O empréstimo pode ser concedido.")
    else:
        print("O empréstimo não pode ser concedido.")