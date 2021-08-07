# -*- coding: utf-8 -*-
"""
Created on Mon Jul 19 10:58:49 2021

@author: Mateus Henrique
"""

print("Costs of a new car")

percDistributor = 28
percTax = 45

while True:
    try:
        factoryCost = float(input("Type the factory cost: $"))
        distributorCost = factoryCost + (factoryCost * (percDistributor / 100))
        taxCost = factoryCost + (factoryCost * (percTax / 100))
        
        consumerCost = factoryCost + distributorCost + taxCost
    
        break
    except:
        print("Invalid Input.")
        continue

print("The consumer cost is R$" + str("%.2f" % consumerCost))