'''
A jail has a number of prisoners and a number of treats to pass out to them. Their jailer decides the fairest way to divide the treats is to seat the prisoners around a circular table in sequentially numbered chairs. A chair number will be drawn from a hat. Beginning with the prisoner in that chair, one candy will be handed to each prisoner sequentially around the table until all have been distributed.

The jailer is playing a little joke, though. The last piece of candy looks like all the others, but it tastes awful. Determine the chair number occupied by the prisoner who will receive that candy.

For example, there are 4 prisoners and 6 pieces of candy. The prisoners arrange themselves in seats numbered to . Let's suppose two is drawn from the hat. Prisoners receive candy at positions 2,3,4,1,2,3. The prisoner to be warned sits in chair number 3.

Function Description

Complete the saveThePrisoner function in the editor below. It should return an integer representing the chair number of the prisoner to warn.

saveThePrisoner has the following parameter(s):

    n: an integer, the number of prisoners
    m: an integer, the number of sweets
    s: an integer, the chair number to begin passing out sweets from

Input Format

The first line contains an integer,t, denoting the number of test cases.
The next t lines each contain 3 space-separated integers:
- n: the number of prisoners
- m: the number of sweets
- s: the chair number to start passing out treats at
Output Format

For each test case, print the chair number of the prisoner who receives the awful treat on a new line.

Sample Input 

2
5 2 1
5 2 2

Sample Output 

2
3

Explanation 

In first query, there are n=5 prisoners and m=2 sweets. Distribution starts at seat number s=1. Prisoners in seats numbered 1 and 2 get sweets. Warn prisoner 2.
In the second query, distribution starts at seat 2 so prisoners in seats 2 and 3 get sweets. Warn prisoner . 
'''
#!/bin/python3

import math
import os
import random
import re
import sys

def saveThePrisoner(n, m, s):
    m %= n
    s += m - 2
    return 1 + (s % n)

if __name__ == '__main__':
    t = int(input())

    for t_itr in range(t):
        nms = input().split()

        n = int(nms[0])

        m = int(nms[1])

        s = int(nms[2])

        result = saveThePrisoner(n, m, s)
   
    
