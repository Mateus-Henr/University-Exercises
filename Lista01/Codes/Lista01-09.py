# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:38:52 2021

@author: Mateus Henrique
"""

print("The sum of the square of three numbers")

def squareOfNumber(numberToCalculate):
    return str(numberToCalculate * numberToCalculate)

while True:
    try:
        firstNumber = int(input("Type the first number: "))
        secondNumber = int(input("Type the second number: "))
        thirdNumber = int(input("Type the second number: "))
        
        break
    except:
        print("Invalid Input.")
        continue
    
print("The squares: " +
              "\n" + str(firstNumber) + " - " + squareOfNumber(firstNumber) +
              "\n" + str(secondNumber) + " - " + squareOfNumber(secondNumber) +
              "\n" + str(thirdNumber) + " - " + squareOfNumber(thirdNumber) +
              "\nThe sum of the squares is " + str((firstNumber * firstNumber) +
                                                    (secondNumber * secondNumber) +
                                                    (thirdNumber * thirdNumber)))