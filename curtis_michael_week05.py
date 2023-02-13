# -*- coding: utf-8 -*-
"""
DS2001 (S23-Matherly) Week 5


@author:  Michael Curtis
"""



"""
In this week's exercise, we're going to finish our app that reads in receipts.
You should reuse the code from last week for Q1-3.

This week, we'll add data from each day to the daily summaries, specifically:
    - Sum up all the receipts for the day then add to the daily total list
    - Get the number of expenses for each day and add to the daily count list
    - Get the daily maximum amount and add that to the daily max list
Then, we'll calculate percentages by category and the daily average, and 
prepare a report for the user summarizing the information and presenting it in
bar and line charts.


"""
import matplotlib.pylab as plt

EXPENSE_FILE = ["day01.txt","day02.txt","day03.txt", "day04.txt", "day05.txt",
                "day06.txt", "day07.txt", "day08.txt", "day09.txt", "day10.txt"]




# Q1-3 should already be completed from last week, so you can just C-P that
# code in here
def main():
    tr_lst = []
    fo_lst = []
    cl_lst = []
    pe_lst = []
    me_lst = []
    
    daily_total_exp = []
    daily_items = []
    most_exp = []
    
    
    for file in EXPENSE_FILE:
        daily_receipts = []
        print("\rProcessing: ", file, end = '\n')
        with open(file, "r") as infile:
            while True:
                expense = infile.readline().strip()
                if expense == "":
                    break
                expense_type = expense[0:2]
              #  print(expense_type)
                
                amount = float(expense[5:])
           #     print(amount)
                
                if expense_type == 'TR':
                    tr_lst.append(amount)
                elif expense_type == 'FO':
                    fo_lst.append(amount)
                elif expense_type == 'CL':
                    cl_lst.append(amount)
                elif expense_type == 'PE':
                    pe_lst.append(amount)
                elif expense_type == 'ME':
                    me_lst.append(amount)
                
                daily_receipts.append(amount)
                
                
    
    # Q4: After processing the file for each days (but within the file list loop)
    # - total up the daily receipts and add this to the daily total list
    ## Use the sum() function to get the total of all values in the list
    # - get the length of the daily receipts and add it to the daily count list
    ## Use the len() function to get the number of items in a list
    # - get the maximum amount and add that to the daily max list
    ## Use the max() function to get the maximum value in a list
    

            daily_total_exp.append(sum(daily_receipts))
            daily_items.append(len(daily_receipts))
            most_exp.append(max(daily_receipts))
                        
                        
                        
            

    
# Q5: After processing all the files and outside the file list loop, 
# let's do the required calculations.
# Create a new list to store the percentages by category, and then append
# each percentage to it
# Then, calculate the daily average expenditure.
# How can you calculate the average? You need to divide every element in the
# daily list by every element in the daily count list. Think about using a 
# for loop and an incrementing counter together...



    pct_day = []
    
    tr_avg = (sum(tr_lst) / sum(daily_total_exp) * 100)
    pct_day.append(tr_avg)
    
    fo_avg = (sum(fo_lst) / sum(daily_total_exp) * 100)
    pct_day.append(fo_avg)
    
    cl_avg = (sum(cl_lst) / sum(daily_total_exp) * 100)
    pct_day.append(cl_avg)
    
    pe_avg = (sum(pe_lst) / sum(daily_total_exp) * 100)
    pct_day.append(pe_avg)
    
    me_avg = (sum(me_lst) / sum(daily_total_exp) * 100)
    pct_day.append(me_avg)
    
    
    
    daily_avg = []
    for i in range(len(daily_total_exp)):
        avg = daily_total_exp[i] / daily_items[i]
        daily_avg.append(avg)
    
    
    
    
    
   


# Q6: Let's prepare the report.
# First, show them their overall average daily expenditure
# Then show the percentage they spent on each category.
# Finally, let's prepare some visualizations of the data.
# Make a bar chart showing the overall percentages. 
# plt.bar needs three arguments, which can be list:
# - x, the x position of the bars,
# - height, the height of the bars (in our case, the percentages)
# - tick_label, the labels the bars will have on the x-axis
# Make one line chart showing the daily totals, daily max and daily average
# Don't forget to put labels on the axes!
    print("The overall daily average expenditure is: $", round(avg, 2), sep ="")
    print("The daily expenditure for Transportation is: ", round(tr_avg, 2), "%", sep ="")
    print("The daily expenditure for Food is: ", round(fo_avg, 2), "%", sep ="")
    print("The daily expenditure for Clothes is: ", round(cl_avg, 2), "%", sep ="")
    print("The daily expenditure for Personal is: ", round(pe_avg, 2), "%", sep ="")
    print("The daily expenditure for Medical is: ", round(me_avg, 2), "%", sep ="")
    

    # use plt and then slice [1]
    plt.bar(1, tr_avg, label = "Transportation")
    plt.bar(2, fo_avg, label = "Food")
    plt.bar(3, cl_avg, label = "Clothes")
    plt.bar(4, pe_avg, label = "Personal")
    plt.bar(5, me_avg, label = "Medical")
    plt.ylim(0, 40)
    
    plt.xlabel("Category")
    plt.ylabel("Overall Average Expenditure")
    plt.title("% Spent on Category")
    plt.legend()
    
    plt.show()
    
    day = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
    
    plt.plot(day, daily_total_exp, label = "Daily Total Expense")
    plt.plot(day, most_exp, label = "Daily Most Expense")
    plt.plot(day, daily_avg, label = "Daily Average")
    
    plt.xlabel("Days")
    plt.ylabel("Amount ($)")
    plt.legend()
    
    
    

    
    
main()