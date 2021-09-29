# Election_Analysis
Module 3 PyPoll with Python

## Overview of the Election Audit
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of the candidates who recieved votes.
3. Calculate the total number of votes each candidate received.
4. Calculate the percentage of votes each candidate won.
5. Determine the winner of the election based on popular vote.
6. Determine the percentage of the total votes that each county represents.
7. Determine the largest county by voter turnout.

## Resources
- Data Source: election_results.csv
- Software: Python 3.6.1, Visual Studio Code, 1.38.1

## Election Audit Results
The Audit of the election shows that:
1. There were 369,711 votes cast in the election.

   This was determined with the following string of code. This code uses a `for` loop to check every row (representing each vote) and add one vote to the total number of votes cast.
  ```
  for row in reader:
      total_votes = total_votes + 1
  ```
2. The candidates were:
   - Charles Casper Stockham
   - Diana DeGette
   - Raymon Anthony Doane

    This code builds on the `for` loop in the step above to check each row in the canidate name column and add it to a list.
```
   for row in reader:
      total_votes = total_votes + 1
      candidate_name = row[2]
      if candidate_name not in candidate_options:
         candidate_options.append(candidate_name)
```

3. The total number of votes per candidate were:
   - Charles Casper Stockham recieved 85,213 votes.
   - Diana DeGette recieved 272,892 votes.
   - Raymond Anthony Doane recieved 11,606 votes.

    This code continues to build on the `for` loop above, to begin tracking votes and adding them to the list of candidates, adding one vote for every row that contains the name of the candidate.
```
   for row in reader:
      total_votes = total_votes + 1
      candidate_name = row[2]
      if candidate_name not in candidate_options:
         candidate_options.append(candidate_name)
         candidate_votes[candidate_name] = 0
      candidate_votes[candidate_name] += 1
```
4. The percentage of the votes that each candidate won:
   - Charles Casper Stockham recieved 23.0% of the total votes.
   - Diana DeGette recieved 73.8% of the total votes.
   - Raymond Anthony Doane recieved 3.1% of the total votes.

    This string of code is using a `for` loop to take the total votes for each candidate generated in the step above and dividing it by the total number of votes calculated in the first step, and multiplying by 100, yielding the percentage.
```
   for candidate_name in candidate_votes:
      votes = candidate_votes.get(candidate_name)
      vote_percentage = float(votes) / float(total_votes) * 100
```
5. The winner of the election was:
   - Diana DeGette, who recived 73.8% of the vote and 272.892 votes.

    This code uses an `if` statement determing if the the votes the candidate recieved is greater than the minimum winning count of votes, and the votes recieved percentage is larger than the minimum winning percentage of votes, then to record the winning candidates name, the number of votes recieved and the percentage of votes recieved.
```
   if (votes > winning_count) and (vote_percentage > winning_percentage):
      winning_count = votes
      winning_candidate = candidate_name
      winning_percentage = vote_percentage
```
6. The percentage of the total votes that each county represents:
   - Jefferson County with 10.5% of the total votes, with 38,855 votes cast.
   - Denver County with 82.8% of the total votes, with 306,055 votes cast.
   - Arapahoe County with 6.7% of the total votes, with 24,801 votes cast.

    This code uses a `for` loop to look through each county and record how many votes were cast in that county, as well as calculating and recording the percentage of the total vote that has been counted in each county.
```
   for county_name in county_list:
      votes = county_votes.get(county_name)
      vote_percentage= float(votes)/float(total_votes)*100
      county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")
```
7. The largest county was:
    - Denver County, with 306,055 votes, or 82.8% of the total voters.
    
     This code builds on the `for` loop in the sequence above, and uses an `if` statement to determine which county has the highest number of votes cast.
```
   for county_name in county_list:
      votes = county_votes.get(county_name)
      vote_percentage= float(votes)/float(total_votes)*100
      county_results = (f"{county_name}: {vote_percentage:.1f}% ({votes:,})\n")   
         if (votes > largest_turnout):
            largest_turnout = votes
            largest_county = county_name
```
## Election Audit Summary
This prorgam can be expanded to examine any volume of votes cast, and number of counties polled and any number of candidates participating.
- This program is already set up to examine any number of votes, using this section of code. This uses a `for` loop to examine every row (each row representing a single vote), and count it. 
```
   for row in reader:
      total_votes = total_votes + 1
```
- This program is set up to record any number of counties that are participating in the election. This section of code builds on the `for` loop in the statement above, using an `if` statment. This `if` statement is telling the program to check every row, and determine the county name. If the county name isn't in a list of counties, to add it to the list. This will yield a list of all of the counties polled.
```
   if county_name not in county_list:
      county_list.append(county_name)
```
With some modification this can be changed to states that participated, as opposed to counties that participated if this is a nation wide election. By modifying the code to represent states and to pull the data from the correct location in the data that has been supplied. The code will function the same way, recording the largest voter turn out, gathering all of the state names, the votes cast in each state, and the percentage of the total votes that each state represents.
```
state_list = []
state_votes = {}
largest_state_turnout = ""
largest_vote_count = 0
state_name = row[x] (where x is the correct column in the data, states)
   if state_name not in state_list:
      state_list.append(state_name)
      state_votes[state_name] = 0
   state_votes[state_name] += 1
for state_name in state_list:
   votes = state_votes.get(state_name)
   vote_percentage= float(votes)/float(total_votes)*100
   state_results = (f"{state_name}: {vote_percentage:.1f}% ({votes:,})\n")
   if (votes > largest_state_turnout):
      largest_state_turnout = votes
      largest_vote_count = state_name
```
- This program is also set up to record all of the candidates that recieved votes in the election.
```
   if candidate_name not in candidate_options:
      candidate_options.append(candidate_name)
      candidate_votes[candidate_name] = 0
   candidate_votes[candidate_name] += 1
```
With some modifications this program can be adjusted to recored the names of the different parties that recieved votes in this election.
```
party_options = []
party_votes = {}
winning_party = ""
winning_count = 0
winning_percentage = 0
party_name = row[x] (where x represents the correct column in the data that holds party affiliation)
if party_name not in party_options:
   party_options.append(party_name)
   party_votes[party_name] = 0
party_votes[party_name] += 1
for party_name in party_votes:
   votes = party_votes.get(party_name)
   vote_percentage = float(votes) / float(total_votes) * 100
   party_results = (f"{party_name}: {vote_percentage:.1f}% ({votes:,})\n")
   if (votes > winning_count) and (vote_percentage > winning_percentage):
      winning_count = votes
      winning_party = party_name
      winning_percentage = vote_percentage
```
