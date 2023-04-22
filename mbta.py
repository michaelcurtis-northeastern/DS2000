'''
    Michael Curtis
    DS2000
    Homework #5
    Spring 2023
    mbta.py
    
'''

import csv
import matplotlib.pyplot as plt

MBTA_FILE = "mbta_data.csv"
LINE_COL = 3
TOTAL_ON = 12
TOTAL_OFF = 13
TIME_OF_DAY = 8

def read_file(filename):
    ''' Function: read_file
        Parameters: filename (string) for a CSV file
        Returns: 2d list of what the file contains
        Does: Reads every line of the file, except the header,
              and stored in a 2d list which is returned at the end
    '''
    data = []
    with open(filename) as csvfile:
        reader = csv.reader(csvfile, delimiter = ",")
        next(reader)
        for row in reader:
            data.append(row)
    return data

def get_col(data, col):
    ''' Function: get_col
        Parameters 2d list of anything, a column number (int)
        Returns: one column of the 2d list, turned into a list of its own
        Does: Loops over the 2d list, and for each sublist, appends
              a value at the given location onto a new list
    '''
    lst = []
    for row in data:
        lst.append(row[col])
    return lst

# Function 1
def riders_per_line(data, lines, line_col, total_on):
    ''' Function: riders_per_line
        Parameters: 2d list, MBTA lines, column of the MBTA lines, 
                    total people on the line(int)
        Returns: a float indicating the average number of riders 
                    getting on the given line
        Does: Looks for the line in the 2D list. If found, increase the
                total number of riders
    '''
    
    riders = []
    
    for row in data:
        if row[line_col] == lines:
        # Adding riders
            riders.append(float(row[total_on]))
    # Calculating average of riders 
    avg_riders = sum(riders) / len(riders)


    return round(avg_riders, 2)
            
# Function 2
def split_by_time(data, time_period, time_of_day):
    ''' Function: split_by_time
        Parameters: 2d list, time period, an int for the column number 
                     where the time_period column lives
        Returns: a float indicating the average number of riders 
                    getting on the given line
        Does: Looks for the line in the 2D list. If found, increase the
                total number of riders
    '''
    
    time_data = []
    for row in data:
        if row[time_of_day] == time_period:
            time_data.append(row)
    return time_data
  
# Function 3

def plot_ridership(ridership, lines):
    
    ''' Function: plot_ridership
        Parameters: A list of ints (# of riders per line), and list of strings
                    (lavels MBTA line name)
        Returns: nothing
        Does: makes a bar graph with colors and labels take from list of strings, 
            height taken from the list of ints
    '''
    
    # Create a bar chart with ridership data and lines
    plt.bar(lines, ridership, color = lines)
    
    # Set x-tick labels to line name
    
    
    # Create labels
    plt.xlabel("MBTA Lines")
    plt.ylabel("Number of Riders")
    plt.title("Number of Riders on MBTA Lines")
    
    plt.show()
    
# Function 4

def plot_time_ridership(ridership_time, lines):
    ''' Function: plot_time_ridership
        Parameters: 2d list of floats, with a sublist representing ridership
            of all MBTA lines at a certain time of dat
        Returns: Nothing
        Does: Creates line chart cahlling the get_col function. List of strings
        is used to plot labels
    '''
    
    for i in range(len(lines)):
        
        ridership = get_col(ridership_time, i)
        
        plt.plot(ridership, label = lines[i], color = lines[i])
        
        plt.xlabel("Time")
        plt.ylabel("Ridership")
        plt.title("Ridership on MBTA Lines Throughout the Day")
        plt.xticks([i for i in range(0, len(ridership), 3)], \
            ["Morning", "Mid Day", "Afternoon", "Night"])
        plt.legend()
    
    
    
# Main function
def main():
    
    # Step One: Gathering data
    # Get the data as a 2d list of ints
    data = read_file(MBTA_FILE)
    
    # Step Two: Computations 
    # Compute the average number of riders getting on each line
    lines = ["Green", "Blue", "Red", "Orange"]
    
    ridership = []
    for i in range(len(lines)):
        on_riders = riders_per_line(data, lines[i], LINE_COL, TOTAL_ON)
        ridership.append(on_riders)
    
    

    # Step Two: Computations
    # Count the average number of total riders at each time of day
    # We can reuse the ridership functions above, but first we
    # split the data into each separate part of day 
    
    ridership_time = []
    for i in range(1, 12):
        time_period = "time_period_{:02d}".format(i)
        time_data = split_by_time(data, time_period, TIME_OF_DAY)
        curr_riders = []
        for j in range(len(lines)):
            riders = riders_per_line(time_data, lines[j], LINE_COL, TOTAL_ON)
            curr_riders.append(riders)
        ridership_time.append(curr_riders)
        
        
    
    # Step Three: Communicate! 
    # Plot the average number of riders getting on each line
    plot_ridership(ridership, lines)
    plt.show()
    
    
    # Plot each line's ridership over the day as a line chart
    plot_time_ridership(ridership_time, lines)
    
    # Communicate part 2... print out average ridership per line
    print("Average ridership per line:")
    for i in range(len(lines)):
        print("\t", lines[i], ": ", round(ridership[i]), " avg riders.",
              sep = "")
    
main()