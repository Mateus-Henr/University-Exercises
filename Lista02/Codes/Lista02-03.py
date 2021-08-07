# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 20:12:50 2021

@author: Mateus Henrique
"""

anos = int(input("Digite o número de ano(s): "))
meses = int(input("Digite o número de mese(s): "))
dias = int(input("Digite o número de dias: "))
diasUser = dias
mesesUser = meses
qtdDiasEmMes = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

if (dias >= 0):
    if (anos > 0):
        dias = dias + (anos * 365)
    
    if (meses > 0):
        while (meses > 0):
            for qtdDias in qtdDiasEmMes:
                if (meses > 0):
                    dias = dias + qtdDias
                    meses -= 1
                else:
                    break
    
print(str(anos) + " ano(s), " + str(mesesUser) + " mese(s), " + str(diasUser) + " dia(s) é igual a " + str(dias) + " dias.")