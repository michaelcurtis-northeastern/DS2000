#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
      Michael Curtis    
      DS2000
      Homework #7
      Spring 2023
      race.py

"""


RUNNER_FILE = "runner_data.txt"

COLORS = ['blue', 'magenta', 'green', 'orange', 'grey']

import matplotlib.pyplot as plt

# from [filename] inport [classname]
from runner import Runner

def main():

    # Create an empty list to append runners
    runners = []
    
    # Intiialize a counter variable for colors & position
    counter = 0
    
    # Gather Data - Read in the file, skip the header, and assume one
    # runner per line
    with open(RUNNER_FILE, "r") as infile:
        header = infile.readline()
       
        for line in infile:
            line = line.strip().split(' ')
            runner_name = ' '.join(line[0:2])
            
            # For each line in the file, create a Runner object, assign colors
            # and y-values for the plot, and keep all Runners in a list
            runner = Runner(runner_name, color = COLORS[counter], 
                            y = counter + 1)
            counter += 1
            
            # Iterate over runs, adding one run to the runs list
            # add distance to each runner individual list of runs
            for run in line[2:]:
                runner.add_run(float(run))
            runners.append(runner)
    
    # Initialize the max distance ran and best runner             
    max_distance = 0
    best_runner = None
    
    # Find the runner who ran farthest and max distance
    for runner in runners:
        total_distance = runner.get_total_distance()
   
        if total_distance > max_distance:
            max_distance = total_distance
            winning_runner = runner
   
   # Iterate over every day in Feb
    for day in range(1, 29):
        
        # Create consistent xlim and ylim values for each plot
        plt.xlim(0, max_distance + 10)
        plt.ylim(-1, 9)
        
        # Generate plots, rendering all Runner objects and updating their 
        # x-values with daily run amounts 
        for runner in runners:
            runner.move_next()
            runner.draw()
            
        # Add a consistent legend, xlabel, and title
        plt.xlabel('Miles Traveled')
        plt.title('Miles Covered by Runners in February') 
        plt.legend(fontsize = 9)
        plt.show()
            
    # Print name of the runner who ran the most miles in February
    print(winning_runner)

main()
