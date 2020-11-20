'''
Roy wanted to increase his typing speed for programming contests. His friend suggested that he type the sentence "The quick brown fox jumps over the lazy dog" repeatedly. This sentence is known as a pangram because it contains every letter of the alphabet.

After typing the sentence several times, Roy became bored with it so he started to look for other pangrams.

Given a sentence, determine whether it is a pangram. Ignore case.

Function Description

Complete the function pangrams in the editor below. It should return the string pangram if the input string is a pangram. Otherwise, it should return not pangram.

pangrams has the following parameter(s):

    s: a string to test

Input Format

Input consists of a string

.

Constraints


Each character of ,

Output Format

Output a line containing pangram if

is a pangram, otherwise output not pangram.

Sample Input 0

We promptly judged antique ivory buckles for the next prize

Sample Output 0

pangram
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the pangrams function below.
def pangrams(s):
    return len(set(c.lower() for c in s if c != ' '))
if __name__ == '__main__':
    s = input()
    if pangrams(s) == 26:
        print ("pangram")
    else:
        print ("not pangram")
