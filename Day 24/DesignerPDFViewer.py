'''
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:

There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index . There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm^2 assuming all letters are 1mm wide. 
Function Description

Complete the designerPdfViewer function in the editor below.

designerPdfViewer has the following parameter(s):

    int h[26]: the heights of each letter
    string word: a string

Returns

    int: the size of the highlighted area

Input Format

The first line contains 26 space-separated integers describing the respective heights of each consecutive lowercase English letter, ascii[a-z].
The second line contains a single word consisting of lowercase English alphabetic letters.
Sample Input 

1 3 1 3 1 4 1 3 2 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5 5
abc

Sample Output 

9

Explanation 

We are highlighting the word abc:

Letter heights area=1,b=3 and c=1. The tallest letter, b, is3mm high. The selection area for this word is3*1mm*3mm=9mm^2.

Note: Recall that the width of each character is 1mm.

'''
#!/bin/python3

import math
import os
import random
import re
import sys

def designerPdfViewer(h, word):
    max=0
    for i in range(len(word)):
        heights=int(h[ord(word[i])-97])
        if(heights>max):
            temp=heights
            heights=max
            max=temp
    return(max*len(word))

if __name__ == '__main__':
    h = list(map(int, input().rstrip().split()))

    word = input()

    result = designerPdfViewer(h, word)
    
    
    