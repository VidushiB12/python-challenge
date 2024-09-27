import csv
import os

#Building file path
filepath=os.path.join('Resources', 'election_data.csv')

#Opening and Reading CSV file
with open(filepath, 'r') as textfile:
    csvreader=csv.reader(textfile, delimiter=',')
    csvheader=next(csvreader)

    #Defining and Assigning variables and lists. I have added Z in candidate list so that I can the person who voted. 
    vote=0
    candidate_count=1
    candidates=["Z"]
    unique_candidates_list=[]
    vote_list=[]
    percentage_list=[]
    
    #Looping through each row and adding each the candidate name to candidates list
    for rows in csvreader:
        vote=vote+1
        candidates.append(rows[2])
    
    #Sorting the data in ascending order
    candidates.sort()

    #Looping through the candidates list and checking if the items are equal. 
    # If not, the name is being added to unique candidate list and the count is also stored in vote list.
    for i in range(len(candidates)-1):
        if candidates[i+1]==candidates[i]:
            candidate_count=candidate_count+1


        else:
            unique_candidates_list.append(candidates[i])
            vote_list.append(candidate_count)
            candidate_count=1

    #Looping throug the vote list and calculating the percentage. Then adding it to percentage list
    for j in range(len(vote_list)):
        percentage_value=round((vote_list[j]/vote)*100,3)
        f_percentage_value=f"{percentage_value}%"
        percentage_list.append(f_percentage_value)

    #Finding max percentage and the winner
    max_percentage=max(percentage_list)
    winner=unique_candidates_list[percentage_list.index(max_percentage)]

    #Printing the results
    print(f"Total votes: {vote}")

    for j in range(len(vote_list)):
        print(f"{unique_candidates_list[j]}: {percentage_list[j]} ({vote_list[j]})")

    print(f"Winner: {winner}")
    
    #Building file path for new file results.csv
    filepath2=os.path.join('analysis','results.txt')

    with open(filepath2, 'w') as textfile2:
        textfile2.write(f"Total Votes: {vote}\n\n")
            
        for j in range(len(vote_list)):
            textfile2.write(f"Candidate: {unique_candidates_list[j]}, Percentage: {percentage_list[j]}, Votes: {vote_list[j]}\n")
        
        textfile2.write(f"\nWinner: {winner}")

    
        


        
    






    



    


