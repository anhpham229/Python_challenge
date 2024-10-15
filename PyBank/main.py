# Dependencies
import csv
import os

# Files to load and output (update with correct file paths)
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

# Define variables to track the financial data
total_profit_lost = 0
total_months = 0
change_list = []
previous_profit_lost = None

# Open and read the csv
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)

     # Skip the header row
    header = next(reader)
    first_row = next(reader)

    # Extract first row to avoid appending to net_change_list
    total_months += 1
    previous_profit_lost = int(first_row[1])
    total_profit_lost += previous_profit_lost

     # Track the total and net change

     # Process each row of data
    for row in reader:

        # Track the total
        total_months += 1
        current_profit_lost = int(row[1])
        total_profit_lost += current_profit_lost

         # Track the net change
        change = current_profit_lost - previous_profit_lost
        change_list.append((row[0], change))
        previous_profit_lost = current_profit_lost

        # Calculate the greatest increase in profits (month and amount)
        greatest_increase = max(change_list, key=lambda x: x[1])

        # Calculate the greatest decrease in losses (month and amount)
        greatest_decrease = min(change_list, key=lambda x: x[1])
total_change = sum(change[1] for change in change_list)

# Calculate the average net change across the months
average_change =  round(total_change / len(change_list),2)

# Print the output

print("Total Months: " + str(total_months))
print("Total: " + "$" + str(total_profit_lost))
print("Average Change: " + "$" + str(average_change))
print("Greatest Increase in Profits: " + "$" + str(greatest_increase))
print("Greatest Decrease in Profits: " + "$" + str(greatest_decrease)) 
        
    # Write the results to a text file
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"""
                   Financial Analysis
                   
                   ----------------------------
                   
                   Total Months: {total_months}
                   Total: ${total_profit_lost}
                   Average Change: ${average_change}
                   Greatest Increase in Profits: ${greatest_increase}
                   Greatest Decrease in Profits: ${greatest_decrease}""")