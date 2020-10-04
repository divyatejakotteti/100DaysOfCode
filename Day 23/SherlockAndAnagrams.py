'''
Two strings are anagrams of each other if the letters of one string can be rearranged to form the other string. Given a string, find the number of pairs of substrings of the string that are anagrams of each other.

For example s= mom, the list of all anagrammatic pairs is [m,m],[mo,om]at positions [[0],[2]],[[0,1],[1,2]]respectively.

Function Description

Complete the function sherlockAndAnagrams in the editor below. It must return an integer that represents the number of anagrammatic pairs of substrings in s.

sherlockAndAnagrams has the following parameter(s):

    s: a string .
Input Format

The first line contains an integer q, the number of queries.
Each of the next q lines contains a string s to analyze.

Output Format

For each query, return the number of unordered anagrammatic pairs.

Sample Input 

2
abba
abcd

Sample Output 

4
0
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the sherlockAndAnagrams function below.
def sherlockAndAnagrams(s):
    l=0
    for i in range(1,len(s)):
        d={}
        for j in range(len(s)-i+1):
            string="".join(sorted(s[j:j+i]))
            if string not in d:
                d[string]=1
            else:
                d[string]+=1
            l+=d[string]-1
    return l
        
if __name__ == '__main__':

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = sherlockAndAnagrams(s)

        