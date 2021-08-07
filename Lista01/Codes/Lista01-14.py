# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:54:13 2021

@author: Mateus Henrique
"""

print("Check if the number is even or odd")

while True:
    try:
        number = int(input("Type the number that yo'ud like to check: "))
        
        if (number % 2) == 0:
            print("The typed number '" + str(number) + "' is even.")
        else:
            print("The typed number '" + str(number) + "' is odd.")
            
        break
    except:
        print("Invalid Input.")
        continue