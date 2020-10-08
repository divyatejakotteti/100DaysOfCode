'''
You are given a number of sticks of varying lengths. You will iteratively cut the sticks into smaller sticks, discarding the shortest pieces until there are none left. At each iteration you will determine the length of the shortest stick remaining, cut that length from each of the longer sticks and then discard all the pieces of that shortest length. When all the remaining sticks are the same length, they cannot be shortened so discard them.

Given the lengths of
sticks, print the number of sticks that are left before each iteration until there are none left.
Function Description

Complete the cutTheSticks function in the editor below. It should return an array of integers representing the number of sticks before each cut operation is performed.

cutTheSticks has the following parameter(s):

    arr: an array of integers representing the length of each stick

Input Format

The first line contains a single integer
, the size of .
The next line contains space-separated integers, each an where each value represents the length of the

stick.

Output Format

For each operation, print the number of sticks that are present before the operation on separate lines. 
Sample Input 

6
5 4 4 2 2 8

Sample Output 

6
4
2
1

'''

#!/bin/python3

import math
import os
import random
import re
import sys

def cutTheSticks(arr):
    ls = []
    while len(arr) >= 1:
        ls.append(len(arr))
        m = min(arr)
        arr = [i-m for i in arr if i!=m]
    return ls
if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    result = cutTheSticks(arr)