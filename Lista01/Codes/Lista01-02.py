# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 22:16:59 2021

@author: Mateus Henrique
"""

print("Calculate the number of minimum salaries that a specific salary has")

def formatFloatValue(valueToFormat):
    return str("%.2f" % valueToFormat)

while True:
    try:
        minimumSalary = float(input("Type the minimum salary value: R$"))
        personSalary = float(input("Type the salary value: R$"))
        
        break
    except:
        print("Invalid Value")
        continue
    
print("The minimum salary value informed is R$" + formatFloatValue(minimumSalary) + 
      "\nThe person with a salary of R$" + formatFloatValue(personSalary) + 
      " earns " +  formatFloatValue(personSalary / minimumSalary) + "x the minimum salary.")