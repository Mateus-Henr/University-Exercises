# -*- coding: utf-8 -*-
"""
Created on Mon Aug 16 20:16:26 2021

@author: Mateus Henrique
"""

maiorPesoNome = maiorAlturaNome = ""
totalIdades = qtdAtletas = maiorAltura = maiorPeso = 0

while True:
    nome = input("Nome: ")
    
    if nome == "@":
        break
    
    sexo = input("Sexo: ")
    totalIdades += int(input("Idade: "))
    peso = float(input("Peso: "))
    altura = float(input("Altura: "))
                 
    if sexo == "FEMININO" or sexo.upper() == "F":
        if peso > maiorPeso:
            maiorPeso = peso
            maiorPesoNome = nome
    
    if altura > maiorAltura:
        maiorAltura = altura
        maiorAlturaNome = nome
        
    qtdAtletas += 1
    
    
print("Atleta mais alto: {}".format(maiorAlturaNome) + 
      "\nAtleta sexo feminino mais pesado: {}".format(maiorPesoNome) +
      "\nMédia idades: {}".format(totalIdades / qtdAtletas))
        