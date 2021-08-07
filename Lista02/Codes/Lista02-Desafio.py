# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 22:59:03 2021

@author: Mateus Henrique
"""

L = int(input("Digite a largura da sala: "))
C = int(input("Digite o comprimento da sala: "))

qtdTipo2 = (((L - 1) + (C - 1)) * 2)
qtdTipo1 = (L * C) + ((L - 1) * (C - 1))

print("Lajotas necessárias: " + 
      "\nTipo 1 = " + str(qtdTipo1) +
      "\nTipo2 = " + str(qtdTipo2) + 
      "\nTipo 3 = 4")
