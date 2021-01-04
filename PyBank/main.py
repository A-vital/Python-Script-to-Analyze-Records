#Import the necessary dependencies
import os
import csv
from csv import reader

months = 0
net_total = 0
average_changes = 0.0
greatest_increase = {}
greatest_decrease = {}
current_month = 0
previous_month = 0
change = 0

#Read in a csv file
budget_data = os.path.join("Resources", "budget_data.csv")
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile)
    header = next(csvreader)
    for row in csvreader :
        net_total += int(row[1])
        months += 1
        current_month = row[1]
        change = int(current_month) - int(previous_month)
        #if current month is greater than previous month add to greatest_increase 
        if int(current_month) > int(previous_month):
            #add the first element as a key and the change to greatest_increase
            greatest_increase[row[0]] = change  
        else:
            #add to greatest decrease
            greatest_decrease[row[0]] = change
        #net_total = net_total + header[1]
    average_changes = int(net_total)/int(months)
    print(f"Financial Analysis")
    print(f"---------------------")
    print(f"Total Months: {months}")
    print(f"Net Total: {net_total}")
    print(f"Average Change: {average_changes}")
    print(f"Greatest Increase in Profits: {greatest_increase}")
    print(f"Greatest Decrease in Profits: {greatest_decrease}")