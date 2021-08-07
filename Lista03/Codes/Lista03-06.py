# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 17:58:34 2021

@author: Mateus Henrique
"""

x = int(input("Digite x: "))
z = int(input("Digite z: "))

if x < z:
    for num in range(x, (z + 1)):
        print(str(num), end=", ")
elif x == z:
    print("Nenhum valor entre x e z, eles são iguais.")
else:
    print("z é maior que x. Operação inválida.")