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
        print(x)
        datalist.append(x)
        
totalrows = len(datalist)
#totalrows = 7

totalcols = len(datalist[0])
#totalcols = 8

        
def completeYear():
    print("Museum Visitors in 2014\n")
    for count in datalist:
        idx = datalist[0].index("2014")
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



    
def mostVistors():
    #3.	Of the user’s selected museum, display the three highest visitor attendances
    #and their corresponding years  
    
    for i in range(1,totalrows):

        y = tuple(datalist[i])
        z = sorted(y)
       # print(z)
        museumName = (z[-1])
        big_3 = (z[-4:])
        #print(big_3)
        
        print(f"{z[-1]}, {big_3[0]},{big_3[1]},{big_3[2]}")
        
       # for row in range(1,totalrows):
         #   museumName = datalist[row][0]
        #    for col in range(1,totalcols):
       #         x = datalist[row][col]
      #          for num in range(3):
     #               if int(x) == int(big_3[num]):
   #                     idy = x.index(big_3[num])
  #                      print(f" big_3[num] index is {idy} ")
    #                    

        
    
    #
    #big_3 = (z[:3]) prints 3 smallest
    #big_3 = (z[:-3]) print all except 3 biggest
    #big_3 = (z[3:]) print all except 3 smallest
        

def plotGraph():

    import matplotlib.pyplot as plt
    

    years = datalist[0][1:]
    print(years)
    NMS = datalist[2][1:]
    print(NMS)
    SAM = datalist[3][1:]
    print(SAM)
    
    plt.title("NMS against SAM")
    plt.xlabel("year")
    plt.ylabel("museum")
    

    plt.plot(years, NMS)
    plt.plot(years, SAM)

    
    
    
    
    

               
