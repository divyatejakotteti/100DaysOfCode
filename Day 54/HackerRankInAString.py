'''
We say that a string contains the word hackerrank if a subsequence of its characters spell the word hackerrank. For example, if string it does contain hackerrank, but does not. In the second case, the second r is missing. If we reorder the first string as

, it no longer contains the subsequence due to ordering.

More formally, let
be the respective indices of h, a, c, k, e, r, r, a, n, k in string . If is true, then

contains hackerrank.

For each query, print YES on a new line if the string contains hackerrank, otherwise, print NO.

Function Description

Complete the hackerrankInString function in the editor below. It must return YES or NO.

hackerrankInString has the following parameter(s):

    s: a string

Input Format

The first line contains an integer
, the number of queries.
Each of the next lines contains a single query string

.

Constraints

Output Format

For each query, print YES on a new line if

contains hackerrank, otherwise, print NO.

Sample Input 0

2
hereiamstackerrank
hackerworld

Sample Output 0

YES
NO


'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the hackerrankInString function below.
def hackerrankInString(s):
    str='hackerrank'
    l=0
    for i in s:
        if i==str[l]:
            l+=1
        if l==len(str):
            break
    if l== len(str):
        return "YES"
    else:
        return "NO"
    

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    q = int(input())

    for q_itr in range(q):
        s = input()

        result = hackerrankInString(s)

        fptr.write(result + '\n')

    fptr.close()
