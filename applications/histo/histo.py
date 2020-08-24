# Your code here

import os
import sys
import re

my_dict = {}

def print_hash(n):
    return "#" * n

with open(os.path.join(sys.path[0], "robin.txt")) as f:
    for line in f:
        line = line.rstrip("\n").split(" ")
        for word in line:
            word = re.sub("[^a-zA-Z]+", "", word)
            word = word.lower()
            if word not in my_dict:
                my_dict[word] = 1
            else:
                my_dict[word] += 1    
    # print(my_dict)
    del my_dict[""]

    my_dict_items = list(my_dict.items())
    my_dict_items.sort(key=lambda x: (-x[1],) + x[:1])
    # print(my_dict_items)
    for i in my_dict_items:
        print(f"{i[0]} \t {print_hash(i[1])}".expandtabs(24))

