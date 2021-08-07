# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:26:42 2021

@author: Mateus Henrique
"""

print("Calcule the volume of an oil can")

while True:
    try:
        radius = float(input("Type the radius of the oil can: "))
        height = float(input("Type the height of the oil can: "))
        volume = (3.14159 * (radius * radius) * height)
        
        break
    except:
        print("Invalid Input.")
        continue
    
print("The properties of the informed oil can are: "
      "\nHeight: " + str(height) +
      "\nRadius: " + str(radius) +
      "\nVolume: " + str("%.2f" % volume))