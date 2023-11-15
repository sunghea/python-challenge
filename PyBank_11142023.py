import os
import csv

# Set the path to the CSV file
csvpath = r'C:\Users\user\Downloads\Bootcamp\Starter_Code (3)\Starter_Code\PyBank\Resources\budget_data.csv'


# Initialize variables to store results
total_months = 0
net_total = 0
previous_profit_loss = None
monthly_changes = []  # List to store monthly profit/loss changes
months = []  # List to store corresponding months

# Initialize variables for the greatest increase in profits
greatest_increase = 0
greatest_increase_month = ""
greatest_decrease = 0
greatest_decrease_month = ""

# Read and print the first few lines of the CSV file
with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    next(csvreader, None)

    # Print csv file 
    #for  row in enumerate(csvreader):
    #            print(row)

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])
        profit_loss = int(row[1])

   # Calculate monthly profit/loss changes
        if previous_profit_loss is not None:
            monthly_change = profit_loss - previous_profit_loss
            monthly_changes.append(monthly_change)

            # Check if this month had the greatest increase in profits
            if monthly_change > greatest_increase:
                greatest_increase = monthly_change
                greatest_increase_month = row[0]
            # Check if this month had the greatest decrease in profits
            if monthly_change < greatest_decrease:
                greatest_decrease = monthly_change
                greatest_decrease_month = row[0]

        previous_profit_loss = profit_loss
    
# Calculate the average change
average_change = sum(monthly_changes) / len(monthly_changes)

# Print the total number of months, net total, and average change
print(f"The total number of months included in the dataset: {total_months}")
print(f"The net total amount of Profit/Losses over the entire period: ${net_total}")
print(f"The average change in Profit/Losses over the entire period: ${average_change:.2f}")

# Print the greatest increase in profits (date and amount)
print(f"The greatest increase in profits occurred in {greatest_increase_month} with an amount of $({greatest_increase})")
# Print the greatest decrease in profits (date and amount)
print(f"The greatest decrease in profits occurred in {greatest_decrease_month} with an amount of $({greatest_decrease})")

# Save the results to a text file
output_file = "financial_analysis3.txt"
with open(output_file, "w") as textfile:
    textfile.write("Financial Analysis\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Total Months: {total_months}\n")
    textfile.write(f"Total: ${net_total:.2f}\n")
    textfile.write(f"Average Change: ${average_change:.2f}\n")
    textfile.write(f"Greatest Increase in Profits: {greatest_increase_month} (${greatest_increase})\n")
    textfile.write(f"Greatest Decrease in Profits: {greatest_decrease_month} (${greatest_decrease})\n")

print("Results have been saved to 'financial_analysis.txt3'.")