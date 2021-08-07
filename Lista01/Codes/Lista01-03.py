# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:36:28 2021

@author: Mateus Henrique
"""

print("The amount of fuel spent on a trip")

while True:
    try:
        timeSpent = int(input("Type the time in hours spent to complete the trip: "))
        speed = int(input("Type the speed that you used during the trip: "))
        
        distance = timeSpent * speed
        litresOfFuelSpent = float(distance / 12)
        
        break
    except:
        print("Invalid Input.")
        continue
    
print("The informations about the trip provided by the user: " +
      "\nSpeed: " + str(speed) +
      "\nTime spent: " + str(timeSpent) + "h")
print("The traveled distance is " + str(distance) + "Km(s)." +
      "\nThe amount of litles spent to complete the journey is " + str(litresOfFuelSpent) + "L.")