import os
import csv

pypollCSV = os.path.join('election_data.csv')

with open(pypollCSV, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    totalcounter=0
    candidates = []
    totals = []
    unique = []
    count = 0
    
    # Read each row of data after the header
    for row in csvreader:
        totalcounter +=1
        candidates.append(row[2])
    
    # Sort candidates list
    candidates.sort()
    
    # Append placeholder to accommodate count loops
    candidates.append("Placeholder")

    # Dynamic counting of candidate votes
    for x in candidates:
        if x not in unique:
            unique.append(x)
            count +=1
            totals.append(count)
            count = 0
        else: 
            count +=1
    totals.pop(0)
    unique.pop(-1)

# combine = zip(unique, totals)

# combinedlist = list(combine)

# Max votes to use in for loop to find winner
maxvotes = max(totals)

# Using for loop to find winner using index method
for x in totals:
    if x == maxvotes:
        y = totals.index(x)
        winner = unique[1]

# Calculate percentages of votes
khanpercent = round(float(((totals[1])/totalcounter)*100), 2)
correypercent = round(float(((totals[0])/totalcounter)*100), 2)
lipercent = round(float(((totals[2])/totalcounter)*100), 2)
tooleypercent = round(float(((totals[3])/totalcounter)*100), 2)

print("                               ")
print("Election Results")
print("---------------------")
print(f"Total Votes: {totalcounter}")
print("---------------------")
print(f"Khan: {khanpercent}% ({totals[1]})")
print(f"Correy: {correypercent}% ({totals[0]})")
print(f"Li: {lipercent}% ({totals[2]})")
print(f"O'Tooley: {tooleypercent}% ({totals[3]})")
print("---------------------")
print(f"Winner: {winner}")
print("---------------------")
