import os
import csv

# Path to the budget data file
py_bank = os.path.join("PyBank/Resources/budget_data.csv")

# Initialize variables
month_count = 0
total_profits = 0
profit_changes = []
dates = []
profits = []

# Open the CSV file
with open(py_bank) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Read each row in the CSV file
    for row in csvreader:
        # Extract date and profit/loss values
        date = row[0]
        profit = int(row[1])

        # Update total profits and count of months
        total_profits += profit
        month_count += 1

        # Append date and profit to respective lists
        dates.append(date)
        profits.append(profit)

# Calculate the changes in profits
for i in range(1, len(profits)):
    profit_change = profits[i] - profits[i - 1]
    profit_changes.append(profit_change)

# Find the index of the greatest increase in profits
max_increase_index = profit_changes.index(max(profit_changes))
max_decrease_index = profit_changes.index(min(profit_changes))

# Get the date corresponding to the greatest increase
greatest_increase_date = dates[max_increase_index + 1]
greatest_decrease_date = dates[max_decrease_index + 1]
# Calculate the average change, greatest increase, and greatest decrease in profits
average_change = sum(profit_changes) / len(profit_changes)
greatest_increase = max(profit_changes)
greatest_decrease = min(profit_changes)

# Print the financial analysis
print("Financial Analysis")
print("-----------------------------------------------")
print(f"Total Months: {month_count}")
print(f"Total: ${total_profits}")
print(f"Average Change: ${average_change:.2f}")
print(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})")
print(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})")

#With a LOT of help from Xperience assistant.

# Path to the output file
output_file = os.path.join("../python_challenge/Analysis/financial_analysis.txt")

# Write the financial analysis results to a text file
with open(output_file, "w") as file:
    file.write("Financial Analysis\n")
    file.write("-----------------------------------------------\n")
    file.write(f"Total Months: {month_count}\n")
    file.write(f"Total: ${total_profits}\n")
    file.write(f"Average Change: ${average_change:.2f}\n")
    file.write(f"Greatest Increase in Profits: {greatest_increase_date} (${greatest_increase})\n")
    file.write(f"Greatest Decrease in Profits: {greatest_decrease_date} (${greatest_decrease})\n")






