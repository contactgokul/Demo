import os
import csv

csvpath = os.path.join("cereal_bonus.csv")
# Open the file using "write" mode. Specify the variable to hold the contents
with open(csvpath, newline='') as csvfile:

    # CSV reader specifies delimiter and variable that holds contents
    csvreader = csv.reader(csvfile, delimiter=',')

    #print(csvreader)

    # Read the header row first (skip this step if there is now header)
    #csv_header = next(csvreader, None)
    #print(f"CSV Header: {csv_header}")

    # Read each row of data after the header
    for row in csvreader:
        if float(row[7]) >= 5:
            #print(row[0], row[7])
            print(row)