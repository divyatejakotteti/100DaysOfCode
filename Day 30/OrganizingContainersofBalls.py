'''
David has several containers, each with a number of balls in it. He has just enough containers to sort each type of ball he has into its own container. David wants to sort the balls using his sort method.
David wants to perform some number of swap operations such that:

    Each container contains only balls of the same type.
    No two balls of the same type are located in different containers.

You must perform
queries where each query is in the form of a matrix,

. For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.

Function Description

Complete the organizingContainers function in the editor below. It should return a string, either Possible or Impossible.

organizingContainers has the following parameter(s):

    containter: a two dimensional array of integers that represent the number of balls of each color in each container

Input Format

The first line contains an integer

, the number of queries.

Each of the next

sets of lines is as follows:

    The first line contains an integer 

, the number of containers (rows) and ball types (columns).
Each of the next
lines contains space-separated integers describing row .
Output Format

For each query, print Possible on a new line if David can satisfy the conditions above for the given matrix. Otherwise, print Impossible.

Sample Input 0

2
2
1 1
1 1
2
0 2
1 1

Sample Output 0

Possible
Impossible

'''

import math
import os
import random
import re
import sys

q = int(input())
for q_itr in range(q):
    n = int(input())
    container = []
    for _ in range(n):
        container.append(list(map(int, input().rstrip().split())))
row = []
col = []
for i in range(len(container)):
    row.append(sum(container[i]))
    colSum = 0
    for j in range(len(container)):
        colSum += container[j][i]
    col.append(colSum)
row.sort()
col.sort()
if (row ==col):
    print ("Possible")
else:
    print ("Impossible")
