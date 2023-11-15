import os
import csv


total_votes = 0
candidates_set = set()
# Initialize a dictionary to store the votes for each candidate
candidate_votes = {}

# Initialize a variable to store the total number of votes cast
total_votes = 0

# Set the path to the CSV file
csvpath = r'C:\Users\user\Downloads\Bootcamp\Starter_Code (3)\Starter_Code\PyPoll\Resources\election_data.csv'

with open(csvpath, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=',')

    # Skip the header
    next(csvreader, None)

    # Count the votes for each candidate and calculate the total number of votes
    for row in csvreader:
        candidate = row[2]
        total_votes += 1

        if candidate in candidate_votes:
           candidate_votes[candidate] += 1
        else:
           candidate_votes[candidate] = 1

# Find the winner of the election based on popular vote
winner = max(candidate_votes, key=candidate_votes.get)

# Print the total number of votes cast
print(f"The total number of votes cast: {total_votes}\n")

# Print a complete list of candidates who received votes
print("A complete list of candidates who received votes:")
for candidate in candidate_votes.keys():
    print(candidate)

# Print the percentage of votes each candidate won
print("\nThe percentage of votes each candidate won:")
for candidate, votes in candidate_votes.items():
    percentage = (votes / total_votes) * 100
    print(f"{candidate}: {percentage:.2f}%")

# Print the total number of votes each candidate won
print("\nThe total number of votes each candidate won:")
for candidate, votes in candidate_votes.items():
    print(f"{candidate}: {votes}")

# Print the winner of the election based on popular vote
print("\nThe winner of the election based on popular vote is:")
print(winner)

# Save the results to a text file
output_file = "Election_Results.txt"
with open(output_file, "w") as textfile:
    textfile.write("Election Results\n")
    textfile.write("----------------------------\n")
    textfile.write(f"{candidate}: {percentage:.3f}% ({votes}\n")
    textfile.write("----------------------------\n")
    textfile.write(f"Winner: {winner}\n")
   
print("Results have been saved to 'Election_Results.txt'.")