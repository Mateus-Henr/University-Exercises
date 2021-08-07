# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:29:34 2021

@author: Mateus Henrique
"""

print("Display the predecessor and successor of a number")

while True:
    
    try:
        number = int(input("OBS: In case of a decimal number is informed the number will be rounded. \nEnter a number: "))
        
        break
    except:
        print("Invalid Input.")
        continue
    
print("The predecessor of " + str(number) + " is " + str(number-1) +
      "\nThe successor of " + str(number) + " is " + str(number+1))
            