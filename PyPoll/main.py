import os
import csv
from csv import reader
from operator import itemgetter

votes = 0
winner_votes = 0
total_candidates = 0
candidates = []
candidate_votes = {}

election = os.path.join("Resources", "election_data.csv")
with open(election, newline="") as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidates:
            
            candidates.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1

    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
#results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 