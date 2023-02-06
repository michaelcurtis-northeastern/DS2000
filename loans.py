#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Michael Curtis
    DS2000
    Homework 2
    Spring 2023
    loans.py
    
"""
import matplotlib.pylab as plt

LOANS_FILE = "debt_vs_tuition.txt"

def main():
    
    # Gather data -- read in "debt_vs_tuition.txt" 
    
    with open(LOANS_FILE, "r") as infile:
        # School 1
        name1 = infile.readline().strip()
        debt1 = int(infile.readline())
        tuition1 = int(infile.readline())
        color1 = infile.readline().strip()
        
    
        # School 2
        name2 = infile.readline().strip()
        debt2 = int(infile.readline())
        tuition2 = int(infile.readline())
        color2 = infile.readline().strip()
        
        # School 3
        name3 = infile.readline().strip()
        debt3 = int(infile.readline())
        tuition3 = int(infile.readline())
        color3 = infile.readline().strip()
    
        # Computation -- average of all debt
        
        avg_debt = (debt1 + debt2 + debt3) / 3
        
        # Communicate -- build scatter plot to compare debt and tuition
        # tuition = x value
        # debt = y value 
        
        plt.plot(tuition1, debt1, "o", color = color1, label = "Northeastern")
        plt.plot(tuition2, debt2, "o", color = color2, label = "Tufts")
        plt.plot(tuition3, debt3, "o", color = color3, label = "Brown")
        
        # Change the xlimit and ylimit
        
        plt.xlim(50000, 70000)
        plt.ylim(15000, 30000)
        
        # Labeling graph
        
        plt.xlabel("Tuition ($)")
        plt.ylabel("Debt ($)")
        plt.title("Debt v. Tuition at Northeastern, Tufts, & Brown")
        
        # Line for average debt
        
        plt.axhline(avg_debt, color = "black")
        
        # Legend
        
        plt.legend(fancybox = True, framealpha = 1, shadow = True,\
                   borderpad = 1)
        
        
main()
