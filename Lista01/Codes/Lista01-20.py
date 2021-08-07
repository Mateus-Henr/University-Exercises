# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 00:23:40 2021

@author: Mateus Henrique
"""

print("Inform the electoral class depending on the age")

while True:
    try:
        age = int(input("Type the person's age': "))
        
        if age < 16:
            print("Can't vote. It's not a voter.")
        elif age >= 18 and age < 65:
            print ("Mandatory voter.")
        else:
            print("Optional voter.")
            
        break
    except:
        print("Invalid Input.")
        continue