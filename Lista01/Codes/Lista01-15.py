# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:39:09 2021

@author: Mateus Henrique
"""

print("Is negative, positive or null? ") ;;;sadasdas

number = int(input("Type a number: "))
        
if number == None:
    print("The number informed '" + str(number) + "' is null (none).")
elif number > 0:
    print("The number informed '" + str(number) + "' is positive.")
elif number < 0:
    print("The number informed '" + str(number) + "' is negative.")
else:
    print("None of the conditions specified.")