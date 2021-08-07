# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:04:53 2021

@author: Mateus Henrique
"""

print("Write the number if greater than 20")

while True:
    try:
        number = int(input("Type a number: "))
        
        if number > 20:
            print("The typed number '" + str(number) + "' is greater than 20.")

        break
    except:
        print("Invalid Input.")
        continue