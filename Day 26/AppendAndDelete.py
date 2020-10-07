'''
You have a string of lowercase English alphabetic letters. You can perform two types of operations on the string:

    Append a lowercase English alphabetic letter to the end of the string.
    Delete the last character in the string. Performing this operation on an empty string results in an empty string.

Given an integer,
, and two strings, and , determine whether or not you can convert to by performing exactly of the above operations on . If it's possible, print Yes. Otherwise, print No.
Function Description

Complete the appendAndDelete function in the editor below. It should return a string, either Yes or No.

appendAndDelete has the following parameter(s):

    s: the initial string
    t: the desired string
    k: an integer that represents the number of operations

Input Format

The first line contains a string
, the initial string.
The second line contains a string , the desired final string.
The third line contains an integer

, the number of operations.

Constraints

s and t consist of lowercase English alphabetic letters,.

Output Format

Print Yes if you can obtain string
by performing exactly operations on

. Otherwise, print No.

Sample Input 0

hackerhappy
hackerrank
9

Sample Output 0

Yes
'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the appendAndDelete function below.
def appendAndDelete(s, t, k):
    count=0
    for i,j in zip(s,t):
        if(i==j):
            count+=1
        else:
            break
    t_len=len(s)-len(t)
    if(t_len<=2*count+k and t_len%2==k%2 or t_len<k):
        return "Yes"
    else:
        return "No"

if __name__ == '__main__':

    s = input()

    t = input()

    k = int(input())

    result = appendAndDelete(s, t, k)

