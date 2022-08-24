# Importing the data source to code
import os
import csv

# Creating directory to extract file source data 

os.chdir(os.path.dirname(__file__))
budget_data_csv = os.path.join('Resources', 'budget_data.csv')

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