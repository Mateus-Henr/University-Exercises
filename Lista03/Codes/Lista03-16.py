# -*- coding: utf-8 -*-
"""
Created on Sun Aug  1 12:38:56 2021

@author: Mateus Henrique
"""
"""
from random import randint

sim = 1
nao = 2
m = {sim: 0, nao: 0}
f = {sim: 0, nao: 0}

for x in range(2000):
    resposta = randint(1, 2)
    if randint(1, 2) == 1:
        m[resposta] += 1
    else:
        f[resposta] += 1

totalSim = m[sim] + f[sim]
totalNao = m[nao] + f[nao]

print("Pessoas que responderam sim = " + str(totalSim) +
      "\nPessoas que responderam nao = " + str(totalNao) +
      "\nPocentagem do sexo feminino que respondeu sim = " + 
      str("%.2f" % (f[sim] / (f[sim] + f[nao]) * 100)) + "%" +
      "\nPocentagem do sexo masculino que respondeu sim = " + 
      str("%.2f" % (m[sim] / (m[sim] + m[nao]) * 100)) + "%")
"""

from random import randint
sim, nao, femsim, mascnao = 0, 0, 0, 0
mTotal, fTotal = 0, 0
for i in range (0, 2000):
    voto = randint(1, 2)
    sexo = randint(1, 2)
    if voto == 1:
        sim += 1
    if voto == 2:
        nao += 1
    if sexo == 1:
        mTotal += 1
        if voto == 2:
            mascnao += 1
    if sexo == 2:
        fTotal += 1
        if voto == 1:
            femsim += 1
print('Votos SIM: {}\nVotos NÃO: {}'.format(sim, nao))
print('Fem. SIM: {}%\nMasc. NÃO: {}%'.format(((femsim) / fTotal) * 100, ((mascnao) / mTotal) * 100))
