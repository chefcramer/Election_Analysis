#The data we need to retrieve.
#1. THe total number of votes cast
#2. A complete list of canididates who recived votes
#3. The percentage of votes that each candidate won
#4. The total numbers of votes each candidate won
#5. The winner of the election based on popular vote

#add our dependencies (programming script that lets us do things without writing our own code)
import csv
import os
#assign a varaiable for the file to load and the path
file_to_load = os.path.join("resources", "election_results.csv")
#create a filename variable to a direct or indriect path to the file
file_to_save = os.path.join ("analysis", "election_analysis.txt")

#1. initialize a total vote counter.
total_votes = 0

#Candidate Options and canidate votes
candidate_options = []
#Declare the empty dictionary
candidate_votes = {}

#winning Candidate and winning count tracker
winning_candidate = ""
winning_count = 0
winning_percentage = 0

#open the election results and read the file
with open(file_to_load) as election_data:
     #to do: read and analyze the data here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read the header row.
    headers = next(file_reader)
    
    #print each row in the CSV file
    for row in file_reader:
        #2. add to the total vote count.
        total_votes += 1

        #print the candidate name for each row
        candidate_name = row [2]

        #if the candidate does not match any existing candidate...
        if candidate_name not in candidate_options:
            #add it to the list of candidates
            candidate_options.append(candidate_name)
            #begin tracking that candidate's vote count
            candidate_votes[candidate_name] = 0
        #add a vote to that candidte's count
        candidate_votes[candidate_name] += 1

#determine the percentage of voters for each candidate by looping through the count of votes
#iterate through the candidate list
for candidate_name in candidate_votes:
    #retrieve vote count of a candidate
    votes = candidate_votes[candidate_name]
    #Calculate the percentage of votes
    vote_percentage = float(votes) / float(total_votes) * 100

    #print out each candidate's name, vote count, and percentage of votes to the terminal
    print(f"{candidate_name}: {vote_percentage:.1f}% ({votes:,})\n")

    #determine winning vote count and candidate
    #determine if the votes is greater than the winning count.
    if (votes > winning_count) and (vote_percentage > winning_percentage):
        #if true then set winning_count = votes and winning_percent = vote_percentage
        winning_count = votes
        winning_percentage = vote_percentage
        #and, set the winning candidate equal to the candidates name
        winning_candidate = candidate_name
    #printing the winning candidate info
    winning_candidate_summary = (
        f"-----------------------------\n"
        f"Winner: {winning_candidate}\n"
        f"Winning Vote Count: {winning_count:,}\n"
        f"Winning Percentage: {winning_percentage:.1f}%\n"
        f"-----------------------------\n")
    print(winning_candidate_summary)

    #print the candidate name and percentage of votes
    #print (f"{candidate_name}: received {round(vote_percentage,1)}% of the vote.")

#print the candidate vote dictionary
#print(candidate_votes)

#Print the total votes
#print(total_votes)

#using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #write some data to the file
    txt_file.write("Hello World!\n")
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    #write three counties to the file, \n is a line break, an "enter"
    txt_file.write("Arapahoe\nDenver\nJefferson")
