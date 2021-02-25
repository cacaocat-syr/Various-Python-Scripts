#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'numKeypadSolutions' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY wordlist
#  2. STRING_ARRAY keypads
#

def numKeypadSolutions(wordlist, keypads):
    # Write your code here
    count_array = []
    for pad in keypads:
        count = 0
        for word in wordlist:
            if pad[0:1] not in word:
                continue
            subcount = 0
            for letter in word:
                if letter in pad:
                    subcount += 1
            if subcount >= 5 and subcount == len(word):
                count += 1
        count_array.append(count)
    return count_array
