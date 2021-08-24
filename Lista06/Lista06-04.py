# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:54:22 2021

@author: Mateus Henrique
"""

vetor = [int(x) for x in input("Digite os 25 números: ").split(None, 25)[:25]]
n = int(input("Posição: "))
print(vetor[n] if n < len(vetor) else "Posição inexistente.")