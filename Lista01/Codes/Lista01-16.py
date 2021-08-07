# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:55:54 2021

@author: Mateus Henrique
"""

print("Sum of two numbers")

while True:
    try:
        firstNumber = float(input("Type the first number: "))
        secondNumber = float(input("Type the second number: "))
        
        sumOfTheNumbers = firstNumber + secondNumber
        
        if sumOfTheNumbers > 20:
            print("As the sum of the numbers is greater than 20, 8 will be added." +
                  "\nThe final result is " + str(sumOfTheNumbers + 8))
        else:
            print("As the sum of the numbers is smaller than 20, 5 will be subtracted." +
                  "\nThe final result is " + str(sumOfTheNumbers - 5))
            
        break
    except:
        print("Invalid Input.")
        continue