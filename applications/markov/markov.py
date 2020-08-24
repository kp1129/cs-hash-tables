
"""
import random
import os
import sys
import re

# Read in all the words in one go
with open(os.path.join(sys.path[0],"input.txt")) as f:
    words = f.read()
    words = words.rstrip("\n").split(" ")
    clean_words = []
    for word in words:
        word = re.sub("[^a-z.!?'A-Z]+", " ", word)
        word = word.split(" ")
        for each in word:
            if each != "":
                clean_words.append(each)
    # clean words is a list with the text, 
    # the words appear in chronological order
    # print(clean_words)

# TODO: analyze which words can follow other words
# Your code here
    my_dict = {}

    for ix, word in enumerate(clean_words):
        if word not in my_dict and ix != len(clean_words) - 1:
            my_dict[word] = []
            my_dict[word].append(clean_words[ix + 1])
        elif word in my_dict and ix != len(clean_words) -1:
            my_dict[word].append(clean_words[ix + 1])    
    print(my_dict)

    
    # previous = ""

    # for word in reversed(words):
    #     if word in my_dict and previous != "":
    #         my_dict[word].append(previous)
    #         previous = word
    #     if word not in my_dict and previous != "":
    #         my_dict[word] = []
    #         my_dict[word].append(previous)  
    #         previous = word

    # print(my_dict)

# TODO: construct 5 random sentences
# Your code here
"""

import os
import sys
import random

with open(os.path.join(sys.path[0],"input.txt")) as f:
    words = f.read().split()

    dataset = {}

    for i in range(len(words) - 1):
        word = words[i]
        next_word = words[i + 1]

        if word not in dataset:
            dataset[word] = [next_word]

        else:
            dataset[word].append(next_word)    


    start_words = []
    for key in dataset.keys():
        if key[0].isupper and len(key) > 1 and key[1].isupper():
            start_words.append(key) 

    word = random.choice(start_words)      

    stopped = False
    stop_signs = "?.!"

    sentence = []
    while not stopped:
        sentence.append(word)
        if word[-1] in stop_signs or len(word) > 1 and word[-2] in stop_signs:
            stopped = True

        following_words = dataset[word]
        word = random.choice(following_words)


    print(" ".join(sentence))
