# -*- coding: utf-8 -*-
"""
Created on Tue Aug 17 12:53:17 2021

@author: Mateus Henrique
"""

a = int(input("Número: "))
b = int(input("Número: "))

while True:
    if b > a:
        break
    a = a - b
    print(a)