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

#open the election results and read the file
with open(file_to_load) as election_data:
     #to do: read and analyze the data here
    #read the file object with the reader function
    file_reader = csv.reader(election_data)

    #read and print the header row.
    headers = next(file_reader)
    print(headers)

#using the with statement open the file as a text file
with open(file_to_save, "w") as txt_file:
    #write some data to the file
    txt_file.write("Hello World!\n")
    txt_file.write("Counties in the Election\n")
    txt_file.write("-------------------------\n")
    #write three counties to the file, \n is a line break, an "enter"
    txt_file.write("Arapahoe\nDenver\nJefferson")
