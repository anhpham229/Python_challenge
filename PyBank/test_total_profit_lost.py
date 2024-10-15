import csv
import os
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
total_profit_lost = 0
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    for row in reader:
        total_profit_lost += int(row[1])
print("Total: " + "$" + str(total_profit_lost))
              