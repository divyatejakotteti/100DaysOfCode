'''
Given a sequence of integers, where each element is distinct and satisfies . For each x where 1<=x<n, find any integer y such that p(p(y))=x and print the value of y on a new line.

Function Description

Complete the permutationEquation function in the editor below. It should return an array of integers that represent the values of

.

permutationEquation has the following parameter(s):

    p: an array of integers

Input Format

The first line contains an integer
, the number of elements in the sequence.
The second line contains space-separated integers where .
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def permutationEquation(p):

        print((p.index(p.index(x+1)+1)+1)for x in range(n))

if __name__ == '__main__':

    n = int(input())

    p = list(map(int, input().rstrip().split()))

    permutationEquation(p)   
    
    