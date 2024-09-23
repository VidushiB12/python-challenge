Working with PyBank and budget data CSV file:
     The lines of codes in main.py work as follows:
        1. Opens and reads budget_data.csv file

        2. To find the total months, I created a for loop that will loop through each row and adds 1 to total months each iteration.

        3. To find the total profit/loss, I used the same for loop that will loop through row and adds up the profit/loss value each interation.

        4. To calculate average changes, I first calculated the monthly change and stored in a change_list.

            -I stored both the values for date in each row in a date list and the profit/loss values in a profit_loss list.

            -The monthly change is calculated by computing the difference in the values in the list which I also stored in another list called change_list to find min and max profit.

            -The average change is calculated by adding all the monthly changes and dividing it by 85 because we start taking from Feb.

        5. I used the change list to and found the min and max for greatest decrease and increase in profit. I also used the date list to find the dates using index function. 

        6. I then exported the results to a new text file.


Working with PyPoll and election_data CSV file:
    The lines of codes in main.py work as follows:
        1. Opens and reads election_data.csv file

        2. To find total votes, I looped through the CSV file and added 1 to the vote variable when it looped through each rows.

        3. Looping through each row, I stored the candidates name in a list called candidates. I have added an item Z in that list so that it appears at the end after sorting and can fulfill the criteria that it is not equal to the last candidate name.

        4. To get the votes for each candidate, I created a loop for the candidates list and it counts it when the items are equal.

        5. I also created a unique candidate list whoich contains the unique names. When the critera is not satisfied, it goes into that list and the candidate count is reset to 1.

        6. I have created a vote list which stores the count of each candidate and calculated the percentage for each one. This is also stored in the percentage list.

        7. The winner is the one with the greatest percentage of votes, hence I found the max item of the percentage list.

        8. The results have been printed accordingly and exported to a new text file called results.csv.
