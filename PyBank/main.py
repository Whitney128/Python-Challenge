import os
import csv

#add path
csv_path = os.path.join("Resources", "Budget_Data.csv")
#open file
with open(csv_path, nextline) as csvfile:
    csvreader =csvreader(csvfile, delimeter=",")
    csv_header = next(csvfile)
    
    print(f"header: {Finnancial Analysis}")
    
    #Find Profit, Loss and how many months
    Profit = []
    Loss = []
    Months = []
    
    # each row count
    Profit.append(row[2])
    Months.append(row[1])
    
    #find profit/loss change
    profit_change = []
    loss_change = []
    
    for x in range(1, len(Profit)):
        profit_change.append((int(Profit[x])- int(Profit[x-1])))
        
    #average profit change
        profit_change = sum(profit_change) / len(profit_change)
        
    #total months 
    total_months = len(months)
    