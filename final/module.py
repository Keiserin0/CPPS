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

import function as mod

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
        mod.mostVistors()
        
    elif sel == "D":
        mod.plotGraph()
        
    elif sel == "Q":
        loop_status = False
        
    else:
        print("Sorry, Invalid selection. Please try again!")