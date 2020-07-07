import os
import csv

#add path
csv_path = os.path.join("Resources", "Budget_Data.csv")

#find profit/loss
profit = 0
months = 0
profit_changes = []
avg_change = 0
previous_month = 0
Greatest_increase = []
Greatest_decrease = []
max_value = []
    
#open file
with open(csv_path, 'r') as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    
    csv_header = next(csvreader)
    
    for row in csvreader:
        profit += int(row[1])
        months += 1
        
        if(avg_change >= 1):
            profit_changes.append(int(row[1])-previous_month)
            previous_month = int(row[1])
        else: 
            previous_month = int(row[1])
            avg_change += 1  
            
max_val = max(profit_changes)
min_val = min(profit_changes)
file_run = open("C:\\Users\\whitn\\Python-Challenge\\Python-Challenge\\PyBank\\Analysis\\budget_data.txt", "w")       
print("Finnacial Analysis")
file_run.write("Finnancial Analysis\n")
print("....................................")
file_run.write(".............................\n")
print("Total Months:", months)
file_run.write("Total Months:" + str(months) + "\n")
print("Total:", "$", profit)
file_run.write("Total:" + "$" + str(profit) + "\n")
print("Average Change:", round(sum(profit_changes) / len(profit_changes),2))
file_run.write("Average Change:" + str(round(sum(profit_changes) / len(profit_changes),2)) + "\n")
print("Greatest Increase In Profit:", max_val)
file_run.write("Greatest Increase In Profit:" + str(max_val) + "\n")
print("Greatest Decrease In Profit:", min_val)
file_run.write("Greatest Decrease In Profit:" + str(min_val) + "\n")
file_run.close()

          
                                                     
                    
                                                                         
    
    