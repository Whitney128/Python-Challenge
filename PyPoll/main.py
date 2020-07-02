import os
import csv

#add path
csv_path = os.path.join("Resources", "Election_Data.csv")
#open file
with open(csv_path, nextline) as csvfile:
    csvreader =csvreader(csvfile, delimeter=",")
    csv_header = next(csvfile)
    
    print(f"header": "Election Results")
    
    #find total votes, percentage of votes per candiate, winner
    total votes = []
    percentage votes Khan = []
    percentage votes Correy = []
    percentage votes Li = []
    percentage votes O'Tooley = []
    Winner = []
    
    #total votes
    total_votes = len(votes)