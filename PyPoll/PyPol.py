#The data we need to retrieve
#Assign a variable for the file to load and the path
from os import close


file_to_load = 'Resources/election_results.csv'

import csv
import os
# Assign a variable for the file to load and the path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# 1a. Initialize a total vote counter
total_votes = 0
# 2a. Declare a new list
candidate_options = []
# 3a. Declare a new dictionary for votes for each candidate
candidate_votes = {}
# 5a. Create variables Winning Candidate and Winning Count Tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0    

# Open the election results and read the file.
with open(file_to_load) as election_data:
    file_reader = csv.reader(election_data)

    # Read the header row.
    headers = next(file_reader)

    # Print each row in the CSV file.
    for row in file_reader:
        # 1b. Add to the total vote count
        total_votes += 1

        # 2b. Print the candidate name from each row.
        candidate_name = row[2]
        
        # 2e. Add if statement to see if candidate does not match existing candidate
        if candidate_name not in candidate_options:
            # 2c. Add the candidate name to the candidate list.
            candidate_options.append(candidate_name)

            # 3b. Add candidates to the candidate votes dictionary
            candidate_votes[candidate_name] = 0

        # 3d. Add a vote to that candidate's count.
        candidate_votes[candidate_name] += 1


# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

 # Print the final vote count to the terminal.
    election_results = (
        f"\nElection Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes:,}\n"
        f"-------------------------\n")
    print(election_results, end="")
    # Save the final vote count to the text file.
    txt_file.write(election_results)   

    # 4a. Iterate through candidate to start calculating voting percentage
    for candidate_name in candidate_votes:
        # 4b. Retrieve vote count of a candidate
        votes = candidate_votes[candidate_name]
        # 4c. Calculate the percentage of votes.
        vote_percentage = float(votes) / float (total_votes)*100
        # 4e. Print the candidate vote dictionary
        # To do: print out each candidate's name, vote count, and percentage of
        # votes to the terminal.
        candidate_results = (f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

        # Print each candidate, their voter count, and percentage to the terminal.
        print(candidate_results)
        #  Save the candidate results to our text file.
        txt_file.write(candidate_results)

    # 5b. Determine winning vote count and candidate
    # 5c. Determine if the votes are greater than the winning count.
        if (votes > winning_count) and (vote_percentage > winning_percentage):
            # 5d. If true then set winning_count = votes and winning_percent =
            # vote_percentage.
            winning_count = votes
            winning_percentage = vote_percentage
            # 5e. Set the winning_candidate equal to the candidate's name.
            winning_candidate = candidate_name


    winning_candidate_summary = (
        f"-------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-------------------------\n")
        
    print(winning_candidate_summary) 
    # Save the winning candidate's results to the text file.
    txt_file.write(winning_candidate_summary)  
