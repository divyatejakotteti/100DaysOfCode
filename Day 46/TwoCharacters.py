'''
In this challenge, you will be given a string. You must remove characters until the string is made up of any two alternating characters. When you choose a character to remove, all instances of that character must be removed. Your goal is to create the longest string possible that contains just two alternating letters.

As an example, consider the string abaacdabd. If you delete the character a, you will be left with the string bcdbd. Now, removing the character c leaves you with a valid string bdbd having a length of 4. Removing either b or d at any point would not result in a valid string.

Given a string
, convert it to the longest possible string made up only of alternating characters. Print the length of string on a new line. If no string can be formed, print

instead.

Function Description

Complete the alternate function in the editor below. It should return an integer that denotes the longest string that can be formed, or

if it cannot be done.

alternate has the following parameter(s):

    s: a string

Input Format

The first line contains a single integer denoting the length of
.
The second line contains string

.

Constraints

Output Format

Print a single integer denoting the maximum length of
for the given ; if it is not possible to form string , print

instead.

Sample Input

10
beabeefeab

Sample Output

5

'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the alternate function below.
def alternate(s):
    ans=0
    for i in range(0,26):
     for j in range(0,26):
        if i==j:
            continue
        p1 = i
        p2 = j
        flag = 1
        l = 0
        for c in s:
            if ord(c)-ord('a')!=p1 and ord(c)-ord('a')!=p2:
                continue
            if ord(c)-ord('a') == p1:
                l = l + 1
                p1,p2 = p2,p1
            else:
                flag = 0
        if flag == 1 and l>1:
            ans=max(ans,l)

    return ans

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    l = int(input().strip())

    s = input()

    result = alternate(s)

    fptr.write(str(result) + '\n')

    fptr.close()
