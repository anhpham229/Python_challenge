import os
import csv

file_to_load = os.path.join("Resources/election_data.csv")
file_to_output = os.path.join("Resources/election_analysis.txt")

total_votes = 0
with open (file_to_load) as csvfile:
    csv_reader = csv.reader(csvfile)
    csvheader = next(csv_reader)
    for row in csv_reader:
        total_votes += 1
print("Total Votes:" + str(total_votes))

                    