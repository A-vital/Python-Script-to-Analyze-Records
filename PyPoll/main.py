import os
import csv
from csv import reader

votes = 0
winner_votes = 0
total_candidates = 0
candidate_votes = {}

election = os.path.join("Resources", "election_data.csv")
with open(election, newline="") as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        votes = votes + 1
        total_candidates = row["Candidate"]        

        if row["Candidate"] not in candidate_options:
            
            candidate_options.append(row["Candidate"])

            candidate_votes[row["Candidate"]] = 1
            
        else:
            candidate_votes[row["Candidate"]] = candidate_votes[row["Candidate"]] + 1