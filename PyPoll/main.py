import os
import csv
from csv import reader
from operator import itemgetter

votes = 0
winner_votes = 0
total_candidates = 0
candidates = []
candidate_votes = {}

election = os.path.join(os.path.sep, 'Users/apetek/Desktop/Github/python-challange/PyPoll/Resources/election_data.csv')
with open(election, newline="") as csvfile:
    reader = csv.reader(csvfile)

    for row in reader:
        votes = votes + 1
        total_candidates = row[2]        

        if row[2] not in candidates:
            
            candidates.append(row[2])

            candidate_votes[row[2]] = 1
            
        else:
            candidate_votes[row[2]] = candidate_votes[row[2]] + 1

    print("Election Results")
    print("-------------------------")
    print("Total Votes " + str(votes))
    print("-------------------------")
#results
    for candidate in candidate_votes:
        print(candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 
        candidate_results = (candidate + " " + str(round(((candidate_votes[candidate]/votes)*100))) + "%" + " (" + str(candidate_votes[candidate]) + ")") 

winner = sorted(candidate_votes.items(), key=itemgetter(1), reverse=True)

#results
print("-------------------------")
print("Winner: " + str(winner[0]))
print("-------------------------")