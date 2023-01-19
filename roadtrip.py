#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Michael Curtis
    DS2000
    Homework 1
    Spring 2023
    roadtrip.py

    Test Case #1:
        Distance = 3000
        Speed = 50 MPH
        Sleep time = 8 hours
        Expected: 3 days, 4 hours
        
    Test Case #2: 
        Distance = 100 
        Speed = 100 MPH
        Sleep tome = 2 hours
        Expected: 0 days, 1 hour

"""
def main():
    # Gather data -- Ask user how many miles the trip will be, the average
    # speed in MPH, and how much time Kermit and Fozzie spend resting
    
    distance = int(input("How far are Kermit and Fozzie going, in miles?\n"))
    speed = int(input("What will their average speed, in MPH?\n"))
    sleep_time = int(input("How long will they sleep each day, in hours?\n"))
    
    # Caluculating total hours trip will take 
    driving_hours = (distance / speed)
    

    # Converting total hours to days and hours
    
    trip_days = driving_hours // 24
    
    # calcuate total sleep hours and add to total hours
    
    sleep_hours = trip_days * sleep_time
    total_hours = driving_hours + sleep_hours
    
    # recalculate trip days and calculate trip hours
    
    trip_days = int(total_hours // 24)
    trip_hours = int(total_hours % 24)
    
    print("The Muppet Road Trip will take...")
    print(trip_days, "days, ", trip_hours, "hours\n")

main()