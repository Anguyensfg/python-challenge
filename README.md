# python-challenge

Week 3 - Assignment 

------------------------------------------------------------------------------------------------------------------------------------------------------------

Part 1 - PyBank 

------------------------------------------------------------------------------------------------------------------------------------------------------------

PyBank Instructions:

In this Challenge, you are tasked with creating a Python script to analyse the financial records of your company. You will be given a financial dataset called budget_data.csv. The dataset is composed of two columns: "Date" and "Profit/Losses".

Your task is to create a Python script that analyses the records to calculate each of the following values:

The total number of months included in the dataset

The net total amount of "Profit/Losses" over the entire period

The changes in "Profit/Losses" over the entire period, and then the average of those changes

The greatest increase in profits (date and amount) over the entire period

The greatest decrease in profits (date and amount) over the entire period

-------------------------------------------------------------------------------------------

# Importing the data source to code
import os
import csv

# Creating directory to extract file source data 
os.chdir(os.path.dirname(__file__))
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

# create output for text file
text_path = "output.txt"

# Allocate variables/parameters to code 
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

# Opening CSV data file 
with open(budget_data_csv, newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")

    # Reading Headers
    csv_header = next(csvreader)

    # Reading the headers to determine the starting point for cacluations 
    first_row = next(csvreader)
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
    # Analysing data and tracking month movement 
    for row in csvreader:
        dates.append(row[0])
        
        # Calculate the change and store to list 
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        
        # Calculate total months
        total_months += 1

        # Calculate total profit/loss over period 
        total_pl = total_pl + int(row[1])

    # Calculate Greatest Increase in Profits
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

    #Calculate Greatest Decrease in profits 
    greatest_decrease = min(profits)
    worst_index = profits.index(greatest_decrease)
    worst_date = dates[worst_index]

    #Average change in Profit/Losses between months over period 
    avg_change = sum(profits)/len(profits)
    

# Return calculations

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")

# Store calualtion in text output file 

output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {worst_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))

------------------------------------------------------------------------------------------------------------------------------------------------------------------

PyPoll Instructions:

In this Challenge, you are tasked with helping a small, rural U.S. town modernise its vote-counting process.

You will be given a set of poll data called election_data.csv. The dataset is composed of three columns: "Voter ID", "County", and "Candidate". Your task is to create a Python script that analyzes the votes and calculates each of the following values:

The total number of votes cast

A complete list of candidates who received votes

The percentage of votes each candidate won

The total number of votes each candidate won

The winner of the election based on popular vote

----------------------------------------------------------------------------------------------------

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


--------------------------------------------------------------------------------------------------------------------------------------------------------------




