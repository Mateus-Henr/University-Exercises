# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:51:01 2021

@author: Mateus Henrique
"""

print("Is multiple of 3? programme")

while True:
    try:
        numberToCheck = int(input("Type the number that you'd like to see if it's multiple of 3: "))
        
        if numberToCheck % 3 == 0:
            print("The number informed '" + str(numberToCheck) + "' IS a multiple of three.")
        else:
            print("The number informed '" + str(numberToCheck) + "' is NOT a multiple of three.")
            
        break
    except:
        input("Invalid Value.")