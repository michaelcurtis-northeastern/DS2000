#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
     Michael Curtis
     DS2000
     Homework 2
     Spring 2023
     roulette.py
 
"""
import random

import matplotlib.pylab as plt

def main():
    
    
    
    # Kayla and Laney start at $0
   
    kayla_wins = 0
    laney_wins = 0
    kayla_dollars = 0
    laney_dollars = 0
    
    while kayla_dollars < 50000 and laney_dollars < 50000:
        
        # Gather data -- get a random number
        spin = random.randint(1, 36)
        
        
        # Compute -- Determine if Kayla wins and how much she wins
        
        if spin % 2 == 1:
            kayla_dollars += 5
            kayla_wins += 1
            
        # Compute -- Determine if Laney wins and how much she wins
        
        if spin == 31 or spin == 32:
            laney_dollars += 50
            laney_wins += 1
    
    
    
    # Commuicate -- show how many wins and how much money Kayla and Laney have
    
    plt.bar("Kayla", kayla_wins, color = "blue")
    plt.bar("Laney", laney_wins, color = "red")
    plt.title("Encore Wins vs Loses for Kayla & Laney")
    plt.ylabel("Total Wins")
    
    plt.show()
    
    plt.bar("Kayla", kayla_dollars, color = "blue")
    plt.bar("Laney", laney_dollars, color = "red")
    plt.title("Encore Total Money Won for Kayla & Laney")
    plt.ylabel("Total Money Won")
    
    
    
    
    
    
main()