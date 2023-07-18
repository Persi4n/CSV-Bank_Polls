import csv
import os

csv_path = os.path.join("PyPoll", "Resources", "election_data.csv")

total_votes = 0
candidates = {}
winner = ""

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    next(csvreader)

    for row in csvreader:
        
        total_votes += 1
        candidate_name = row[2]

        if candidate_name not in candidates:
            candidates[candidate_name] = 0

        candidates[candidate_name] += 1

max_votes = 0
for candidate, votes in candidates.items():
    percentage = (votes / total_votes) * 100
    candidates[candidate] = {"votes": votes, "percentage": percentage}
    if votes > max_votes:
        max_votes = votes
        winner = candidate





output = f"""Election Results
-------------------------
Total Votes: {total_votes}
-------------------------
"""
for candidate, data in candidates.items():
    votes = data["votes"]
    percentage = data["percentage"]
    output += f"{candidate}: {percentage:.3f}% ({votes})\n" 
output += f"""-------------------------
Winner: {winner}
"""
print(output)
