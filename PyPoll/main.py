import csv
import os

#assign variables to paths
election_csv = os.path.join('/Users/meganflinders/Desktop/Bootcamp/Repos/Python_challenge/python_challenge/PyPoll/Resources/election_data.csv')
election_results = os.path.join('/Users/meganflinders/Desktop/Bootcamp/Repos/Python_challenge/python_challenge/PyPoll/analysis/election_results.txt')
#declare and initialize variables
total_votes = 0
#create dictionary with candidate as key and vote count as value
candidate_votes = {}
#create variables for winning candidate, vote count and percentage
winner = ""
winning_votes = 0
winning_percentage = 0


#open election results
with open(election_csv) as csvfile:
    #read results
    csvreader = csv.reader(csvfile)
    #skip header
    next(csvreader)
    #loop through csv
    for row in csvreader:
        #find total votes
        total_votes += 1
        #locate data for candidate name
        candidate = row[2]
        #add to vote count of candidate if alreading in candidate_votes, otherwise add candidate to dict with value 1
        if candidate in candidate_votes:
            candidate_votes[candidate] += 1
        else:
            candidate_votes[candidate] = 1
#print data from first loop and save in txt file
print("Election Results\n"
      "___________________________\n"
      f"Total Votes: {total_votes}\n"
      "___________________________\n")
with open(election_results, "w") as f:
    f.write("Election Results\n"
            "___________________________\n"
            f"Total Votes: {total_votes}\n"
            "___________________________\n")
#loop through candidates to find total votes for each
    for candidate, votes in candidate_votes.items():
        candidate_votes[candidate] = votes
        #calculate percentage of the vote each candidate received
        vote_percentage = round((votes / total_votes) * 100, 3)
        #print results and save in txt file
        print(f'{candidate}: {vote_percentage}% ({votes})')
        f.write(f'{candidate}: {vote_percentage}% ({votes})\n')
    f.write("___________________________\n")
    print("___________________________")
    #loop through candidates again to find candidate with the max number of votes
    for candidates,votes in candidate_votes.items():
        winner = max(candidate_votes, key= lambda candidate: candidate_votes[candidate])
    #print the winner and save to txt file
    print(f"Winner: {winner}\n"
          "___________________________")
    f.write(f"Winner: {winner}\n"
            "___________________________")
