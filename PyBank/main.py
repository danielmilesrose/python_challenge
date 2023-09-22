import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'budget_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip headers
    headers = next(csvreader)
    # Create month list
    months = []
    # Create revenue list
    revenue = []
    # Create list for revenue change calculations
    rev_change = []

    # Iterate through and extract data from CSV to lists for counting total months/revenues
    for row in csvreader:
        months.append(row[0])
        revenue.append(int(row[1]))
    # Iterate through revenues and calculate change in revenue month to month, add to list   
    for i in range(len(revenue)-1):
        rev_change.append(revenue[i+1]-revenue[i])

# Definitions for final calculations
# Find greatest increase total in revenue list
greatest_increase = max(rev_change)
# Find greatest decrease total in revenue list
greatest_decrease = min(rev_change)
# Find position in list of greatest increase, add one to calculate correct position of month in list
month_of_increase = rev_change.index(max(rev_change))+1
# Find position in list of greatest decrease, add one to calculate correct position of month in list
month_of_decrease = rev_change.index(min(rev_change))+1

# Print final analysis to Terminal
print("Financial Analysis")
print("----------------------------")
# Calculate total months
print(f"Total Months: {len(months)}")
# Calculate total of revenue list 
print(f"Total: ${sum(revenue)}")
# Calculate average change, formatted as $ and rounded to two decimal places
print(f"Average Change: {round(sum(rev_change)/len(rev_change), 2)}")
# Print the month of the greatest profit increase and the value for greatest increase
print(f"Greatest Increase in Profits: {months[month_of_increase]} (${str(greatest_increase)})")
# Print the month of the greatest profit decrease and the value for greatest decrease
print(f"Greatest Decrease in Profits: {months[month_of_decrease]} (${str(greatest_decrease)})")

# Export results to a text file in Analysis folder
# Define path to text file folder
textfile = os.path.join('Analysis', 'PyBank_Final_Analysis.txt')
# Create text file and write findings to file
with open(textfile, mode = "w+") as final_analysis:
    final_analysis.write("Financial Analysis\n")
    final_analysis.write("----------------------------\n")
    final_analysis.write(f"Total Months: {len(months)}\n")
    final_analysis.write(f"Total: ${sum(revenue)}\n")
    final_analysis.write(f"Average Change: {round(sum(rev_change)/len(rev_change), 2)}\n")
    final_analysis.write(f"Greatest Increase in Profits: {months[month_of_increase]} (${str(greatest_increase)})\n")
    final_analysis.write(f"Greatest Decrease in Profits: {months[month_of_decrease]} (${str(greatest_decrease)})")
    final_analysis.close()
