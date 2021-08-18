# -*- coding: utf-8 -*-
"""
Created on Mon Aug  9 18:29:52 2021

@author: Mateus Henrique
"""

horario = input("Digite o horário no formato (horas:minutos): ")

print("Se passaram " + str((int(horario.split(":")[0]) * 60) + 
                           int(horario.split(":")[1])) + " minutos.")