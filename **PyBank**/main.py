import os
import csv

pybankCSV = os.path.join('budget_data.csv')

with open(pybankCSV, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    print(csvreader)

    # Read the header row first
    csv_header = next(csvreader)

    # Initialize counters and lists
    counter=0
    add=0
    profits = []
    deltas = []
    months = []
    
    # Read each row of data after the header
    for row in csvreader:
        counter +=1
        add +=int(row[1])
        profits.append(int(row[1]))
        months.append(str(row[0]))
    
    # Append deltas list, and calculate average change
    for x in range(1,len(profits)):
        deltas.append(int(profits[x]) - int(profits[x-1]))
    
    averagechange = round((sum(deltas))/(len(deltas)), 2)

# Find max month
max = 0
for y in deltas:
    if y > max:
        max = y
        z = deltas.index(y)
        maxmonth = months[z+1]

# Find min month
min = 0
for y in deltas:
    if y < min:
        min = y
        r = deltas.index(y)
        minmonth = months[r+1]

# Print to terminal
print("                              ")
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {counter}")
print(f"Total: ${add}")
print(f"Average Change: ${averagechange}")
print(f"Greatest Increase in Profits: {maxmonth} (${max})")
print(f"Greatest Increase in Profits: {minmonth} (${min})")
print("---------------------")

# Print to txt file
output = open('PyBankResults.txt', 'w')
print("                              ", file=output)
print("Financial Analysis", file=output)
print("---------------------", file=output)
print(f"Total Months: {counter}", file=output)
print(f"Total: ${add}", file=output)
print(f"Average Change: ${averagechange}", file=output)
print(f"Greatest Increase in Profits: {maxmonth} (${max})", file=output)
print(f"Greatest Increase in Profits: {minmonth} (${min})", file=output)
print("---------------------", file=output)
output.close()