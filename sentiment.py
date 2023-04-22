#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Michael Curtis    
    DS2000
    Homework #6
    Spring 2023
    sentiment.py
    
    
"""

import matplotlib.pylab as plt

REDDIT_FILE = "reddit.txt"

SENT_WORDS = {"love" : 1, "positive" : .8, "research" : .1, "coop" : .5,
              "understanding" : .5, "understand" : .5, "major" : .1, 
              "like" : .7, "likes" : .7, "Boston" : .6, "program" : .4, 
              "great" : .8, "involved" : .6, "awesome" : 1, "nice" : .8, 
              "enjoy" : 1, "accepted" : .3, "interesting" : .4, 
              "interests" : .7, "happy" : .9, "club" : .3, "friends" : .8,
              "opportunity" : .8, "opportunities" : .8, "recomend" : .9, 
              "highly" : .5, "rich" : -.5, "problem" : -.9, "problems" : -.9,
              "problematic" : -.9, "tuition" : -.5, "off" : -.3, 
              "expensive" : -.6, "shit" : -1, "afford" : -.5, "transfer" : -1,
              "transferred" : -1, "hotel" : -.5, "far" : -.2, "cold" : -.3, 
              "sucks" : -1, "suck" : -1, "space" : -.1}

ALPHABET = 'abcdefghijklmnopqrstuvwxyz'


def read_txt(filename):
    '''Function: read_txt
        Parameter: filename, string
        Returns: list of strings
        Does: iterates over the file and creates one list of all words
    '''
   
    
    lines = []
    
    with open(filename, "r") as infile:
        for line in infile:
        
            words = line.lower().strip()

            lines.append(words)
    
    return lines


def sentiment_score(words, sent):
    '''Function: sentiment_score
        Parameters: list of strings, dictionary
                    where key = string, value = float
        Return: float
        Does: iterate over the list of words, 
        adjusting ther score based on dictionary values
    '''
    
    score = 0
    
    for word in words:
        if word in sent:
            score += sent[word]
    
    return score / len(words)


def alpha(text): 
    '''Function: alpha
        Parameters: Text (string)
        Return: Text (string) containing ONLY alpha characters
        Does: Removes punctuation and numbers from given string
    '''
    for word in text:
        if word.isalpha() == False:
            text = text.replace(word, " ")
    
    return text

def string_lst(lst):
    ''' Function: tokenize
        Parameters: 1d list of strings
        Return: 2D list of strings
        Does: Separates each comment into a list of strings, creating
                a larger 2D list of individual comment lists
    '''
    lines_lst = []
    
    for i in lst:
        lst = i.split()
        lines_lst.append(lst)
        
    return lines_lst


def main():
    
    # Gather data - read in the REDDIT_FILE
    
    file = read_txt(REDDIT_FILE)
    
    # Create an empty list of words to iterate over and 
    # clean the list -- remove punctuation
    # Append to words list
    
    words = []
    for word in file:
        no_punctuation = alpha(word)
        words.append(no_punctuation)
    
    words = string_lst(words)
    
    
    
    # Computation -- call the sentiment_score function to 
    # caluculate the score of each word from list pf words
    # Append scores to a list
    scores = []
    
    
    for words in words:
        score = sentiment_score(words, SENT_WORDS)
        scores.append(score)
   
    
    # Reverse scores to be old-to-new 
    scores.reverse()
    
    # Create lists for individual score categories
    
    pos = []
    neutral = []
    neg = []
    
    # Initialize a value for the list position
    list_pos = 0
    
    # Create lists for comment position 
    positive_position = []
    neutral_position = []
    negative_position = []
    
    # Iterate over scores list to find the sentiment of the score
    # Append to appropriate pos, neutral, or neg list
    
    for score in scores:
        if score > 0:
            pos.append(score)
            list_pos += 1
            positive_position.append(list_pos)
        if score == 0:
            neutral.append(score)
            list_pos += 1
            neutral_position.append(list_pos)
        if score < 0:
            neg.append(score)
            list_pos += 1
            negative_position.append(list_pos)
        
    
    # Communication - plot the scores in different colors
    plt.scatter(positive_position, pos, color = "limegreen", label = 
                "Positive")
    plt.scatter(neutral_position, neutral, color = "grey",
                label = "Neutral")
    plt.scatter(negative_position, neg, color = "orangered", 
                label = "Negative")
    
    # Axes & labels
    plt.title("Sentiment Scores of NU Reddit")
    plt.ylim(-.1, .4)
    plt.xlabel("Comments over time (oldest to newest)")
    plt.ylabel("Sentiment Score")
    plt.legend()
main()