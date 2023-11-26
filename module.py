# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 22:41:52 2023

@author: tanka
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:15:58 2023

@author: tanka
"""

import bol as mod

datarows = []
loop_status = True

    
while loop_status:
    mod.dispMenu()
    sel = input("Please choose A,B,C or Q: ").upper()
    if sel == "A": #or sel == "a":
        mod.completeYear()
        print("\n")
        
    elif sel == "B":
        mod.between()
        
    elif sel == "C":
        print("not done")
        
    elif sel == "D":
        loop_status = False
        
    elif sel == "Q":
        break
        
    else:
        print("Sorry, Invalid selection. Please try again!")