# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 17:55:21 2020

@author: Lenovo
"""


import os
import csv

def print_analysis():
    
    print("""Financial Analysis
----------------------------------------------""")
    print(f"Total Months: {int(len(Dates))}")
    print(f"Total: ${Net_Total}")
    print(f"Average Change: $ {avgchange}")
    print(f"Greatest Increase in profit:{Dates[Change.index(GreatestInc)]} ( ${GreatestInc})")
    print(f"Greatest Decrease in profit:{Dates[Change.index(GreatestDec)]} ( ${GreatestDec})")


input_file= os.path.join("Resources","PyBank_Resources_budget_data.csv") 
    
#define variables and lists to be used as per the analysis required

Dates=[]        #stores all dates as list
profit_loss=[]  #stores profit/loss values as list
Totalchange=0   #Total change value will hold the final change in profit and loss
Change=[]       #defines list to hold the change in profit/loss
GreatestInc=0   #variable to hold the greatest increase in profit
GreatestDec=0   #variable to hold the greatest decrease in profit
Net_Total=0     # variable to hold the net value of profit or loss
diff=[]         # holds values of change as a list to call the values as required

#open the input file with the described path in csv format to read the data

with open(input_file,'r', newline="") as csvfile:
    
    #Read the input csv file 
    input_read= csv.reader(csvfile, delimiter=",")
    
    #dont need to read the headers
    next(csvfile, None)
    
    #looping to read every row and stores values as required
    for row in input_read:
        
        #store the dates as a list
        Dates.append(row[0])
        
        # running total of the profit/loss values
        Net_Total+= float(row[1])
        
        #Create a list to hold profit/loss values
        profit_loss.append(row[1])
     
    # Calculate the change in profit/ loss value to determine max and min values
    for i in range(len(profit_loss)):
        
        if i==0:            #change should be of the same size as the other lists to recall corresponding values
            diff=0
                       
        else:
            diff=float(profit_loss[i])- float(profit_loss[i-1])    
            
        Totalchange+=diff
        Change.append(diff)   
        
    #Average change is total change divided by the actual no of changes i.e length of change list minus 1            
    avgchange= round((Totalchange/int(len(Change)-1)),2)    #rounding off to 2 decimal places  
    
    #calculate the greatest increase and decrease using the max and min fucntions
    GreatestInc=max(Change)
    GreatestDec= min(Change)
    
    
    #call the print function to display the output
    print_analysis()

#to export the results to a text file:
 
output_file= os.path.join("Analysis","pyBank-Analysis.txt")

#open the output file in write format
with open(output_file, 'w+') as text:

    text.write("""Financial Analysis
----------------------------------------------""")
    text.write("\n" +"Total Months:" + str(int(len(Dates))) +"\n")
    text.write("Total: $" + str(Net_Total) +"\n")
    text.write("Average Change:" + " $" + str(avgchange) + "\n")
    text.write("Greatest Increase in profit: " + str(Dates[Change.index(GreatestInc)]) +" ($" + str(GreatestInc) +")" +"\n")
    text.write("Greatest Decrease in profit: " + str(Dates[Change.index(GreatestDec)]) +" ($" + str(GreatestDec) +")" +"\n")
    
    text.close()