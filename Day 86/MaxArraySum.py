'''
Given an array of integers, find the subset of non-adjacent elements with the maximum sum. Calculate the sum of that subset.

For example, given an array

we have the following possible subsets:

Subset      Sum
[-2, 3, 5]   6
[-2, 3]      1
[-2, -4]    -6
[-2, 5]      3
[1, -4]     -3
[1, 5]       6
[3, 5]       8

Our maximum subset sum is

.

Function Description

Complete the

function in the editor below. It should return an integer representing the maximum subset sum for the given array.

maxSubsetSum has the following parameter(s):

    arr: an array of integers

Input Format

The first line contains an integer,
.
The second line contains space-separated integers

.

Constraints

Output Format

Return the maximum sum described in the statement.

Sample Input 0

5
3 7 4 6 5

Sample Output 0

13

Explanation 0

Our possible subsets are
and . The largest subset sum is from subset

Sample Input 1

5
2 1 5 8 4

Sample Output 1

11

Explanation 1

Our subsets are
and . The maximum subset sum is

from the first subset listed.

Sample Input 2

5
3 5 -7 8 10

Sample Output 2

15


'''
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the maxSubsetSum function below.
def maxSubsetSum(arr):
    n=len(arr)
    x=[0]*n
    x[0]=arr[0]
    x[1]=max(arr[1],x[0])
    for i in range(2,n):
        x[i]=max(arr[i],x[i-1],arr[i]+x[i-2])
    return x[-1]
           

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    res = maxSubsetSum(arr)

    fptr.write(str(res) + '\n')

    fptr.close()
