#!/usr/bin/env python
# coding: utf-8

# In[30]:


import csv
import os


file_to_load=os.path.join(".", "PyPoll", "Resources", "election_data.csv")
file_to_output=os.path.join(".", "PyPoll", "election_analysis.txt")

total_votes=0
candidate_votes={}
candidate_option=[]


winning_candidates=""
winning_count=0
with open(file_to_load)as election_data:
    #csv read
    reader=csv.reader(election_data)
    #read the header
    header=next(reader)
    #
    for row in reader:
        #add to the total vote count
        total_votes=total_votes+1
        #get the candidate name from each row
        candidate_name=row[2]
        
        #if candidate does not match any existing candidates
        #in a way our loop is discovering candidates as it goes
        
        if candidate_name not in candidate_option:
            #add it to the list of candidates in the running
            candidate_option.append(candidate_name)
            
            candidate_votes[candidate_name]=0
            
        candidate_votes[candidate_name] +=1
print(candidate_votes)
print(candidate_option)
with open(file_to_output,"w") as txt_file:
    election_result=(
        f"Election Results\n"
        f"-------------------------\n"
        f"Total Votes: {total_votes}\n"
        f"-------------------------\n"


    )
    print(election_result)    
    txt_file.write(election_result)
    for candidate in candidate_votes:
        votes=candidate_votes[candidate]
        vote_percentage=float(votes)/float(total_votes)*100
        if(votes>winning_count):
            winning_count=votes
            winning_candidate=candidate
        voter_output=f"{candidate}:{vote_percentage:.3f}% {votes}\n"  
        print(votes)
        print(vote_percentage)
        print(voter_output)
        txt_file.write(voter_output)
    winning_candidate_summary=(
    f"-------------------------\n"
    f"Winner: {winning_candidate}\n"
    f"-------------------------\n" 
    )
    print(winning_candidate_summary)
    txt_file.write(winning_candidate_summary)
# Election Results
# -------------------------
# Total Votes: 369711
# -------------------------
# Charles Casper Stockham: 23.049% (85213)
# Diana DeGette: 73.812% (272892)
# Raymon Anthony Doane: 3.139% (11606)
# -------------------------
# Winner: Diana DeGette
# -------------------------


# In[ ]:




