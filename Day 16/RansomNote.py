#!/bin/python3

import math
import os
import random
import re
import sys
   
# Complete the checkMagazine function below.
def checkMagazine(magazine, note):
    for i in magazine:
        if i in note:
            magazine.remove(i)
        else:
            return False
    return True
                  
if __name__ == '__main__':
    mn = input().split()

    m = int(mn[0])

    n = int(mn[1])

    magazine = input().rstrip().split()

    note = input().rstrip().split()

    answer=checkMagazine(magazine, note)
    if(answer):
        print("Yes")
    else:
        print("No")
   
    
    