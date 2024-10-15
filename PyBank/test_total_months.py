# Files to load and output (update with correct file paths)
import csv
import os
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    total_months = sum(1 for row in reader)
    print("Total Months: " + str(total_months))
