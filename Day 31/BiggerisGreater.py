'''
Lexicographical order is often known as alphabetical order when dealing with strings. A string is greater than another string if it comes later in a lexicographically sorted list.

Given a word, create a new word by swapping some or all of its characters. This new word must meet two criteria:

    It must be greater than the original word
    It must be the smallest word that meets the first condition

For example, given the word
, the next largest word is

.

Complete the function biggerIsGreater below to create and return the new string meeting the criteria. If it is not possible, return no answer.

Function Description

Complete the biggerIsGreater function in the editor below. It should return the smallest lexicographically higher string possible from the given string or no answer.

biggerIsGreater has the following parameter(s):

    w: a string

Input Format

The first line of input contains
, the number of test cases.
Each of the next lines contains .
Output Format

For each test case, output the string meeting the criteria. If no answer exists, print no answer.

Sample Input 0

5
ab
bb
hefg
dhck
dkhc

Sample Output 0

ba
no answer
hegf
dhkc
hcdk


'''

import math
import os
import random
import re
import sys

def biggerIsGreater(w):
    big = ''
    for i in range(len(w)):
        index = -i-1
        c = w[index]
        #print(index,c)
        if c >= big:
            big = c
        else:
            l = sorted(w[index:])
            for j, k in enumerate(l):
                if k > c:
                    return w[:index] + k + ''.join(l[:j] + l[j+1:])
    return 'no answer'


if __name__ == '__main__':

    T = int(input())

    for T_itr in range(T):
        w = input()

        result = biggerIsGreater(w)
