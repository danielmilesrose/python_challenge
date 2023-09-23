import os
import csv

# Path to collect data from the Resources folder
csvpath = os.path.join('Resources', 'election_data.csv')

with open(csvpath, encoding='UTF-8') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    # Skip headers
    headers = next(csvreader)

    # Create voter list
    voters = []
    # Create candidate list
    candidates = []

    for row in csvreader:
        # Extract voter ID data to voters list
        voters.append(int(row[0]))
        # Extract candidate names to candidate list
        candidates.append(row[2])


# Counting total votes per candidate
# Create dictionary to store frequency of each element
vote_count = {}

for votes in candidates:
    if votes in vote_count:
        vote_count [votes] += 1
    else:
        vote_count[votes] = 1


# Calculate total number of votes cast
total_votes = len(voters)

# Print header
print("Election Results")
print("-------------------------")
# Print total votes
print(f"Total Votes: {total_votes}")
print("-------------------------")

# Print standings
# Calculate number of votes per candidate
# (Format -- Candidate: Percentage to 3 decimal places (total votes))
for key, value in vote_count.items():
    print(f"{key}: {round(((value/total_votes) * 100), 3)}% ({value})")
print("-------------------------")

# Print winner using get method
winner = max(vote_count, key=vote_count.get)
print(f"Winner: {winner}")
print("-------------------------")

# Export results to a text file in Results folder
# Define path to text file folder
textfile = os.path.join('Analysis', 'PyPoll_Final_Results.txt')
# Create text file and write findings to file
with open(textfile, mode = "w+") as final_results:
    final_results.write("Election Results\n")
    final_results.write("----------------------------\n")
    final_results.write(f"Total Votes: {total_votes}\n")
    final_results.write("----------------------------\n")
    for key, value in vote_count.items():
        final_results.write(f"{key}: {round(((value/total_votes) * 100), 3)}% ({value})\n")
    final_results.write("----------------------------\n")
    final_results.write(f"Winner: {winner}\n")
    final_results.write("----------------------------\n")
    final_results.close()