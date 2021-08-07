# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:29:57 2021

@author: Mateus Henrique
"""

print("Are the informed numbers divisible by one another?")

while True:
    try:
        firstNumber = float(input("Type the first number: "))
        secondNumber = float(input("Type the second number: "))
        
        if (firstNumber % secondNumber) == 0:
            print("The first number '" + str(firstNumber) + "' is divisible by the second number '" + str(secondNumber) + "'.")
        if (secondNumber % firstNumber) == 0:
            print("The second number '" + str(secondNumber) + "' is divisible by the first number '" + str(firstNumber) + "'.")
        else:
            print("The numbers typed '" + str(firstNumber) + "' and '" + str(secondNumber) + "' are not divisible by one another.")
            
        break
    except:
        print("Invalid Input.")
        continue