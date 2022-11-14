import os
import csv
#Assigning variables and arrays
ecsvdt = "Resources\\election_data.csv"
eBallotID = []
eCountry = []
eCandidate = []
candidates = []
secured_votes = 0
win_votes = 0
winner = "TBD"

# creating array lists from csv
with open(ecsvdt) as csv_ele_dt:
    eread = csv.reader(csv_ele_dt , delimiter=',')
    # Read the header row.
    headers = next(eread)
    for infoln in eread:
        eBallotID.append(infoln[0])
        eCountry.append(infoln[1])
        eCandidate.append(infoln[2])





#  The total number of votes cast and print results on terminal and text file
print("  Election Results")
print(" -----------------------------------")

num_votes = len(eBallotID)
print(f"Total votes : {num_votes}") #for terminal output

print(" -----------------------------------")

output_text = "  Election Results\n-----------------------------------\nTotal votes :"+str(num_votes)+"\n-----------------------------------\n" #for text file 


# Creating complete list of candidates who received votes
for c in eCandidate:
    if c not in candidates:
        candidates.append(c)


#Calculating and printing  total number and their percentage of votes each candidate won
for candidate in candidates:
    for votes in eCandidate:
        if votes == candidate:
            secured_votes = secured_votes + 1
    print(candidate,":",round(100*secured_votes/num_votes,3),"% (",secured_votes,")" ) # for Terminal output
    output_text = output_text + str(candidate)+":"+str(round(100*secured_votes/num_votes,3))+"% ("+str(secured_votes)+")\n" #for text file
#winner of the election based on popular vote
    if secured_votes > win_votes: 
        winner = candidate
        win_votes = secured_votes
    secured_votes = 0
print("-----------------------------------")
print("Winner : ",winner)#for Terminal output
print("-----------------------------------")
output_text = output_text+ "-----------------------------------\nWinner : "+str(winner)+"\n-----------------------------------" #for text file

# # create text file PyPollexport
f= open("Analysis\\PyPollexport.txt", "w")
f.write(output_text)
f.close()

#End confirmation
print("New PyPollexport text file created successfully!")
