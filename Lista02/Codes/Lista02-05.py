# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 19:57:34 2021

@author: Mateus Henrique
"""

def formataNum(num):
    return str("%.0f" % num) if (num).is_integer() else str(num)

dividendo = float(input("Digite o dividendo: "))
divisor = float(input("Digite o divisor: "))

if (divisor > 0):
    quociente = dividendo // divisor
    resto = dividendo % divisor
    
    print("Resultados da divisão " + formataNum(dividendo) + " / " +  formataNum(divisor) + ": " +
          "\nQuociente = " + formataNum(quociente) +
          "\nResto = " + formataNum(resto))
    
else:
    print("Divisão não permitida")