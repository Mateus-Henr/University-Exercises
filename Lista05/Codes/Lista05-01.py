# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:05:38 2021

@author: Mateus Henrique
"""

peso = int(input("Peso: "))
altura = int(input("Altura: "))
imc = peso / (altura ** 2)

if imc < 20:
    print("Abaixo do peso")
elif imc >= 20 and imc < 25:
    print("Peso Normal")
elif imc >= 25 and imc < 30:
    print("Sobrepeso")
elif imc >= 30 and imc < 40:
    print("Obeso")
else:
    print("Obeso Mórbido")