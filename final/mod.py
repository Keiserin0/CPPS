
# -*- coding: utf-8 -*-
"""
Created on Tue Jan 10 16:15:58 2023

@author: tanka
"""

import func as mod

#datarows = []
loop_status = True

    
while loop_status:
    mod.dispMenu()
    sel = input("Please choose A,B,C,D or Q: ").upper()
    if sel == "A":
        
        mod.completeYear()
        print("\n")
        
    elif sel == "B":
        mod.between()
        
    elif sel == "C":
        mod.mostVisitors()
        
    elif sel == "D":
        mod.plotGraph()
        
    elif sel == "Q":
        loop_status = False
        
    else:
        print("Sorry, Invalid selection. Please try again!")