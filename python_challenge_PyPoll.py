#Special Thanks to Xpert Learning Assistant :D
import os
import csv

# Path to the election data file
py_polls = os.path.join("PyPoll/Resources/election_data.csv")

# Initialize variables 
votes_cast = 0
votes = 0
all_votes = []
all_candidates = []
candidate_votes = {}

# Open the CSV file
with open(py_polls) as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    # Skip the header row
    next(csvreader)

    # Read each row in the CSV file
    for row in csvreader:
        # Extract votes and candidates
        candidate = row[2]

        # Update total votes cast
        votes_cast += 1

        # Append votes and candidates to respective lists
        all_votes.append(votes)
        all_candidates.append(candidate)

        # Update candidate votes
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1

winner = max(candidate_votes, key=candidate_votes.get)
winner_votes = candidate_votes[winner]


# Print the total votes and votes for each candidate
print(f"Total Votes: {votes_cast}")
print("-----------------------------------------------------------------")
for candidate, votes in candidate_votes.items():
    percentage = (votes/votes_cast)*100
    print(f"{candidate}: {percentage:.2f}% {votes} votes")
print("-----------------------------------------------------------------")
# Print the winner
print(f"Winner: {winner} with {winner_votes} votes")

output_file = os.path.join("../python_challenge/Analysis/polls_analysis.txt")

# Write the financial analysis results to a text file
with open(output_file, "w") as file:
    file.write("Election Results\n")
    file.write("-----------------------------------------------------\n")
    for candidate, votes in candidate_votes.items():
        file.write(f"{candidate}: {percentage:.2f}% {votes} votes\n")
    file.write("-----------------------------------------------------\n")
    file.write(f"Winner: {winner} with {winner_votes} votes\n")