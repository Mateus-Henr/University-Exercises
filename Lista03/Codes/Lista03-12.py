# -*- coding: utf-8 -*-
"""
Created on Sat Jul 31 19:05:52 2021

@author: Mateus Henrique
"""

cabeca = 1
nodulo = cauda = 0

for x in range(20):
    
    cauda = cabeca + nodulo
    cabeca = nodulo
    nodulo = cauda
    
    if x == 19:
      print(str(cauda))
    else:
        print(str(cauda), end=", ")