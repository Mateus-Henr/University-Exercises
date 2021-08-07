# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 23:03:36 2021

@author: Mateus Henrique
"""

divisor = 0
resultado = 0

x = int(input("Digite o valor de x: "))

for potencia in reversed(range(1, 26)):
    divisor += 1
    
    if (potencia % 2) == 0:
        resultado -= (x ** potencia) / divisor
        print(" - " + str(x) + "^" + str(potencia) + "/" + str(divisor), end="")
    else:
        resultado += (x ** potencia) / divisor
        print(((" + ") if (potencia != 25) else "") + str(x) + 
                "^" + str(potencia) + "/" + str(divisor), end="")
        

print("\nResultado = " + str(resultado))
    
