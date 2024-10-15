import csv
import os
file_to_load = os.path.join("Resources", "budget_data.csv")  # Input file path
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path
change_list = []
previous_profit_lost = None
with open(file_to_load) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    first_row = next(reader)
    previous_profit_lost = int(first_row[1])
    for row in reader:
        current_profit_lost = int(row[1])
        change = current_profit_lost - previous_profit_lost
        change_list.append((row[0], change))
        previous_profit_lost = current_profit_lost
greatest_increase = max(change_list, key=lambda x: x[1])
greatest_decrease = min(change_list, key=lambda x: x[1])
total_change = sum(change[1] for change in change_list)
average_change =  total_change / len(change_list)

print("Greatest Increase in Profits: " + str(greatest_increase[0]) + " ($" + str(greatest_increase[1]) + ")")
print("Greatest Decrease in Profits: " + str(greatest_decrease[0]) + " ($" + str(greatest_decrease[1]) + ")")
print(f"Average change is: ${average_change:.2f}")
