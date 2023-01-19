#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Michael Curtis
    DS2000
    Homework 1
    Spring 2023
    sailing.py
    
    Test Case #1: 
        traffic = 3
        wind = 14
        swells = 1
        Expected = (.2)(7) + (.5)(1) + (.3)(0) = 1.9
        
    Test Case #2:
        traffic = 5
        wind = 10
        swells = 1
        Expected = (.2)(5) + (.5)(10) + (.3)(0) = 3.5

"""
TRAFFIC = .2
WIND_SPEED = .5
SWELLS = .3

def main():
    # Gather data -- ask user to input traffic, windspeed, and swells
    traffic = int(input("How much traffic was there, on a scale of 0-10?\n"))
    wind_speed = int(input("What was the wind speed, in knots 5-15?\n"))
    swells = int(input("Where the swells high (0 = no, 1 = yes?\n"))
    
    # Compute -- Converting user input to 0-10 scale
    traffic_convert = (10 - traffic)
    wind_speed_convert = (10 - (wind_speed - 5))
    swells_convert = (10 - swells) // 10
    
    # Compute -- weighted average
    
    weighted_avg = TRAFFIC * traffic_convert + WIND_SPEED * \
                    wind_speed_convert+ SWELLS * swells_convert
    
    #Communicate -- print the weighted average rounded to two decimals
    print("On a scale out of 10, we computed your day of sailing " + 
          "to have a weighted average of ", round(weighted_avg,1), ".", sep="")

main()