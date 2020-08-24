# Use frequency analysis to find the key to ciphertext.txt, and then
# decode it.

# Your code here

# count letter frequencies and letters in ciphertext

# convert cipher letters to their decrypted 
# counterparts using the frequency table
# included in readme

import os
import sys
import re

frequencies = {}
counter = 0
clean_text = ""

with open(os.path.join(sys.path[0], "ciphertext.txt")) as ciphertext:
    for line in ciphertext:
      
        newline = line.rstrip("\n").split(" ")
        
        for each in newline:
            each = re.sub("[^A-Z]+", "", each)
            for char in each:
                counter += 1
                if char in frequencies:
                    frequencies[char] += 1
                else:
                    frequencies[char] = 1

    print(frequencies)
    print(counter)

    # convert to percentages
    for each in frequencies:
        frequencies[each] = round((frequencies[each] * 100) / counter, 2)

    print(frequencies)    

    # convert to decrypted letters
    decrypt_map = {
        "E": 11.53, "T": 9.75, "A": 8.46, "O": 8.08, "H": 7.71, "N": 6.73, "R": 6.29, "I": 5.84, "S": 5.56, "D": 4.74, "L": 3.92, "W": 3.08, "U": 2.59, "G": 2.48, "F": 2.42, "B": 2.19, "M": 2.18, "Y": 2.02, "C": 1.58, "P": 1.08, "K": 0.84, "V": 0.59, "Q": 0.17, "J": 0.07, "X": 0.07, "Z": 0.03
    }

    for line in ciphertext:
        newline = line.rstrip("\n").split(" ")

        for each in newline:
            for char in each:
                
