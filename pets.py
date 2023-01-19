#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Michael Curtis
    DS2000
    Homework 1
    Spring 2023
    pets.py

    Test Case #1:
        Grizz = 62.5 pounds, 1.5 years
        Carol = 39 pounds, 1.5 years
        Expected: Grizz weights 1.6x what Carol weighs 
                  Grizz's age is 1x Carol's age.
    Test Case #2:
        Kona = 45 pounds, 7 years
        Tugboat = 65 pounds, 9 years
        Expected: Kona weighs .69x what Tugboat weighs 
                  Kona's age is .78x Tugboat's age

"""

def main():
    # Gather data - Ask user for name, weight, and age of their pet.
    name_1 = input("What is your first pet's name?\n")
    weight_1 = float(input("What is your first pet's weight?\n"))
    age_1 = float(input("What is your first pet's age?\n"))

    name_2 = input("What is your second pet's name?\n")
    weight_2 = float(input("What is tyour second pet's weight?\n"))
    age_2 = float(input("What is your second pet's age?\n"))

    # Compute --  Using division to calculate how much more the first pet 
    # weighs compared to 2nd pet

    pet_weight = weight_1 / weight_2
    pet_age = age_1 / age_2

    #Communicate -- print first dog and second dog's name, age, and weight
    print(name_1, " weighs ", (round(pet_weight,2)), "x what ",\
                                      name_2, " weighs.", sep="")
    
    print(name_1, "'s age is ", (round(pet_age,2)), "x ", name_2,\
                                              "'s age.", sep="")
main()

