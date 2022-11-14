import os
import csv

#Assigning variables and arrays
bcsvpt = "Resources\\budget_data.csv"
csvdate = []
csvPL = []
change_PL = []
total_PL = 0
previous_pl = 0
total_change_PL = 0

# creating array lists from csv
with open(bcsvpt) as csv_bud_dt:
     cread = csv.reader(csv_bud_dt , delimiter=',')
     for lines in cread:
        csvdate.append(lines[0])
        csvPL.append(lines[1])

#Removing header row   
csvdate.pop(0)
csvPL.pop(0)

# total months caluculations
num_months = (len(csvdate)) #totalmonths 

#Creating change_PL array list
for pl in csvPL:
    total_PL = total_PL + int(pl) #totalPL  
    change_PL.append(int(pl)-previous_pl)
    previous_pl = int(pl)
    
#Removing first cell info from created change_PL list
change_PL.pop(0)

for cpl in change_PL:
    total_change_PL = total_change_PL + cpl #loop

 

#Average change PL
Total_Amount = round(total_change_PL/len(change_PL),2)
# greatest increase in profit date
increase_date = csvdate[change_PL.index(max(change_PL))+1]
#greatest decrease in profits date
decrease_date = csvdate[change_PL.index(min(change_PL))+1]
#greatest increase in profit amt
increase_amt = max(change_PL)
#greatest decrease in profit amt
decrease_amt = min(change_PL)

# Terminal print

print("  Financial Analysis")
print(" -----------------------------------")
print("  Total Months: ",num_months)
print("  Total: $" ,total_PL)
print("  Average Change: $",Total_Amount)
print("  Greatest Increase in Profits: ",increase_date,"($",increase_amt,")")
print("  Greatest Decrease in Profits: ",decrease_date,"($",decrease_amt,")")
print(" -----------------------------------")

# # create text file Pybankexport

f= open("Analysis\\PyBankexport.txt", "w")
f.write("  Financial Analysis\n-----------------------------------\n  Total Months: %s \n" % (num_months))
f.write(  "  Total: $ %s \n" %(total_PL))
f.write(  "  Average Change: $ %s \n" % (Total_Amount))
f.write( "  Greatest Increase in Profits: %s ($ %s)\n" % (increase_date,increase_amt))
f.write( "  Greatest Decrease in Profits: %s ($ %s) \n" %(decrease_date,decrease_amt))
f.write(  "-----------------------------------")
f.close()

#End confirmation
print("New PyBankexport text file created successfully!")


     
     


