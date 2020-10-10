'''
Given a set of distinct integers, print the size of a maximal subset of where the sum of any numbers in is not evenly divisible by .
Function Description

Complete the nonDivisibleSubset function in the editor below. It should return an integer representing the length of the longest subset of

meeting the criteria.

nonDivisibleSubset has the following parameter(s):

    S: an array of integers
    k: an integer

Input Format

The first line contains
space-separated integers, and , the number of values in and the non factor.
The second line contains space-separated integers describing , the unique values of the set.
Output Format

Print the size of the largest possible subset (

).

Sample Input

4 3
1 7 2 4

Sample Output

3

'''
#!/bin/python3

import math
import os
import random
import re
import sys

def nonDivisibleSubset(k, s):
    count=[0]*k
    for i in s:
        count[i%k]+=1
    a=min(count[0],1)
    for i in range(1,k//2+1):
        if(i!=k-i):
            a+=max(count[i],count[k-i])
    if(k%2==0):
        a+=1
    return(a)
   

if __name__ == '__main__':
    first_multiple_input = input().rstrip().split()

    n = int(first_multiple_input[0])

    k = int(first_multiple_input[1])

    s = list(map(int, input().rstrip().split()))

    result = nonDivisibleSubset(k, s)
  
    
    