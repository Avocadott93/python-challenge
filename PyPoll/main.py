## The task is to help a small town with processing vote conuting
import os
import csv

# set file path_
PyPoll_csv = os.path.join("Resources", "election_data.csv")
PyPoll_txt = os.path.join("analysis", "elections_results.txt")


## What the questions asking?
## 1. how many rows in total (minus the header)
## 2. list of candidates who receiced votes
## 3. total number of votes each candidate got
## 4. percentage of each candidate got
## 5. find the candidate who received the most votes

# Create lists to store data
#create total votes
total_votes = 0

candidates = []

candidates_votes = {}

# {name1: 12, name 2: 5000}

winner_candidate = ""

winner_votes = 0



# Open the Pybank_csv file
with open(PyPoll_csv) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    header = next(csvfile)
    

     # Read through the data
    for row in csvreader:

        total_votes = total_votes + 1

        name = row[2]

        if name not in candidates:
            candidates.append(name)

            candidates_votes[name] = 0

        candidates_votes[name] = candidates_votes[name]+1

    # List all the candidates adn 
    print(candidates)
    print(candidates_votes)    

    # Calculate percentage for each candidate
    percent_1 = candidates_votes["Khan"]/ total_votes
    percentage_1 = "{:.0%}". format(percent_1)
    print(percentage_1)

    percent_2 = candidates_votes["Correy"]/ total_votes
    percentage_2 = "{:.0%}". format(percent_2)
    print(percentage_2)

    percent_3 = candidates_votes["Li"]/ total_votes
    percentage_3 = "{:.0%}". format(percent_3)
    print(percentage_3)

    percent_4 = candidates_votes["O'Tooley"]/ total_votes
    percentage_4 = "{:.0%}". format(percent_4)
    print(percentage_4)

    # Print out analysis results
    print("Election Results")
    print("-------------------------")


    print("Khan: ", "(",candidates_votes["Khan"], ")")
    
    with open(PyPoll_txt, "w") as txt_file:
        # print total votes
        total_votes_results = (f"total votes: {total_votes}" )
        txt_file.write(total_votes_results)

        # print percentage, winner, 
        candidates_votes_Khan = (f"Khan: {candidates_votes[Khan]}")
        txt_file.write(candidates_votes_Khan)






        

        



