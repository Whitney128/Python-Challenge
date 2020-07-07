import os
import csv

#add path
csv_path = os.path.join("Resources", "Election_Data.csv")

#find total votes, percentage of votes per candiate, winner
votecount = 0;
candidate_vote_count = {}
candidate_vote_count_percentage = {}
name=""

#open file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    #print(csvreader)
    csv_header = next(csvreader)
    
    for row in csvreader:
        name = row[2]
        votecount = votecount+1
        total_votes = total_votes + 1
        if name in candidate_vote_count:
            vote = candidate_vote_count.get(name)
            candidate_vote_count[name] = vote+1
        else:
            candidate_vote_count[name] = 1
            
            
   
    for name in candidate_vote_count:
        candidate_vote_count_percentage = float(candidate_vote_count.get(name)/float(total_votes))*100


highest_vote = 0
winning_candidate = ""
winning_count = 0
file_run = open("C:\\Users\\whitn\\Python-Challenge\\Python-Challenge\\PyPoll\\Analysis\\election_data.txt", "w")
print("Election Results")
file_run.write("Election Results\n")
print("...................................")
file_run.write("...........................\n")
print("Total Votes:", votecount)
#file_run = open("C:\\Users\\whitn\\Python-Challenge\\Python-Challenge\\PyPoll\\election_data.txt", "w")
file_run.write("Total Votes:" + str(votecount) + "\n")
print("......................................")
file_run.write(".....................................\n")
for candidate in candidate_vote_count:
    highest_vote = candidate_vote_count.get(candidate)
    candidate_vote_count_percentage = round((highest_vote/votecount)*100,2)
    print(candidate + ":" + str(candidate_vote_count_percentage) + "%" + "(" + str(highest_vote) + ")")
    line = candidate + ":" + str(candidate_vote_count_percentage) + "%" + "(" + str(highest_vote) + ")\n"
    file_run.writelines(line)
    if(highest_vote > winning_count):
        winning_count = highest_vote
        winning_candidate = candidate
print("..........................................")
file_run.write(".............................................\n")
print("Winner:", winning_candidate)
file_run.write("Winner:" + winning_candidate + "\n")
print("....................................")
file_run.write(".........................................\n")
file_run.close()
            

            
    