'''
Function Description

Complete the extraLongFactorials function in the editor below. It should print the result and return.

extraLongFactorials has the following parameter(s):

    n: an integer

Note: Factorials of
can't be stored even in a

long long variable. Big integers must be used for such calculations. Languages like Java, Python, Ruby etc. can handle big integers, but we need to write additional code in C/C++ to handle huge values.

We recommend solving this challenge using BigIntegers.

Input Format

Input consists of a single integer 
Output Format

Print the factorial of. 
'''
  
#!/bin/python3

import math
import os
import random
import re
import sys

def extraLongFactorials(n):
    print(math.factorial(n))

if __name__ == '__main__':
    n = int(input())

    extraLongFactorials(n)
  
    
    