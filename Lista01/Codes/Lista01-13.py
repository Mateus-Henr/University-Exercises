# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 11:24:32 2021

@author: Mateus Henrique
"""

print("Division")

while True:
    try:
        divisor = int(input("Type the divisor: "))
        dividend = int(input("Type the dividend: "))
        
        if divisor == 0:
            print("Division not allowed.")
            break
        
        print("Quotient = " + str(divisor // dividend) +
              "\nRest = " + str(divisor % dividend))
        
        break
    except:
        print("Invalid Input.")
        continue