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
       average profit_change = sum(profit_change) / len(profit_change)
        
    #total months 
    total_months = len(months)
    
    #increase/decrease
    greatest_increase = max(profit_change)
    greatest_decrease = min(profit_change)
    
    #Find Analysis
    print("Finnancial Analysis")
    
    print(".................................................................")
    
    print("total months" + str(total_months))
    
    print("average change" + str(profit_change))
    
    print("greatest increase in profit" + str(months[profit_change.index(max(profit_change))+2]) + str(greatest_increase)
    
    print("greatest_decrease in profit" + str(months[profit_change.index(min(profit_change))+2]) + str(greatest_decrease)
          
                                                     
                    
                                                                         
    
    