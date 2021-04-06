## The task is to creating a Python script 
# for analyzing the financial records of your company
import os
import csv

# set file path
Pybank_csv = os.path.join("Resources", "budget_data.csv")

# Create lists to store data

curNumber = []
preNumber = []
curMonth = []
preMonth = []
sum = []
change = []
avgChange = []
maxIncr = []
maxDec = []
maxIncr_Month = []
maxDec_Month = []

# Open the Pybank_csv file
with open(Pybank_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)

     # Read through the data
    for row in csvreader:
        
        curMonth = row[0]
        curNumber = row[1]
        sum = sum + int(row[1])
        change = curNumber - preNumber 
    
        # Find the greatest increase in profits(date and amount)
        if change > 0:
            if change > maxIncr: maxIncr = change
        else: maxIncr = maxIncr + 0 

        # Find the greatest decrease in profits(date and amount)
        if change < 0:
            if change < maxIncr: maxDec = change
            max 
        else: maxDec = maxDec - 0 

        # Assign the current profit/losses to previous value
        preNumber = curNumber


    # Calculate the total number of months, sum of all changes, and the average change     
    sumrow = crow_sum()
    sumChange = sumChange + (crow[1] - preNumber)
    avgChange = sumChange/sumrow
    
# Print my analysis
print("Financial Analysis")
print("-----------------------------")

print("Total Months:" + str(sumrow))
print("Total:" + str(sum))
print("Greatest Increase in Profits:" + maxIncr_Month + str(maxIncr))
print("Graetest Decrease in Profits:" + maxDec_Month + (str(maxDec)))
