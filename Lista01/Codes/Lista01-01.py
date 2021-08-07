# -*- coding: utf-8 -*-
"""
Created on Sun Jul 18 21:00:52 2021

@author: Mateus Henrique
"""
tipPercentage = 10

class Expense:
    
    def __init__(self, name, value):
        self.name = name
        self.value = value
        self.tipValue = (value * (tipPercentage / 100))
        self.totalValue = value + self.tipValue



quit = False;
listOfExpenses = []

def menu():
    print()
    print("\n1 - Add a new expense" +
          "\n2 - See all your expenses" +
          "\n3 - Quit the program")
    
def formatFloatValue(valueToPrint):
    return str("%.2f" % round(valueToPrint, 2))

print("Welcome to our restaurant" +
      "\nYour list of expenses")

while not quit:
    menu()
    userChoice = input("Choose an option: ")
    
    if userChoice == "1":
        expenseName = input("Enter the expense's name: ")
        try:
            expenseValue = float(input("Enter a value for the expense named as '" + expenseName + "': $"))
        except:
            print("Invalid value")
            continue
        
        newExpense = Expense(expenseName, expenseValue)
        listOfExpenses.append(newExpense)
        print("\nThe name informed for the expense is: " + expenseName +
              "\nThe value informed for the expense named as '" + expenseName + "' is $" + formatFloatValue(expenseValue) +
              "\nThe tip to be given will be $" + formatFloatValue(newExpense.tipValue) +
              "\nThe total value with the tip is $" + formatFloatValue(newExpense.totalValue))
        
    elif userChoice == "2":
        if len(listOfExpenses) == 0:
            print("\nNo expenses found.")
        else:
            for expense in listOfExpenses:
                print("\nName: " + expense.name +
                      "\nValue: $" + formatFloatValue(expense.value) +
                      "\nTip value: $" + formatFloatValue(expense.tipValue) +
                      "\nTotal Value: $" + formatFloatValue(expense.totalValue) + "\n")
            
    elif userChoice == "3":       
        print("See you!")
        quit = True
        
    else:
        print("Invalid Input.")
    