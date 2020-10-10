'''
Function Description

Complete the jumpingOnClouds function in the editor below. It should return an integer representing the energy level remaining after the game.

jumpingOnClouds has the following parameter(s):

    c: an array of integers representing cloud types
    k: an integer representing the length of one jump

Input Format

The first line contains two space-separated integers,
and , the number of clouds and the jump distance.
The second line contains space-separated integers where

. Each cloud is described as follows:

    If 

, then cloud
is a cumulus cloud.
If
, then cloud is a thunderhead.
Output Format

Print the final value of

on a new line.

Sample Input

8 2
0 0 1 0 0 1 1 0

Sample Output

92

'''

import math
import os
import random
import re
import sys

def jumpingOnClouds(c, k):
    res=100
    i=0
    while i<len(c):
        i=(i+k)%len(c)
        if(c[i]==1):
            res=res-1-2
        else:
            res-=1
        if(i==0):
            break
    return(res)
        
if __name__ == '__main__':

    nk = input().split()

    n = int(nk[0])

    k = int(nk[1])

    c = list(map(int, input().rstrip().split()))

    result = jumpingOnClouds(c, k)

