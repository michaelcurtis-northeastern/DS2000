#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
    Michael Curtis    
    DS2000
    Homework #6
    Spring 2023
    decryptify.py


"""



VIGENERE_FILE = "vigenere.csv"
KEYS_FILE = "keys.txt"
HEADER = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 
 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 
 '.', '-', ';', ':', '/', '\\']




def make_decryption(file):
    '''Function: make_decryption
        Parameters: a 2D list, such as the one that might be returned
        after reading a CSV file
        Returns: a dictionary
        Does: isolates column 0. Each element of this column 
        becomes a key of the dictionary, with the value coming 
        from the rest of its row
    '''
    
    decryption = {}
    
   
    for row in file: 
        key = row[0]
        value = row[1:]
        decryption[key] = value
        
    return decryption


def decrypyt_word(header, dct, encrypt, key):
    '''Function: decrypt_word
        Parameters: 1D list, dictionary, encrypted string, key
        Returns: string
        Does: Decrypts the fiven word using a vigenere cipher
    '''
    decrypted = ""
    
    for i in range(len(key)):
        
    
        key_letter = key[i]
        lst = dct[key_letter]
        
        
        word_letter = encrypt[i]
        pos = lst.index(word_letter)
    
        
        decrypted_letter = header[pos]
        decrypted += decrypted_letter
        
    return decrypted
    
def main():
    
    # Prompt user for message to decrypt
    user_message = input("What message do you want to decrypt?\n")
    
    
    # Create empty list to append keys 
    keys = []
    
    # Read in file with keys
    with open(KEYS_FILE, "r") as infile:
        for line in infile:
            
            key = line.strip()
            
            # Append the keys to an empty list - key
            keys.append(key)
    
    # Create empty list to append code
    cipher = []
    
    # Read in cipher file
    with open(VIGENERE_FILE, "r") as infile:
        for line in infile:
            line = line.strip()
            
            code = line.split(",")
            
            # Append the code to an empty list - cipher
            cipher.append(code)
    
        
    # Call the decryption function to take the 2D list of the cipher
    # to make it a dictionary
    decryption = make_decryption(cipher)
    
    # Iterate over the keys list
    
    for key in keys: 
        
        # Call the decrypt word function that takes in parameters to 
        # decrypt the user message
        decrypt = decrypyt_word(HEADER, decryption, user_message, key)
        
        # Check to see if the message starts with a link
        if decrypt.startswith("https://bit.ly") == True: 
            
            # Communication -- print the decrypted message
            print("The decrypted message is: ", decrypt)
        
        
main()


