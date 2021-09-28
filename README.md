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

   This was determined with the following string of code. This code uses a for loop to check every row (representing each vote) and add one vote to the total number of votes cast.
  ```
    for row in reader:
      total_votes = total_votes + 1
  ```
2. The candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane

    This code builds on the for loop in the step above to check each row in the canidate name column and add it to a list.
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

    This code continues to build on the for loop above, to begin tracking votes and adding them to the list of candidates, adding one vote for every row that contains the name of the candidate.
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

    This string of code is taking the total votes for each candidate generated in the step above and dividing it by the total number of votes calculated in the first step, and multiplying by 100, yielding the percentage.
```
     for candidate_name in candidate_votes:
        votes = candidate_votes.get(candidate_name)
        vote_percentage = float(votes) / float(total_votes) * 100
```





- The winner of the election was
  - Diana DeGette, who recived 73.8% of the vote and 272.892 votes.
- The percentage of the total votes that each county represents:
  - Jefferson County with 10.5% of the total votes, with 38,855 votes cast.
  - Denver County with 82.8% of the total votes, with 306,055 votes cast.
  - Arapahoe County with 6.7% of the total votes, with 24,801 votes cast.
- The largest county was Denver County, with 306,055 votes, or 82.8% of the total voters.

## Challenge Overview

## Challenge Summary
