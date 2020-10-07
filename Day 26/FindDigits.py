'''
An integer is a divisor of an integer if the remainder of n%d=0.

Given an integer, for each digit that makes up the integer determine whether it is a divisor. Count the number of divisors occurring within the integer. 
Function Description

Complete the findDigits function in the editor below. It should return an integer representing the number of digits of
that are divisors of.

findDigits has the following parameter(s):

    n: an integer to analyze

Input Format

The first line is an integer,
, indicating the number of test cases.
The subsequent lines each contain an integer, . 
Output Format

For every test case, count the number of digits in
that are divisors of

. Print each answer on a new line.

Sample Input

2
12
1012

Sample Output

2
3

'''

#!/bin/python3

import math
import os
import random
import re
import sys


def findDigits(n):
    count=0
    for i in list(str(n)):
        if(int(i)!=0 and n%int(i)==0):
            count+=1
    return(count)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        n = int(input())

        result = findDigits(n)    
    
    