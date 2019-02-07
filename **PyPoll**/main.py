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
    khancounter=0
    correycounter=0
    licounter=0
    tooleycounter=0
    candidates = []
    
    # Read each row of data after the header
    for row in csvreader:
        totalcounter +=1
        candidates.append(row[2])
    
    # Count candidate votes
    for x in candidates:
        if x == "Khan":
            khancounter +=1
        if x == "Correy":
            correycounter +=1
        if x == "Li":
            licounter +=1
        if x == "O'Tooley":
            tooleycounter +=1

totals = [khancounter, correycounter, licounter, tooleycounter]

# Calculate percentages
khanpercent = ((khancounter)/(totalcounter))*100
correypercent = ((correycounter)/(totalcounter))*100
lipercent = ((licounter)/(totalcounter))*100
tooleypercent = ((tooleycounter)/(totalcounter))*100

winner = max(khancounter, correycounter, licounter, tooleycounter)

print("Election Results")
print("---------------------")
print(f"Total Votes: {totalcounter}")
print("---------------------")
print(f"Khan: {khanpercent}% ({khancounter})")
print(f"Correy: {correypercent}% ({correycounter})")
print(f"Li: {lipercent}% ({licounter})")
print(f"O'Tooley: {tooleypercent}% ({tooleycounter})")
print("---------------------")
print(f"Winner: {winner}")
