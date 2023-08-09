import os
import csv

budget_data = os.path.join("Resources", "budget_data.csv")

# opev csv
with open(budget_data, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")
    csv_header = next(csvreader)
    print(f"Header: {csv_header}")
   

    # find total months, total profit/loss and average change
    month = []
    profit_loss = []
    profit_loss_changes = []

    for rows in csvreader:
        month.append(rows[0])
        profit_loss.append(int(rows[1]))


        
    for x in range(1, len(profit_loss)):
        profit_loss_changes.append(int(profit_loss[x]) - int(profit_loss[x-1]))

    (average_change) = sum(profit_loss_changes) / len(profit_loss_changes)
    average_change = round(average_change, 2)
    
    total_months = len(month)

    greatest_increase = max(profit_loss_changes)
    greatest_decrease = min(profit_loss_changes)

    file = open("results.txt", "w")
    file.write("Financial Analysis" + "\n" )
    file.write("----------------------------" + "\n")
    file.write("Total_Months: " + str(total_months) + "\n")
    file.write("Total: " + "$" + str(sum(profit_loss)) + "\n")
    file.write("Average Change: " + "$" + str(average_change) + "\n")
    file.write("Greatest Increase in Profits: " + str(month[profit_loss_changes.index(max(profit_loss_changes))+1]) + " ($" + str(max(profit_loss_changes)) + ")" + "\n")
    file.write("Greatest Decrease in Profits: " + str(month[profit_loss_changes.index(min(profit_loss_changes))+1]) + " ($" + str(min(profit_loss_changes)) + ")" + "\n")
    
    file.close()