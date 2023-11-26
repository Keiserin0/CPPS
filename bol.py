# -*- coding: utf-8 -*-
"""
Created on Wed Jan 11 20:57:50 2023

@author: tanka
"""

def dispMenu():
    
    print("""
================================================================================
                        
                        * Please Select A, B, C or Q *
        A. Display the visitor numbers of all museums in the year 2014.

        B. Display the museums, the years and the visitor numbers where the 
        visitor numbers are between 400,000 and 800,000 over the 
        7-year span.

        C. Display the three highest visitor attendances and their 
        corresponding years over the 7-year span.

        D. Plots for visitor number of NMS and SAM vs Year and Total number of 
        visitors to all museums excluding NMS and NMS vs Year as a bar graph

        Q. Terminate the program
            
            
================================================================================
    """)
    

datalist = []

with open('museumvisitors_dataset.csv') as mv:
    for row in mv:
        result = row.strip("\n")
        x = result.split(",")
        datalist.append(x)
        
def completeYear():
    print("Museum Visitors in 2014\n")
    for count in datalist:
        idx = datalist[0].index("2014")
        idx2 = datalist[0].index("Museum")
        name = count[idx2]
        amount = count[idx]
        
        print(f"{name}, {amount}")
        
def between():
    
    #totalrows = 7
    totalrows = len(datalist)
    totalcols = len(datalist[0])
    
    for row in range(1,totalrows):
        museumName = datalist[row][0]
        for col in range(1,totalcols):
            x = datalist[row][col]
            if 400000 < int(x) < 800000:
                print(f"Museum: {museumName}, Year: {datalist[0][col]}, Visitor Count: {x} ")
            else:
                continue
    
    
    
        
        
        

               
