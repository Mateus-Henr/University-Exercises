# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 23:27:46 2021

@author: Mateus Henrique
"""

print("Conversor from Celsius to Fahrenheit")

def formatFloatValue(valueToFormat):
    return str("%.2f" % valueToFormat)

while True:
    try:
        celsius = float(input("Type the temperature in Celsius: "))
        
        fahrenheit = (celsius * 1.8) + 32
        
        break
    except:
        print("Invalid Input.")
        continue
    
print(formatFloatValue(celsius) + "°C is equal to " + formatFloatValue(fahrenheit) + "°F.")