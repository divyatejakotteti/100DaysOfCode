'''You are given an array and you need to find number of tripets of indices (i,j,k) such that the elements at those indices are in geometric progression for a given common ratio and i<j<k.
For example,[1,4,16,64]. If r=4, we have [1,4,16] and [4,16,64]at indices (0,1,2)and(1,2,3).

Function Description

Complete the countTriplets function in the editor below. It should return the number of triplets forming a geometric progression for a given

as an integer.

countTriplets has the following parameter(s):

    arr: an array of integers
    r: an integer, the common ratio

Input Format

The first line contains two space-separated integers n and r, the size of arr and the common ratio.
The next line contains space-seperated integers arr[i].
Output Format

Return the count of triplets that form a geometric progression.

Sample Input 

4 2
1 2 2 4

Sample Output 

2


'''
#!/bin/python3

import math
import os
import random
import re
import sys
from collections import Counter

# Complete the countTriplets function below.
def countTriplets(arr, r):
    a={}
    b={}
    count=0
    for i in reversed(arr):
                if i*r in b:
                        count += b[i*r]                        
                if i*r in a:
                        b[i] = b.get(i, 0) + a[i*r]

                a[i] = a.get(i, 0) + 1
    return count
if __name__ == '__main__':

    nr = input().rstrip().split()

    n = int(nr[0])

    r = int(nr[1])

    arr = list(map(int, input().rstrip().split()))

    ans = countTriplets(arr, r)
    
    
    
    
