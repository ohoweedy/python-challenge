import os
import csv

pybankCSV = os.path.join('budget_data.csv')

with open(pybankCSV, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)
    #print(f"CSV Header: {csv_header}")

    counter=0
    sum=0
    y=0
    z=0
    profits = []
    deltas = []
    
    # Read each row of data after the header
    for row in csvreader:
        counter +=1
        sum +=int(row[1])
        profits.append(int(row[1]))
    
    while y < len(profits):
        for x in profits:
            y +=1
            deltas = profits[y] - profits[z]
            z +=1
            print(deltas)

print("Financial Analysis")
print("---------------------")
print(f"Total Months: {counter}")
print(f"Total: ${sum}")
