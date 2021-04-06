## The task is to help a small town with processing vote conuting
import os
import csv

# set file path
PyPoll_csv = os.path.join("Resources", "election_data.csv")


## What the questions asking?
## 1. how many rows in total (minus the header)
## 2. list of candidates who receiced votes
## 3. total number of votes each candidate got
## 4. percentage of each candidate got
## 5. find the candidate who received the most votes

# Create lists to store data

num_Khan = 0
num_Correy = 0
num_Li = 0
num_OTooley = 0

# Open the Pybank_csv file
with open(PyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    crow = next(csvfile)

     # Read through the data
    for crow in csvreader:
        if crow[2] == Khan:
            num_Khan = num_Khan + 1
            
        elif crow[2] == Correy:
            num_Co

        

             



