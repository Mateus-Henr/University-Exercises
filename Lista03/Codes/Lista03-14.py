# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:09:24 2021

@author: Mateus Henrique
"""

from random import randint

votos = []
listaDeVotos = {1:0, 2:0, 3:0, 4:0, 5:0, 6:0}
totalVotos = 0

for x in range(1000):
    votos.append(randint(list(listaDeVotos.keys())[0], 
                         list(listaDeVotos.keys())[len(listaDeVotos) - 1]))


for voto in votos:
    if voto in listaDeVotos.keys():
        listaDeVotos[voto] += 1
        totalVotos += 1
        
for opcao in listaDeVotos.keys():
    if opcao in range(1, 5):
        print("Candidato " + str(opcao) + " tem " + 
              str(listaDeVotos[opcao]) + " votos.")
    elif opcao == 5:
        print("Quantidade de votos nulos = " + str(listaDeVotos[opcao]))
    else:
        print("Quantidade votos em branco = " + str(listaDeVotos[opcao]))

invalido = listaDeVotos[5] + listaDeVotos[6]
print("Porcentagem de votos nulos e brancos sobre o total é de " + 
      str("%.2f" % ((invalido / totalVotos) * 100)) + "%")