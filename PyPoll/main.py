import os
import csv
from csv import reader

votes = 0
winner_votes = 0
total_candidates = 0
candidate_votes = {}

election = os.path.join("Resources", "election_data.csv")