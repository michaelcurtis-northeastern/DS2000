#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
        Michael Curtis
        DS2000
        Homework 2
        Spring 2023
        race.py
        
        Test Case:
            Laney's location: (2,2)
            Kayla's location: (5,2)
            Cooper's location: (5,5)
            Euclidean distance (Laney): (5 - 2) ** 2 + (5 - 2) ** 2
            Euclidean distance (Kayla): (5 - 5) ** 2 + (5 - 2) ** 2 
                    take sqrt of this value to get 4.242 & 3
            Time from Cooper(Laney): 4.243 * 10 min = 42.246 minutes
            Time from Cooper(Kayla): 3 * 10 min = 30 minutes
        
"""

FILE_NAME = "locations.txt"

def main():
    
    # Gather data -- open 'locations.txt' file 
    
    with open(FILE_NAME, "r") as infile:
        
        # Name 1 -- Kayla 
        name1 = infile.readline().strip()
        name1_x = int(infile.readline())
        name1_y = int(infile.readline())
        
        # Name 2 -- Laney
        name2 = infile.readline().strip()
        name2_x = int(infile.readline())
        name2_y = int(infile.readline())
    
    # Gather data -- ask user to put in Cooper's coordinates
    
    cooper_x = int(input("What is Cooper's x-coordinate?\n"))
    cooper_y = int(input("What is Cooper's y-coordinate?\n"))
    
    # Compute -- Calculate distance between Cooper and Kayla & 
    # Cooper and Laney
    
    distance_1 = (cooper_x - name1_x) ** 2 + (cooper_y - name1_y) ** 2
    sqrt_1 = distance_1 ** .5
    
    distance_2 = (cooper_x - name2_x) ** 2 + (cooper_y - name2_y) ** 2
    sqrt_2 = distance_2 ** .5
    
    time_1 = sqrt_1 * 10
    time_2 = sqrt_2 * 10
    
    # Communicate -- print distance to Cooper from each person
    
    print(name1, "is ", round(sqrt_1, 3), "units & ",\
          round(time_1, 3), "minutes away from Cooper.")
    
    print(name2, "is ", round(sqrt_2, 3), "units & ",\
          round(time_2, 3), "minutes away from Cooper.")
    
    
main()



