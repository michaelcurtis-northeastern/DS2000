#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Michael Curtis
    DS2000
    Spring 2023
    HW 7 
    runner.py
"""

import matplotlib.pyplot as plt

# Define Runner class and initialize attributes in the constructor

class Runner:
    ''' class: Runner
    
        attributes: runner name, distance runner ran each day in February,
                    x-position,y-position, color 
                    
        methods:    draw: renders runner on grid
                    add_run: appends given run to list of runs
                    get_total_distance: returns total dist of all runs in lst
                    move_next: moves runner rightwards by amnt found 
                    in next pos. in list of runs
                    __str__:returns string used when print() is
                    called on a Runner object
    '''
    
    # Build constructor to initialize attributes 
    def __init__(self, name, x = 0, y = 0, color = "green"):
        self.name = name
        self.runs = []
        self.x = x
        self.y = y
        self.color = color
   
    # Render the Runner with matplotlib
    def draw(self):
        plt.plot(self.x, self.y, self.color, marker = "4", markersize = 15,
                 label = self.name)
  
    # Add one run to the list of runs
    def add_run(self, run):
        self.runs.append(run)
     
    # Return the total miles in list of runs
    def get_total_distance(self):
        return sum(self.runs)
    
    # Move the x-value to the right by next value in runs list  
    def move_next(self):
            distance = self.runs.pop(0)
            self.x += distance
   
    # Return a well-formatted string representing object
    def __str__(self):
        return self.name + " ran the furthest overall in February."