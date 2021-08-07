# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:37:59 2021

@author: Mateus Henrique
"""

dias = int(input("Digite a idade em dias: "))
qtdDiasEmMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
diasUser = dias
anos = 0
meses = 0
quit = False


while not quit:
    for qtdDias in qtdDiasEmMes:
        if (dias >= qtdDias):
            dias = dias - qtdDias
            meses += 1
        else:
            quit = True
            break

if (meses >= 12):
    anos = meses // 12
    meses = meses - (anos * 12)

print("A idade de " + str(diasUser) + " dias é: " +
      "\nAno(s) = " + str(anos) +
      "\nMese(s) = " + str(meses) +
      "\nDia(s) = " + str(dias))
    
    