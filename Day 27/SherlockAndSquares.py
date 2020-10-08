'''
Watson likes to challenge Sherlock's math ability. He will provide a starting and ending value describing a range of integers. Sherlock must determine the number of square integers within that range, inclusive of the endpoints.
Function Description

Complete the squares function in the editor below. It should return an integer representing the number of square integers in the inclusive range from
to

.

squares has the following parameter(s):

    a: an integer, the lower range boundary
    b: an integer, the uppere range boundary

Input Format

The first line contains q, the number of test cases.
Output Format

For each test case, print the number of square integers in the range on a new line.

Sample Input

2
3 9
17 24

Sample Output

2
'''
#!/bin/python3

import math
import os
import random
import re
import sys


def squares(a, b):
    sqrtA = math.ceil(math.sqrt(a))
    sqrtB = math.floor(math.sqrt(b))
    return(sqrtB - sqrtA + 1)

if __name__ == '__main__':
    q = int(input())

    for q_itr in range(q):
        ab = input().split()

        a = int(ab[0])

        b = int(ab[1])

        result = squares(a, b)

   
    