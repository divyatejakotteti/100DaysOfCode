'''
HackerLand Enterprise is adopting a new viral advertising strategy. When they launch a new product, they advertise it to exactly 5people on social media.

On the first day, half of those 5 people (i.e.floor(5/2) =2, ) like the advertisement and each shares it with of their friends. At the beginning of the second day, floor(5/2)*3 = 2*3 = 6 people receive the advertisement.

Each day,floor(recipients/2) of the recipients like the advertisement and will share it with friends on the following day. Assuming nobody receives the advertisement twice, determine how many people have liked the ad by the end of a given day, beginning with launch day as day 1.

For example, assume you want to know how many have liked the ad by the end of the 5thday.

Day Shared Liked Cumulative
1      5     2       2
2      6     3       5
3      9     4       9
4     12     6      15
5     18     9      24

The cumulative number of likes is 24.

Function Description

Complete the viralAdvertising function in the editor below. It should return the cumulative number of people who have liked the ad at a given time.

viralAdvertising has the following parameter(s):

    n: the integer number of days

Input Format

A single integer,n, denoting a number of days.
Output Format

Print the number of people who liked the advertisement during the first n days.

Sample Input

3

Sample Output

9


'''
#!/bin/python3

import math
import os
import random
import re
import sys

def viralAdvertising(n):
    liked=[2]
    ad=2
    for i in range(n-1):
        ad=ad*3//2
        liked.append(ad)
    return(sum(liked))

if __name__ == '__main__':
    n = int(input())

    result = viralAdvertising(n)