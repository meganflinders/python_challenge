import os
import csv
budget_csv = os.path.join('/Users/meganflinders/Desktop/Bootcamp/Repos/Python_challenge/python_challenge/PyBank/Resources/budget_data.csv')
financial_analysis = os.path.join('/Users/meganflinders/Desktop/Bootcamp/Repos/Python_challenge/python_challenge/PyBank/analysis/financial_analysis.txt')

# assign variables
row_count = 0
net_total = 0
previous_revenue = 0
change_list = []
month_change = []
revenue_change = 0
average_change = 0



print("Financial Analysis\n"
      "-------------------------------------")

with open(budget_csv) as csvfile:
    csvreader = csv.reader(csvfile)
    #skip the header row
    next(csvreader)
    #loop through csv 
    for row in csvreader:
        #find total number of months from number of rows in data
        row_count += 1
        #find net total profit/losses
        net_total = net_total + int(row[1])
        #find change in profit/losses between months
        if previous_revenue == 0:
            revenue_change = 0
        else:
            revenue_change = int(row[1]) - previous_revenue
        #update prevous revenue
        previous_revenue = int(row[1])
        #add revenue change to change list
        change_list.append(revenue_change)
        #add month of change to month of change list
        month_change.append(row[0])
    #find average change of profit/losses; divide by length of change list -1 since there is no change in the first month
    average_change = float(round(sum(change_list) / (len(change_list) - 1), 2))

#print total months, net total and average change
print(f'Total months: {row_count}\n'
      f'Total: ${net_total}\n'
      f'Average change: ${average_change}')

#export text file with results
with open(financial_analysis, "w") as f:
    f.write("Financial Analysis\n"
            "-------------------------------------\n")
    f.write("Total months: %d\n" % row_count)
    f.write("Total: $%d\n" % net_total)
    f.write("Average change: $%s\n" % str(average_change))

    #zip the month_change list and the change_list together into a dictionary
    change_per_month = dict(zip(month_change, change_list))
    #find the maximum change from the dictionary
    max_change = max(change_per_month.values())
    #find the minimum change from the dictionary
    min_change = min(change_per_month.values())
    #loop through dict to find the keys of the values that = the max and min
    for month in change_per_month.keys():
        #find key-value in dict that = min and max change; print and save to txt file
        if change_per_month[month] == min_change:
            print(f'Greatest Decrease in Profits: {month} (${change_per_month[month]})')
            f.write(f'Greatest Decrease in Profits: {month} (${change_per_month[month]})\n')
        if change_per_month[month] == max_change:
            print(f'Greatest Increase in Profits: {month} (${change_per_month[month]})')
            f.write(f'Greatest Increase in Profits: {month} (${change_per_month[month]})\n')

    

