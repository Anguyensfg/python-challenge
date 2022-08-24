# Importing the data source to code
import csv
import os

# Creating directory to extract file source data 
os.chdir(os.path.dirname(__file__))
csvpath = os.path.join('Resources', 'election_data.csv')
election_data_csv = os.path.join('Resources', 'election_data.csv')

# create output for text file
text_path = "output.txt"

# Allocate variables/parameters to code 
votes = 0
winner_votes = 0
total_candidates = 0
greatest_votes = ["", 0]
candidate_options = []
candidate_votes = {}

# Opening CSV data file 
with open(csvpath) as csvfile:
    reader = csv.DictReader(csvfile)
    # Calculate total votes under candidate column 
    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        
    
    # Breakdown cacluation against each candidate name
        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    # Based winnder on the highest amount of votes
    if (votes > winner_votes):
        greatest_votes[1] = candidate_votes
        greatest_votes[0] = row["Candidate"]
    
    #Return calculations
    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
    
    # Calculating each candidate votes and percentage of total votes
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
    
candidate_votes

winner = sorted(candidate_votes.items(),)

# Return calculations
print("-------------------------")
print("Winner: " + str(winner[1]))
print("-------------------------")

# Store calualtion in text output file 
with open(text_path, "w") as txt_file:
    
    txt_file.write("Election Results")
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")")
    txt_file.write(str(winner))
    txt_file.write("\n")
    txt_file.write("-------------------------")
    txt_file.write("\n")
    txt_file.write("Winner: " + str(winner[1]))
    txt_file.write("\n")
