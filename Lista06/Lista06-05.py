# -*- coding: utf-8 -*-
"""
Created on Mon Aug 23 19:59:04 2021

@author: Mateus Henrique
"""

vetor = [int(input("Nota: ")) for _ in range(15)]
print("A média é {}".format (sum(vetor) / len(vetor)))