# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:49:09 2021

@author: Mateus Henrique
"""
print("Write the sum of two values if greater than 10")

while True:
    try:
        firstNumber = int(input("Type the first number: "))
        secondNumber = int(input("Type the second number: "))
        
        sumOfTheNumbers = firstNumber + secondNumber
        
        if sumOfTheNumbers > 10:
            print("The result of the sum between the numbers informed '" 
                  + str(firstNumber) + "' and '" + str(secondNumber) + "' is " + str(sumOfTheNumbers))

        break
    except:
        print("Invalid Input.")
        continue