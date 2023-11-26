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
    
#initiate datalist
datalist = []
#file_name = input("enter csv file name (e.g, file.csv): ")
file_name = "museumvisitors_dataset.csv"
with open(file_name) as mv:
    for row in mv:
        #removes all \n
        result = row.strip("\n")
        #split each element with a ","
        x = result.split(",")
        #append x into datalist
        datalist.append(x)
#totalrows = 7      
totalrows = len(datalist)
#counts the total amount of rows

#totalcols = 8
totalcols = len(datalist[0])
#count the total amount of columns
        
def completeYear():
    #print("Museum Visitors in 2014\n")
    #enter 2014
    year_input = input("enter year: ")
    for count in datalist:

        idx = datalist[0].index(year_input)
        idx2 = datalist[0].index("Museum")
        name = count[idx2]
        amount = count[idx]
        
        print(f"{name}, {amount}")
        
def between():
    
    for row in range(1,totalrows):
        museumName = datalist[row][0]
        for col in range(1,totalcols):
            x = datalist[row][col]
            if 400000 < int(x) < 800000:
                print(f"Museum: {museumName}, Year: {datalist[0][col]}, Visitor Count: {x} ")
                
def selectMenu():
    print("""
================================================================================
                        
                        * Please Select A, B, C or Q *
        A. Asian Civilisations Museum (ACM)

        B. National Museum of Singapore (NMS)
        
        C. Singapore Art Museum (SAM)

        D. Singapore Philatelic Museum (SPM)
        
        E. Sun Yat Sen Nanyang Memorial Hall (SYSNMH)
        
        F. The Peranakan Museum (TPM)

        Q. Terminate the program
            
            
================================================================================
    """)      
                
       
def mostVisitors():
    print("Select a Museum:")
    selectMenu()
    museum = input().upper()
    museum_index = None
    
    if museum == "A":
        museum_index = 1
    elif museum == "B":
        museum_index = 2
    elif museum == "C":
        museum_index = 3
    elif museum == "D":
        museum_index = 4
    elif museum == "E":
        museum_index = 5
    elif museum == "F":
        museum_index = 6
    elif museum == "Q":
        return

    museum_data = datalist[museum_index][1:]
    museum_data = [(int(data), year) for year, data in zip(datalist[0][1:], museum_data)]
    museum_data.sort(reverse=True)

    print(f"Three highest visitor counts and corresponding years for {datalist[museum_index][0]}:")
    for i in range(3):
        print(f"Year: {museum_data[i][1]}, Visitor Count: {museum_data[i][0]}")