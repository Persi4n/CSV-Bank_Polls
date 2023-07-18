import csv
import os
 
csv_path = os.path.join("PyBank", "Resources", "budget_data.csv")

total_months = 0
net_total = 0
previous_profit_loss = 0
changes = []
greatest_increase = ["", 0]
greatest_decrease = ["", 0]

with open(csv_path, newline="") as csvfile:
    csvreader = csv.reader(csvfile, delimiter=",")

    next(csvreader)

    for row in csvreader:
        total_months += 1
        net_total += int(row[1])

        current_profit_loss = int(row[1])
        if previous_profit_loss != 0:
            change = current_profit_loss - previous_profit_loss
            changes.append(change)
        previous_profit_loss = current_profit_loss
 
        if current_profit_loss > greatest_increase[1]:
            greatest_increase[0] = row[0]
            greatest_increase[1] = current_profit_loss

        if current_profit_loss < greatest_decrease[1]:
            greatest_decrease[0] = row[0]
            greatest_decrease[1] = current_profit_loss
 
average_change = sum(changes) / len(changes)


print("\nFinancial Analysis")
print("______________________________")
print(f"Total Months: {total_months}")
print(f"\nTotal: ${net_total}")
print(f"\nAverage Change: ${average_change}")
print(f"\nGreatest Increase in Profits: {greatest_increase[0]} (${greatest_increase[1]})")
print(f"\nGreatest Decrease in Profits: {greatest_decrease[0]} (${greatest_decrease[1]})")