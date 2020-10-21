#Import the necessary dependencies
import os
import csv

months = 12
net_total = 0
average_changes = 0
greatest_increase = {}
greatest_decrease = {}

#Read in a csv file
budget_data = os.path.join("Resources", "budget_data.csv")
with open(budget_data) as financial_data:
    reader = csv.reader(financial_data)
    header = next(reader)
    print(header)

