
#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the minimumBribes function below.
def minimumBribes(q):
    moves = 0 
    
    for i,j in enumerate(q):#i=position & j=value
        
        if (j-1) - i > 2:
            print("Too chaotic")
        for k in range(max(0,j-1),i):
            if q[k] > j:
                moves += 1
    print(moves)
    

#if __name__ == '__main__':
t = int(input())

for t_itr in range(t):
    n = int(input())
    q = list(map(int, input().strip().split()))
    minimumBribes(q)
   
    
    
