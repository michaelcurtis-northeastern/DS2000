# -*- coding: utf-8 -*-
"""
DS2001 (S23-Matherly) Week 2

@author: [Michael Curtis]
"""
FILE_LENGTH = "spotify_songlengths.txt"
FILE_NAMES = "spotify_songnames.txt"

def main():


    '''   
    We're going to build a calculator to determine how much the user paid
    per hour to listen to the eight most popular songs on Spotify last year.

    
    Q1:
    This is a polite calculator, so the first thing it should do is greet the
    user. Have your program save the name to a variable called 'name' using the
    input function(), and ask them nicely with an informative prompt.
    '''
    # Gather data -- ask user for name
    name = input("Hello! What is your name?\n")

    '''
    Q2:
    
    Now, let's greet the user by saying "Hi [name], welcome to your calculator."      
    
    '''
    # Greet user
    print("Hi ", name, ", welcome to your calculator.\n", sep="")
    
    
    '''
    Q3:
        
    We need to read in the list of the eight most popular songs on 
    Spotify in 2022. The file "spotify_songnames.txt" contains the list of the
    eight most popular songs on Spotify. Open the file and read the song names
    into eight different variables - s1_name, s2_name, s3_name...s8_name.
    First, put the filename in a CONSTANT at the top of the file, outside of
    the main function. Then use this constant to open the file in the code.
          
    
    '''
    # Gather data - read in file names
    
    with open(FILE_NAMES, "r") as infile:
        s1_name = infile.readline().strip()
        s2_name = infile.readline().strip()
        s3_name = infile.readline().strip()
        s4_name = infile.readline().strip()
        s5_name = infile.readline().strip()
        s6_name = infile.readline().strip()
        s7_name = infile.readline().strip()
        s8_name = infile.readline().strip()
    
    '''
    Q4:
    
    For each song, we need to print the name of the song to the user and ask
    them how many times they listened to the song. In a series of questions,
    print out the name of each song, and ask the user how many times they
    listened to the song. Save the number of times to new variables called
    s1_times, s2_times, s3_times...s8_times.
    '''
    # Gather data - ask user for number of times listening to a song
    
    s1_times = int(input("How many times did you listen to '"
                         + s1_name + "'?\n"))
    s2_times = int(input("How many times did you listen to '" 
                         + s2_name + "'?\n"))
    s3_times = int(input("How many times did you listen to '"
                         + s3_name + "'?\n"))
    s4_times = int(input("How many times did you listen to '"
                         + s4_name + "'?\n"))
    s5_times = int(input("How many times did you listen to '"
                         + s5_name + "'?\n"))
    s6_times = int(input("How many times did you listen to '" 
                         + s6_name + "'?\n"))
    s7_times = int(input("How many times did you listen to '"
                         + s7_name + "'?\n"))
    s8_times = int(input("How many times did you listen to '"
                         + s8_name + "'?\n"))


    '''
    Q5:
        
    Next, we need to read in a file with a list of the lengths of the eight 
    most popular songs, so we can know how long each one is. The file
    "spotify_songlengths.txt" contains the lengths of each of the eight most
    popular songs in the same order as the song names file. Each of the song 
    lengths is converted to decimal minutes (i.e. 3.5 minutes), so make sure 
    you read in the data appropriately. Store the song lengths in eight
    variables - s1_length, s2_length, s3_length...s8_length. As before, put
    the file name in a CONSTANT outside the main function. x 
    
    '''
    # Gather data -- Read in file , song length
    
    with open(FILE_LENGTH, "r") as infile:
        s1_length = float(infile.readline())
        s2_length = float(infile.readline())
        s3_length = float(infile.readline())
        s4_length = float(infile.readline())
        s5_length = float(infile.readline())
        s6_length = float(infile.readline())
        s7_length = float(infile.readline())
        s8_length = float(infile.readline())

    '''
    Q6:
    
    The last bit of information we need from the user is how much they paid per
    month for Spotify. Remember that this can be a partial dollar, so we need
    to process their input appropriately. 

    
    '''
    # Gather data -- ask user to input how much they pay for Spotify each month 
    
    paid = float(input(name + "," + "how much did you pay for"  +
                       " Spotify each month?\n"))
    
    '''
    Q7:
        
    Now we have all the data we need. Calculate the total number of minutes they
    spent listening to each song by multiplying each song length by the number
    of times they listened to it. Then, convert that to hours, and calculate 
    how much they spent per hour on Spotify's top songs in 2022.
    Your program should print to the user:
        - Their total number of minutes listened
        - How much they spent per hour listening 
    
    Make sure to print any calculated values neatly by using round()
    

    '''
    
    # Calculate -- calculate total number of minutes
    
    total_minutes = (s1_times * s1_length) + (s2_times * s2_length)\
        +  (s3_times * s3_length) + (s4_times * s4_length)\
            + (s5_times * s5_length) + (s6_times * s6_length)\
                + (s7_times * s7_length) + (s8_times * s8_length)
    
    # Conversion from minutes to hours for cost per hour 
    
    cost_per_hour = (paid * 12) / (total_minutes / 60) 
    
    
    # Communicate -- Print total number of minutes listened & 
    # how much they spent per hour listening
    
    print(name, ", you listened to ", round(total_minutes, 2)\
          , " minutes on Spotify this month!", sep="")
    print(name, ", you spent $", round(cost_per_hour, 2),\
          " per hour on Spotify's top songs in 2022.", sep="")
    



main()