#!/usr/bin/env python
# coding: utf-8

# In[26]:


#import dependencies
import os
import csv
#fille to load output
#"."=current

file_to_load=os.path.join(".", "PyBank","Resources", "budget_data.csv")

file_to_output=os.path.join(".", "budget_analysis.txt")
total_months=0
total_net=0
net_change_list=[]
greatest=["",0]
least=["", 9999999999900]
#read the files

with open(file_to_load) as financial_data:
    reader=csv.reader(financial_data)
    print(reader)
    #Read the header row
    header=next(reader)
    #read the first row
    first_row=next(reader)

  
    #track the total
    for row in reader:
        #to calculate the total we can do  =total months+=1 (total_months=0+1)
        total_months=total_months+1
        total_net+=int(first_row[1])
        previous_net=int(first_row[1])
        
        #Track the net change
        net_change=int(row[1])-previous_net
        previous_net=int(row[1])
        net_change_list.append(net_change)
        
        #calculate the greatest increases
        if(net_change>greatest[1]):
              greatest[0]=row[0]
              greatest[1]=net_change
        #calculate the greatest decreases
        if(net_change<least[1]):
          least[0]=row[0]
          least[1]=net_change

net_monthly_average=sum(net_change_list)/len(net_change_list)        
        
        
        
        
#\n new line
output=(
    f"Financial Analysis\n"
    f"----------------------------\n"
    f"total_months:{total_months}\n"
    f"total: ${total_net}\net"
    f"Average Change ${net_monthly_average:.2f}\n"
    f"Greatest Increase in Profits: {greatest[0]} (${greatest[1]})\n"
    f"Greatest Decrease in Profits: {least[0]} (${least[1]})"
    )
print(output)
with open(file_to_output,"w")as txt_file:
    txt_file.write(output)
        


# In[ ]:





# In[ ]:





# In[ ]:




