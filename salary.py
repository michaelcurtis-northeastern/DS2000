#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
     DS2000
     Spring 2023
     Sample Code from Class - working with files & salary data
     January 17, 2023
     
     Test case - 
     total of: 
         131111.83
         63698.64
         111431.15
         39508.98
         27228.00
     
"""
FILENAME = "boston_salaries.txt"

def main():
    
        #Gather data - read in salaries from the file
        
    with open(FILENAME, "r") as infile:
        salary1 = float(infile.readline())
        salary2 = float(infile.readline())
        salary3 = float(infile.readline())
        salary4 = float(infile.readline())
        salary5 = float(infile.readline())
    
    # Gather data - ask the user for their salary
    
    salary6 = float(input("How much do you make?\n"))
    
    
    
    total = salary1 + salary2 + salary3 + salary4 + salary5 + salary6
    
    print("Total salary budget is:", total)
main()
