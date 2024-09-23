import csv
import os

#Building file path
filepath=os.path.join('Resources', 'budget_data.csv')

#Opening and Reading CSV file
with open(filepath, 'r') as textfile:
    csvreader=csv.reader(textfile, delimiter=',')
    csvheader=next(csvreader)

#Defining and Assigning variables
    totalmonths=0
    total=0
    profit_loss_list=[]
    date_list=[]
    sum_change=0
    change_list=[]

#Looping through each row in the CSV file
    for rows in csvreader:
        totalmonths=totalmonths+1
        total=total+int(rows[1])
        profit_loss_list.append(rows[1])
        date_list.append(rows[0])
    
    #Calculating monthly change, finding the sum of changes and putting the monthly change amount in a list 
    for i in range(len(profit_loss_list)-1):
        monthly_change=int(profit_loss_list[i+1])-int(profit_loss_list[i])
        sum_change=sum_change+ monthly_change
        change_list.append(monthly_change)

        #Finding max element of the change list, getting the index and finding corresponding date in date list.
        profit_increase=max(change_list)
        profit_index=change_list.index(max(change_list))
        profit_date=date_list[profit_index+1]


        profit_decrease=min(change_list)
        loss_index=change_list.index(min(change_list))
        loss_date=date_list[loss_index+1]

    #Calculating the average change      
    average_change=round(sum_change/(totalmonths-1),2)

    
    #Printing all required results
    max_profit=f"{profit_date} (${profit_increase})"
    min_profit=f"{loss_date} (${profit_decrease})"

    print(f"Total Months: {totalmonths}")
    print(f"Total: ${total}")
    print(f"Average Change: ${average_change}")
    print(f"Greatest Increase in Profits: {max_profit}")
    print(f"Greatest Decrease in Profits: {min_profit}")

    #Building results file path
    filepath2=os.path.join('analysis', 'Results.csv')

    #Opening and exporting results to new text file called Results.csv
    with open(filepath2, 'w', newline='') as textfile2:
        csvwriter=csv.writer(textfile2, delimiter=',')
        csvwriter.writerow(["Total Months", "Total", "Average Change", "Greatest Increase in Profits", "Greatest Decrease in Profits"])
        csvwriter.writerow([totalmonths, total, average_change, max_profit, min_profit])





    