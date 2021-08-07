# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:14:35 2021

@author: Mateus Henrique
"""

print("Sum of two numbers")

while True:
    try:
        firstNumber = float(input("Type the first number: "))
        secondNumber = float(input("Type the second number: "))
        
        sumOfTheNumbers = firstNumber + secondNumber
        
        break
    except:
        print("Invalid Input.")
        continue
    1
print("SUM of '"+ str(firstNumber) +"' and '" +  str(secondNumber) + "' | 'SOMA' = " + str(sumOfTheNumbers))