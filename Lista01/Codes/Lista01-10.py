# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:18:42 2021

@author: Mateus Henrique
"""

print("Perimeter of a square")

while True:
    try:
        sizeOfTheSide = float(input("Type the size of a side of the square: "))
        
        break
    except:
        print("Invalid Input.")
        continue
    
print("The perimeter of the square informed, whose side is " + str(sizeOfTheSide) + ", is " + str(sizeOfTheSide * 4))