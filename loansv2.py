#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
        Michael Curtis
        DS2000
        Homework 2
        Spring 2023
        loansv2.py
        
        
"""

LOANS_FILE = 'debt_vs_tuition2.txt'


import matplotlib.pylab as plt

def main():
    
    total_tuition = 0 
    total_debt = 0
    
    with open(LOANS_FILE, "r") as infile:
        while True:
            school = infile.readline().strip()
            debt = infile.readline()
            tuition = infile.readline()
            
            if school == "": 
                break
            
            debt = int(debt)
            tuition = int(tuition)
            
            #print(school, ":", debt, ":", tuition)
            
            total_tuition += tuition
            total_debt += debt
            
            avg_debt = debt / (tuition * 4)
            
            print(school, avg_debt)

            overall_avg_debt = total_debt / (total_tuition * 4)
            
    # Read in file a second time to plot the average debt 
        # by overall average debt
    
    with open(LOANS_FILE, "r") as infile:
        while True:
            school = infile.readline().strip()
            debt = infile.readline()
            tuition = infile.readline()
            
            if school == "": 
                break
            
            debt = int(debt)
            tuition = int(tuition)

            # Compute -- add all tuition and all debt
            
            total_tuition += tuition
            total_debt += debt
            
            
            # Compute -- average debt and overall average debt
            
            avg_debt = debt / (tuition * 4)
            

            overall_avg_debt = total_debt / (total_tuition * 4)
           
            
            if avg_debt > overall_avg_debt:
                avg_debt_color = "blue"
            elif avg_debt < overall_avg_debt:
                avg_debt_color = "red"
            
            # Communicate -- plot tuition vs. average debt
            
            # x axis -- tuition
            # y axis -- average debt
            
            plt.plot(tuition, avg_debt, "o", color = avg_debt_color)
            
              
            # Change the xlimit and ylimit
            
            plt.xlim(56000, 65000)
            plt.ylim(.05, .13)
            
            # Add labels and a title
            
            plt.xlabel("Overall Average Debt-to-Tuition for Each College ($)")
            plt.ylabel("Average Debt for Each College")
            plt.title("Tuition vs Average Debt for Schools in the Northeast")
        # Add overall average debt line
        plt.axhline(overall_avg_debt, color = "black", label = "Overall Average Debt")
        plt.legend()
            
       
            
            
            
            
    
main()