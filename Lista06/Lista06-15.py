# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 23:00:47 2021

@author: Mateus Henrique
"""

vetor = [[str(x) for x in input("Qtd, peso, preço, valor: ").split()] for _ in range(5)]
realVal = sum(float(x[0]) for x in vetor) * sum(float(x[2]) for x in vetor)

print("Peso Total: {}".format(sum(float(x[1]) for x in vetor)) +
      "\nValor Total: {} \nConflito: {}".format(realVal, "Não" if sum(float(x[3]) for x in vetor) == realVal else "Sim"))

