import os
import csv

# Specify the file to write to
file_to_output = os.path.join("analysis", "budget_analysis.txt")  # Output file path

Total_Months = 86
Total = 20
Greatest_Increase = 30
Greatest_Decrease = 40
Average_change = 50

# Open the file using "write" mode. Specify the variable to hold the contents
with open(file_to_output, "w") as txt_file:
    txt_file.write(f"""
                   Financial Analysis
                   
                   ----------------------------
                   
                   Total Months: {Total_Months}
                   Total: ${Total}
                   Average Change: ${Average_change}
                   Greatest Increase in Profits: ${Greatest_Increase}
                   Greatest Decrease in Profits: ${Greatest_Decrease}""")
