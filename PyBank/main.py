#Import the necessary dependencies
import os
import csv
from csv import reader

months = 0
net_total = 0
average_changes = 0
greatest_increase = {}
greatest_decrease = {}

#Read in a csv file
budget_data = os.path.join("Resources", "budget_data.csv")
with open(budget_data) as financial_data:
    csv_reader = reader(financial_data)
    #reader = csv.reader(financial_data)
    #header = next(reader)
    #firstrow = next(reader)
    #months = months + 1
    #net_total = net
    for row in csv_reader:
        months += 1
        print(months)
        #net_total = net_total + header[1]
        #averge_changes = (net_total/months)

