# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:51:20 2021

@author: Mateus Henrique
"""

print("A and B")

while True:
    try:
        a = input("Type the A value: ")
        b = input("Type the B value: ")
        
        if a > b:
            print("A is bigger than B.")
        elif a < b:
            print ("A is smaller than B.")
        else:
            print("A and B have the same value.")
            
        break
    except:
        print("Invalid Input.")
        continue