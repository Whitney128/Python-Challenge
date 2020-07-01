import os
import csv

#add path
csv_path = os.path.join("Resources", "Budget_Data.csv")
#open file
with open(csv_path, nextline) as csvfile:
    csvreader =csvreader(csvfile, delimeter=",")
    csv_header = next(csvfile)
    
    print(f"header: {Finnancial Analysis}")
    
    #Find Profit and Loss