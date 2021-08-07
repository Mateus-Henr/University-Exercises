# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 21:23:25 2021

@author: Mateus Henrique
"""

idade = int(input("Digite a idade: "))
        
if (idade < 16):
     print("Não eleitor")
elif ((idade >= 18) and (idade < 65)):
     print ("Eleitor obrigatório")
else:
     print("Eleitor facultativo")